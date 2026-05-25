# FileStream Protocol (FSP Push) — Specification v0.2

Last Update: 26/01/2026 - Julien BOUCARON

# 1. Overview

The **FileStream Protocol Push (FSP Push)** is a simple, streaming *push-mode* protocol for dumping filesystem contents from a sender to a receiver over a reliable byte stream.

FSP Push is designed for fast, one-way transfers of regular files and directories, including:

* dumping photos and videos from mobile devices
* transferring large media collections
* dumping and mirroring source trees
* transferring build artifacts
* deploying application payloads

FSP Push serializes filesystem operations and file data into a **single, linear command stream** optimized for:

* maximum sustained throughput
* high latency or unstable links
* minimal protocol overhead
* single-pass, sequential IO

FSP Push operates exclusively in **push mode**, with all commands and data flowing from sender to receiver.

---

## Motivation and performance model (informative)

FSP Push is designed around the physical realities of modern networks, storage, and operating systems. In many real-world scenarios, the primary performance limitation is not raw bandwidth, but **latency and application-layer round trips**.

### Latency dominates small-file workloads

On many real-world links, especially:

* WAN links
* VPNs
* SSH tunnels
* Mobile networks
* Multi-hop routed paths

The dominant cost is round-trip time (RTT), not throughput.

Protocols that perform per-file request/response exchanges (e.g. open, stat, confirm, close) introduce protocol-level pauses between files. Even when each pause is small, this forces the sender to wait for one or more RTTs per file.

For workloads with many small files, this results in:

* idle gaps between files
* collapsing of TCP congestion windows
* poor utilization of available bandwidth
* throughput dominated by RTT instead of link speed

In practice, this can reduce effective throughput by **orders of magnitude**.

### Continuous streaming keeps the transport pipe full

FSP Push is explicitly designed to eliminate application-layer round-trip dependencies. Once a FILE_LIST and its associated data stream begin, the sender can continuously stream bytes without waiting for per-file acknowledgements or protocol responses.

This allows:

* the TCP congestion window to remain open
* the bandwidth-delay product (BDP) to stay utilized
* the transport to operate at steady state
* the link to be limited only by network and storage performance

In this model, the application never intentionally introduces idle periods. Back-pressure is provided solely by:

* TCP flow control
* TCP congestion control
* receiver socket buffers
* receiver disk write speed

These are natural, transport-level mechanisms and do not require protocol-level pauses.

This is analogous to a continuous pipeline: once started, the system runs at the maximum rate allowed by the slowest physical component.

### Multihop and tunneled paths amplify the benefit

On paths with intermediate hops, tunnels, proxies, or relays, RTT is often higher and more variable. Each additional hop increases the cost of per-file protocol exchanges.

By avoiding protocol-level synchronization points, FSP Push is well-suited for:

* SSH tunnels
* VPNs
* NAT traversal
* bastion hosts
* cloud-to-cloud transfers
* mobile-to-desktop transfers

Even when bandwidth is modest, eliminating RTT-bound stalls allows sustained streaming and significantly improves real-world throughput.

### Interaction with TCP and back-pressure

FSP Push does not bypass transport-layer flow control or congestion control. TCP still governs:

* send rate
* receive window
* congestion response
* packet loss recovery

However, by removing application-layer stalls, FSP Push ensures that:

* TCP always has data available to send
* the sender is not artificially idle
* throughput is governed by network and storage, not protocol design

The protocol introduces **no intentional application-layer pauses**.

### Compression and streaming pipelines

The continuous byte stream produced by FSP Push is friendly to intermediate compression and encryption layers. Long-lived streams allow compressors to:

* maintain large dictionaries across file boundaries
* avoid frequent flushes
* improve compression efficiency
* reduce per-file overhead

This improves both compression ratio and CPU efficiency, particularly for workloads with repeated metadata, similar files, or structured content.

### Intended workload

FSP Push is optimized for fast, one-way dumping of regular filesystem content, such as:

* photos and videos from mobile devices
* media collections
* source trees
* build artifacts
* application payloads

### Non-goals (informative)

FSP Push is **not** a synchronization or delta-transfer protocol.

FSP Push is **not** intended for:

* live databases
* block devices
* sparse files
* continuously mutating datasets

Such workloads require application-level or block-level replication mechanisms.

## Illustrative performance examples (informative)

The following table illustrates how protocol-level round trips dominate performance for workloads with many small files, even on fast links. These are not precise benchmarks, but realistic order-of-magnitude estimates.

### Assumptions

* Average small file size: 8 KB
* Per-file protocol cost (FTP/SFTP/SMB): \~1 RTT per file (RTT-bound)
* FSP Push: no per-file RTT dependency (noRTT)
* TCP window large enough to stream at line rate
* Disk IO is not the bottleneck


| Scenario                             | Link / RTT       | Files / Total Data       | RTT-bound                 | noRTT          |
| ------------------------------------ | ---------------- | ------------------------ | ------------------------- | -------------- |
| Fast LAN                             | 1 Gbps / 0.3 ms  | 10,000 × 8 KB (80 MB)   | \~3 seconds               | \~0.7 seconds  |
| Office VPN / multi-hop LAN           | 1 Gbps / 8 ms    | 10,000 × 8 KB (80 MB)   | \~80 seconds              | \~0.7 seconds  |
| WAN, medium latency                  | 100 Mbps / 40 ms | 10,000 × 8 KB (80 MB)   | \~400 seconds (\~6.5 min) | \~6.4 seconds  |
| Lots of tiny files (bad case)        | 100 Mbps / 40 ms | 100,000 × 4 KB (400 MB) | \~4,000 sec (\~66 min)    | \~32 seconds   |
| High bandwidth, high latency (cloud) | 10 Gbps / 80 ms  | 10,000 × 8 KB (80 MB)   | \~800 seconds (\~13 min)  | \~0.06 seconds |

Actual performance may be limited by disk IO, CPU, TCP congestion control, or receiver back-pressure, but FSP Push removes per-file RTT as a first-order term.

These examples assume a single outstanding file per RTT for RTT-bound protocols, which is common in naive implementations.

### Interpretation

For per-file protocols:

```
Total time ≈ file_count × RTT  +  data_size / bandwidth
```

For FSP Push:

```
Total time ≈ data_size / bandwidth
```

When `file_count × RTT` dominates, **protocol design — not bandwidth — determines performance**.

FSP Push eliminates application-layer round trips, allowing sustained streaming and making throughput dependent only on network and storage limits.

# 2. Design principles

* Streaming-first
* No global manifest
* Linear command stream
* Minimal state
* Immediate application
* Transport-agnostic
* Push-only semantics
* Client-declared transfer behavior
* Safety over implicit filesystem semantics
* Integrity over performance shortcuts

---

# 3. Transport assumptions

FSP Push requires a reliable, ordered byte stream (e.g. TCP, TLS, QUIC).

* FSP Push uses a single ordered stream per session.
* Stream multiplexing is out of scope.

---

# 4. Data encoding

* All integers are encoded in **network byte order (big-endian)**.
* This applies to all integer widths, including `uint64`.
* Paths are opaque byte strings (typically UTF-8).
* All paths are interpreted as **absolute paths relative to a receiver-defined root**.

---

# 5. Protocol header

```
uint32  magic   = 0x46535031   // "FSP1"
uint16  version = 2
uint16  flags
```

* `flags` MUST be zero in v0.2.
* Unsupported magic or version MUST cause rejection.

---

# 6. Command stream

After the header, the stream consists of a sequence of commands sent from sender to receiver:

* `SET_MODE`
* `MKDIR` (optional / deprecated)
* `FILE_LIST`
* `END`

Commands are processed strictly in order.
There are no protocol phases and no nesting.

---

# 7. SET_MODE command (client-declared behavior)

Declares how the receiver MUST handle existing paths for subsequent FILE\_LIST commands.

```
uint8   cmd = 0x10
uint8   mode
```

The declared mode applies to all following FILE\_LIST commands until changed by another SET_MODE.

### Modes


| Value | Name                         | Semantics                              |
| ----- | ---------------------------- | -------------------------------------- |
| 0x01  | OVERWRITE\_ALWAYS            | Always overwrite existing files        |
| 0x02  | SKIP\_IF\_EXISTS             | Skip writing if file exists            |
| 0x03  | OVERWRITE\_IF\_HASH\_DIFFERS | Overwrite only if final SHA256 differs |
| 0x04  | FAIL\_IF\_EXISTS             | Error if file exists                   |

Semantics:

* Default mode if SET_MODE is not sent: **OVERWRITE_ALWAYS**
* Receiver MUST apply the active mode to each file in subsequent FILE_LIST
* Mode changes take effect immediately
* Receiver MAY reject unsupported modes
* Size- or timestamp-based overwrite modes are NOT supported

---

# 8. MKDIR command (optional / deprecated)

> NOTE: MKDIR is OPTIONAL in FSP Push v0.2 and MAY be omitted.
> Receivers SHOULD create parent directories implicitly from file paths.

Creates a directory on the receiver.

```
uint8   cmd = 0x01
uint16  path_len
bytes   path
```

Semantics:

* `path` is absolute.
* Creation is idempotent (`mkdir -p` semantics).
* Missing parents MAY be created implicitly.
* Receivers MAY ignore MKDIR entirely.
* Permissions, ownership, and timestamps are out of scope.

---

# 9. FILE_LIST command (with prefix and chunked hashes)

Declares a list of files sharing a common prefix path, immediately followed by their data.

### Constants

* **CHUNK_SIZE = 134,217,728 bytes (128 MB)**

### Format

```
uint8   cmd = 0x02
uint16  prefix_len
bytes   prefix_path        // may be empty, MUST end with "/" if non-empty
uint32  count
repeat count times:
  uint16 relative_path_len
  bytes  relative_path
  uint64 size

  uint32 chunk_count
  repeat chunk_count times:
    uint8 chunk_sha256[32]

  uint8 final_sha256[32]
```

### Semantics

* `prefix_path` is an absolute path and MAY be empty.
* If non-empty, `prefix_path` MUST end with `/`.
* Each file’s full path is:

  ```
  full_path = prefix_path + relative_path
  ```
* `relative_path` MUST NOT be absolute.
* `relative_path` MUST NOT contain `..` path components.

  * Receivers SHOULD normalize path separators and reject paths containing platform-specific path traversal sequences.
* Each file declares:

  * Exact byte size
  * SHA256 for each 128 MB chunk (except last partial chunk)
  * Final SHA256 of the entire file
* `chunk_count` MUST equal:

  ```
  ceil(size / CHUNK_SIZE)
  ```

  The final chunk MAY be smaller than CHUNK_SIZE.
* Senders SHOULD limit individual FILE_LIST groups to a maximum total declared size (e.g. 512 MB–2 GB) to balance memory usage and batching efficiency.

---

# 10. FILE data stream

Immediately following a FILE_LIST command, the sender transmits:

```
[file1 bytes][file2 bytes]...[fileN bytes]
```

### Semantics

* Files are sent in the same order as declared.
* No delimiters or markers are used.
* Sizes define file boundaries.

### Chunk verification

For each file, the receiver:

* Writes data sequentially
* Computes SHA256 for each 128 MB chunk
* Verifies each chunk hash as soon as the chunk completes
* Computes final SHA256 for entire file
* Verifies final SHA256 after file close

On mismatch of:

* Any chunk hash, OR
* Final file hash

Then:

* Receiver SHOULD treat this as a data integrity error
* Receiver SHOULD abort the session

This allows:

* Early corruption detection
* Bounded wasted IO (≤ 128 MB)

---

# 11. Directory handling

* Parent directories for files MUST be created implicitly if missing.
* Directory creation is idempotent.
* Pre-existing directories MUST NOT cause errors.
* MKDIR commands MAY be ignored.

---

# 12. Filesystem safety rules

To ensure safe and deterministic behavior:

* Only regular files and directories are supported.
* Symbolic links, hard links, device nodes, fifos, and other special files are NOT supported.
* Senders SHOULD skip such entries.
* Receivers SHOULD reject or skip such entries if encountered.
* Receivers MUST NOT follow symbolic links when creating or writing files.
* Receivers MUST ensure that normalized paths do not escape the receiver-defined root.
* If two entries within the same session map to the same destination path, this MUST be treated as a duplicate filename condition.

---

# 13. Command ordering rules

* SET\_MODE MAY appear at any time.
* Mode applies to subsequent FILE\_LIST only.
* Any number of MKDIR commands MAY appear consecutively.
* FILE\_LIST commands MAY appear multiple times.
* FILE\_LIST MUST be immediately followed by its file data.
* END MUST be the final command.

---

# 14. Receiver state model

The receiver maintains only two states:

* **COMMAND**
* **DATA**

Additionally, the receiver maintains one session variable:

* **current\_mode**

No full-file or manifest buffering is required.

---

# 15. Error handling

On error (short read, disk full, permission denied, FAIL\_IF\_EXISTS, hash mismatch, etc.):

* Receiver MAY abort immediately.
* Partial results MAY remain on disk.
* Resume/recovery is out of scope.
* Stream resynchronization is not supported.

---

# 16. Durability considerations

Durability is implementation-defined.

Receivers SHOULD periodically flush written data to stable storage.
Flush frequency MAY be based on:

* Per-file
* Cumulative written size thresholds
* End of session
* Implementation policy

Durability behavior is not signaled on the wire.

---

# 17. Security considerations

* FSP Push provides no built-in security.
* Encryption and authentication MUST be provided by the transport layer if required.
* Receivers MUST enforce filesystem safety rules.
* Receivers MUST protect against path traversal and symlink attacks.

---

# 18. Out of scope (v0.2)

* permissions
* ownership
* timestamps
* symbolic links (as transferable objects)
* hard links
* sparse files
* resume / checkpointing
* compression

---

# 19. Sender Batching Guidance

To achieve optimal performance, senders SHOULD batch multiple files into each FILE\_LIST. FILE_LIST commands containing only a single file or very small numbers of files defeat the streaming and batching advantages of the protocol. Typical implementations SHOULD batch files by directory and/or accumulate files until a reasonable size or count threshold is reached (e.g. hundreds of files or hundreds of megabytes) before emitting a FILE\_LIST.

If your wire trace looks like:

> FILE\_LIST, data, FILE\_LIST, data, FILE\_LIST, data (many times)

You’re doing it wrong.

If it looks like:

> FILE\_LIST (big), data (big), FILE\_LIST (big), data (big)

You’re doing it right.

# Platform & Filesystem Quirks (new section for v0.2)

### Supported File Types

Only the following filesystem objects are processed:

* regular files
* directories

All other file types MUST be skipped:

* symbolic links
* hard links
* device nodes
* FIFOs
* sockets
* special or platform-specific types

---

### Path & Filename Handling

To ensure portability across platforms (Linux, macOS, Windows, Android, FAT/exFAT, network filesystems), implementations MUST handle invalid or unsupported paths safely.

#### Invalid or Unsupported Filenames

If a filename or path component is invalid on the target platform, the receiver MUST either:

* fail the transfer, OR
* skip the affected entry

The chosen behavior SHOULD be configurable.

Examples of invalid or problematic names:

* Windows reserved names: `CON`, `PRN`, `AUX`, `NUL`, `COM1`, `LPT1`, etc.
* Names containing forbidden characters (e.g. `: * ? " < > |` on Windows)
* Names exceeding platform filename limits

---

### Duplicate Filenames (Case Folding, Normalization)

On case-insensitive or Unicode-normalizing filesystems (e.g. Windows, macOS, FAT, some Android filesystems), distinct source paths may collide on the destination.

If two source paths map to the same destination path, the receiver MUST either:

* fail the transfer, OR
* skip one of the conflicting entries

The chosen behavior SHOULD be configurable.

---

### Reserved or Special Paths

Paths that map to special namespaces or devices on the receiver MUST be skipped, including (non-exhaustive):

* Windows device paths
* `/dev/*`, `/proc/*`, `/sys/*`
* platform-reserved namespaces

# Appendix

## Updates on 22/01/2026

* Version bumped to v0.2.
* Fixed 128 MB chunk size.
* Per-chunk SHA256 hashes added.
* Final per-file SHA256 added.
* Hash-based overwrite semantics added.
* Path traversal and symlink handling rules tightened.
* FILE\_LIST batching limits added.
* Size- and timestamp-based overwrite modes removed.
* Durability behavior clarified.

## Updates on 23/01/2026

* Platform specifics: supported file types, path & filename handling, duplicate filenames, reserved or special paths

## Updates on 26/01/2026

* Add motivation and performance model (informative): latency is the enemy, As networks become more reliable and higher bandwidth, latency becomes the dominant limiting factor.
* Add illustrative performance examples (informative): show how the latency kills the performance of high speed networks.
* Add the core rule: prevent bad implementation, limit on chunk size and limit on max number of files to be sent.