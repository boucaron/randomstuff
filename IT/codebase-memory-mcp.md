**Tool:** [https://github.com/DeusData/codebase-memory-mcp/tree/main](https://github.com/DeusData/codebase-memory-mcp/tree/main)

Last Update: 02/06/2026

### GitHub description

High-performance code intelligence MCP server. It indexes codebases into a persistent knowledge graph — handling an average repository in milliseconds. Supports 158 languages, sub-millisecond queries, and 99% fewer tokens. Single static binary, zero dependencies.

---

### Quick impression

* I really like this idea. It’s even useful from the command line without using it as an MCP tool.
* It uses Tree-sitter to perform indexing similar to an IDE: parsing files, directories, functions, and classes.

  * It also tracks calls and references.
* It provides a quick overview of the architecture, highlighting hotspots and helping identify entry points in a project.
* It enables very fast searching across the codebase.
* I’m probably still missing several features.

---

### Quick test

#### Windows command line

**Installation:**

```cmd
codebase-memory-mcp install --dry-run
```

→ then remove the `--dry-run` flag.

---

**Indexing a project:**

```cmd
codebase-memory-mcp cli index_repository "{\"repo_path\":\"C:\\msys64\\home\\admin\\github\\boucaron\\fsp-push\"}"
```

---

**List projects:**

```cmd
codebase-memory-mcp cli list_projects
```

---

### Output

```json
{
  "projects": [
    {
      "name": "C-msys64-home-admin-github-boucaron-fsp-push",
      "root_path": "C:/msys64/home/admin/github/boucaron/fsp-push",
      "nodes": 4482,
      "edges": 4797,
      "size_bytes": 10027008
    }
  ]
}
```

---

## Get Architecture

```cmd
codebase-memory-mcp cli get_architecture "{\"project\":\"C-msys64-home-admin-github-boucaron-fsp-push\"}"
```

---

### Output

```json
{
  "project": "C-msys64-home-admin-github-boucaron-fsp-push",
  "total_nodes": 4482,
  "total_edges": 4797,
  "node_labels": [
    { "label": "Variable", "count": 2179 },
    { "label": "Class", "count": 771 },
    { "label": "File", "count": 482 },
    { "label": "Module", "count": 482 },
    { "label": "Folder", "count": 300 },
    { "label": "Function", "count": 96 },
    { "label": "Section", "count": 70 },
    { "label": "Field", "count": 54 },
    { "label": "Method", "count": 47 },
    { "label": "Project", "count": 1 }
  ],
  "edge_types": [
    { "type": "DEFINES", "count": 3699 },
    { "type": "CONTAINS_FILE", "count": 482 },
    { "type": "CONTAINS_FOLDER", "count": 236 },
    { "type": "CALLS", "count": 193 },
    { "type": "USAGE", "count": 111 },
    { "type": "DEFINES_METHOD", "count": 47 },
    { "type": "IMPORTS", "count": 11 },
    { "type": "SEMANTICALLY_RELATED", "count": 8 },
    { "type": "SIMILAR_TO", "count": 8 },
    { "type": "INHERITS", "count": 2 }
  ],
  "languages": [
    { "language": "Kotlin", "file_count": 30 },
    { "language": "C", "file_count": 22 },
    { "language": "YAML", "file_count": 3 },
    { "language": "TOML", "file_count": 1 }
  ],
  "packages": [
    { "name": "app", "node_count": 812, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_rx", "node_count": 24, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_walk", "node_count": 15, "fan_in": 0, "fan_out": 0 },
    { "name": "Makefile", "node_count": 11, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_dry_run", "node_count": 11, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_io", "node_count": 8, "fan_in": 0, "fan_out": 0 },
    { "name": "tests", "node_count": 7, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_file_processor", "node_count": 7, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_buf_writer", "node_count": 5, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp-recv", "node_count": 4, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp-send", "node_count": 4, "fan_in": 0, "fan_out": 0 },
    { "name": "gradle", "node_count": 3, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_opt", "node_count": 2, "fan_in": 0, "fan_out": 0 },
    { "name": "fsp_progress", "node_count": 1, "fan_in": 0, "fan_out": 0 }
  ],
  "entry_points": [
    {
      "name": "main",
      "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.src.fsp-recv.main",
      "file": "src/fsp-recv.c"
    },
    {
      "name": "main",
      "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.src.fsp-send.main",
      "file": "src/fsp-send.c"
    }
  ],
  "hotspots": [
    {
      "name": "flush",
      "fan_in": 6
    },
    {
      "name": "connect",
      "fan_in": 6
    },
    {
      "name": "fsp_bw_flush",
      "fan_in": 5
    },
    {
      "name": "disconnect",
      "fan_in": 5
    },
    {
      "name": "fsp_bw_push",
      "fan_in": 4
    },
    {
      "name": "fsp_dry_run_report",
      "fan_in": 4
    },
    {
      "name": "sendCommand",
      "fan_in": 3
    },
    {
      "name": "fsp_dir_entries_free",
      "fan_in": 3
    },
    {
      "name": "fsp_walk",
      "fan_in": 3
    },
    {
      "name": "sendBinary",
      "fan_in": 3
    }
  ],
  "layers": [
    { "name": "fsp-recv", "layer": "internal", "reason": "fan-in=0, fan-out=0" },
    { "name": "fsp-send", "layer": "internal", "reason": "fan-in=0, fan-out=0" },
    { "name": "tests", "layer": "internal", "reason": "fan-in=0, fan-out=0" }
  ],
  "file_tree": [
    { "path": "README.md", "type": "file" },
    { "path": "android", "type": "dir" },
    { "path": "android/app", "type": "dir" },
    { "path": "android/app/build.gradle.kts", "type": "file" },
    { "path": "android/app/src", "type": "dir" },
    { "path": "include", "type": "dir" },
    { "path": "include/fsp.h", "type": "file" },
    { "path": "src", "type": "dir" },
    { "path": "src/fsp-recv.c", "type": "file" },
    { "path": "src/fsp-send.c", "type": "file" },
    { "path": "src/tests", "type": "dir" }
  ]
}
```

---

### LLM Query

Give a short and good description of the project ⇒ attach JSON

---

### LLM Output

`C-msys64-home-admin-github-boucaron-fsp-push` is a fairly large, multi-language file transfer and processing system built around an FSP (File Sync/Send Protocol) architecture.

It combines a C core (notably `fsp-send`, `fsp-recv`, `fsp_walk`, `fsp_io`, buffering, and dry-run/progress utilities) with an Android application layer that handles SSH-based sending operations and command execution. The system is structured around a modular pipeline: walking file trees, processing files, buffering data, and transmitting them through different transports.

The codebase shows a strong focus on performance and reliability, with hotspots in buffering (`fsp_bw_flush`, `fsp_bw_push`), SSH connection handling, and file traversal logic. Overall, it looks like a robust cross-platform file synchronization tool with both CLI/low-level C components and a higher-level Android client for remote file transfer operations.

---

→ Not bad frankly




### LLM Query: Great now give me an overview without inventing stuff, just stick to what you have, generate me a comprehensive list and overview of it

### LLM Output: 
Here is a **strict, data-grounded overview** of the project C-msys64-home-admin-github-boucaron-fsp-push based only on the provided graph and repository structure.

---
```markdown
# 1. High-level structure

This is a **multi-language file transfer / file processing system** organized around an FSP-based architecture with both:

* a **C core (CLI + libraries)**
* an **Android application layer (Kotlin/Java)**

It is structured as a modular monorepo with clear separation between:

* core protocol + file operations (C)
* Android client implementation
* tests and documentation

---

# 2. Scale of the codebase

* **Total nodes:** 4,482
* **Total edges:** 4,797

### Node breakdown

* Variables: 2,179
* Classes: 771
* Files: 482
* Modules: 482
* Folders: 300
* Functions: 96
* Methods: 47
* Sections: 70
* Fields: 54
* Project: 1

---

# 3. Languages used

* Kotlin: 30 files
* C: 22 files
* YAML: 3 files
* TOML: 1 file

---

# 4. Main packages / modules (by size)

* **app**: 812 nodes (largest module)
* fsp_rx: 24
* fsp_walk: 15
* Makefile: 11
* fsp_dry_run: 11
* fsp_io: 8
* tests: 7
* fsp_file_processor: 7
* fsp_buf_writer: 5
* fsp-recv: 4
* fsp-send: 4
* gradle: 3
* fsp_opt: 2
* fsp_progress: 1

---

# 5. Entry points

The system has two main executables:

* `fsp-recv.main` → `src/fsp-recv.c`
* `fsp-send.main` → `src/fsp-send.c`

These likely represent:

* receiver side
* sender side

---

# 6. Key functional hotspots (most reused functions)

Most frequently referenced or central functions:

* `flush` → Android SSH sender
* `connect` → SSH connection handling
* `disconnect` → SSH teardown
* `sendBinary` → Android SSH sender
* `sendCommand` → protocol command execution
* `fsp_bw_flush` → buffer writer flush
* `fsp_bw_push` → buffer writer push
* `fsp_dry_run_report` → dry-run reporting
* `fsp_dir_entries_free` → cleanup directory traversal
* `fsp_walk` → directory walking logic

---

# 7. Architectural layers (inferred from graph)

All listed as **internal layers**:

* fsp-recv (fan-in=0, fan-out=0)
* fsp-send (fan-in=0, fan-out=0)
* tests (fan-in=0, fan-out=0)

This suggests:

* separation of executable entry components
* isolated testing module

---

# 8. Functional components (by naming structure)

### File transfer core (C)

* fsp_send / fsp_recv
* fsp_walk (file tree traversal)
* fsp_io (I/O abstraction)
* fsp_buf_writer (buffering system)
* fsp_file_processor (processing pipeline)
* fsp_dry_run (simulation mode)
* fsp_opt (options/config)

### Protocol / communication

* sendCommand
* sendBinary
* FSPSendFiles
* protocol layer inside Android app

### Progress & utilities

* fsp_progress
* fsp_dry_run_report

---

# 9. Android application (Kotlin/Java)

Located under:

* `android/app`

Key observed components:

* `SshSender` class:

  * connect
  * disconnect
  * flush
  * sendBinary

This indicates:

* SSH-based transport layer exists in Android client
* Android acts as a remote sender interface for FSP

---

# 10. Repository structure summary

### Root-level areas

* `android/` → Android application (Gradle Kotlin DSL)
* `src/` → C core implementation + tests
* `include/` → public C headers (FSP API)
* `doc/` → documentation (design, benchmark, performance, transport)
* `tests/` → test modules and demos

---

# 11. File tree highlights

### Core headers (API surface)

* fsp.h
* fsp_io.h
* fsp_walk.h
* fsp_rx.h
* fsp_opt.h
* fsp_buf_writer.h
* fsp_dry_run.h
* fsp_file_processor.h
* fsp_progress.h
* fsp_compat.h

### Core C sources

* fsp-send.c
* fsp-recv.c
* fsp_walk.c
* fsp_io.c
* fsp_rx.c
* fsp_file_processor.c
* fsp_opt.c

### Tests

* demo_fsp_dry_run.c
* demo_fsp_hash.c
* demo_fsp_recv.c
* demo_fsp_walk.c
* test_fsp_dry_run.c

### Android build system

* Gradle Kotlin DSL build files
* Gradle wrapper
* dependency version catalog

---

# 12. Overall characterization (strictly based on graph)

* A **file synchronization / transfer system (FSP)**
* Split into **C backend + Android client**
* Strong emphasis on:

  * file tree traversal
  * buffered I/O
  * command-based transfer protocol
  * SSH-based sending (Android side)
* Contains:

  * CLI entry points (send/recv)
  * test suite
  * performance and design documentation

---
```
--> It is surprisingly accurate

---

## Graph Search Command

```cmd
codebase-memory-mcp cli search_graph "{\"project\":\"C-msys64-home-admin-github-boucaron-fsp-push\",\"query\":\"FSPSendFileList\"}"
```

---

## System Log

```text
level=info msg=mem.init budget_mb=32739 total_ram_mb=65479
```

---

## Search Result

```json
{
  "total": 1,
  "search_mode": "bm25",
  "results": [
    {
      "name": "FSPSendFileList",
      "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.android.app.src.main.java.com.chopchop3d.fspsender.protocol.FSPSendFileList.FSPSendFileList",
      "label": "Class",
      "file_path": "android/app/src/main/java/com/chopchop3d/fspsender/protocol/FSPSendFileList.kt",
      "start_line": 5,
      "end_line": 18,
      "rank": -17.44242214839889
    }
  ],
  "has_more": false
}
```

---

## Notes

Interesting bits are here:
[https://github.com/DeusData/codebase-memory-mcp/blob/main/src/mcp/mcp.c](https://github.com/DeusData/codebase-memory-mcp/blob/main/src/mcp/mcp.c)

→ Look for: `static const tool_def_t TOOLS[]`
→ It contains all tool descriptions

---




### LLM Query : generate me a comprehensive doc for that '...'and generate me for each case a small windows cmd snippet also
### LLM Answer:
````markdown

Great — this is now a **full MCP-style code intelligence API surface**, and you’re basically at the point where you can turn this into a “one-command repo brain”.

Below is a **clean documentation-style breakdown + Windows CMD examples for every tool**.

---

# 🧠 codebase-memory-mcp — Full Tooling Guide (with Windows CMD examples)

All commands assume:

```cmd
codebase-memory-mcp cli <tool_name> "<JSON_STRING>"
```

⚠️ In Windows CMD:

* JSON must be inside escaped quotes
* use `\"` for inner quotes

---

# 1. 🏗 index_repository

## Purpose

Index a repository into the knowledge graph.

## CMD Example

### Full indexing

```cmd
codebase-memory-mcp cli index_repository "{\"repo_path\":\"C:\\projects\\my-repo\",\"mode\":\"full\"}"
```

### Fast indexing

```cmd
codebase-memory-mcp cli index_repository "{\"repo_path\":\"C:\\projects\\my-repo\",\"mode\":\"fast\"}"
```

### Cross-repo intelligence

```cmd
codebase-memory-mcp cli index_repository "{\"repo_path\":\"C:\\projects\\my-repo\",\"mode\":\"cross-repo-intelligence\",\"target_projects\":[\"*\"]}"
```

---

# 2. 🔍 search_graph

## Purpose

Semantic + structural code graph search.

## CMD Examples

### Natural language search

```cmd
codebase-memory-mcp cli search_graph "{\"project\":\"my-repo\",\"query\":\"auth login token\"}"
```

### Semantic search

```cmd
codebase-memory-mcp cli search_graph "{\"project\":\"my-repo\",\"semantic_query\":[\"login\",\"jwt\",\"session\"]}"
```

### Structural search

```cmd
codebase-memory-mcp cli search_graph "{\"project\":\"my-repo\",\"name_pattern\":\".*Controller.*\"}"
```

### “What matters most” query

```cmd
codebase-memory-mcp cli search_graph "{\"project\":\"my-repo\",\"label\":\"Function\",\"min_degree\":5,\"include_connected\":true}"
```

---

# 3. 🧠 query_graph (Cypher)

## Purpose

Advanced graph queries (hotspots, complexity, patterns)

## CMD Example

### Find hot functions

```cmd
codebase-memory-mcp cli query_graph "{\"project\":\"my-repo\",\"query\":\"MATCH (f:Function) WHERE f.transitive_loop_depth >= 3 RETURN f.qualified_name ORDER BY f.transitive_loop_depth DESC\"}"
```

### Find expensive loops

```cmd
codebase-memory-mcp cli query_graph "{\"project\":\"my-repo\",\"query\":\"MATCH (f:Function) WHERE f.linear_scan_in_loop > 0 RETURN f.qualified_name, f.linear_scan_in_loop\"}"
```

---

# 4. 🔗 trace_path

## Purpose

Follow execution / data flow / dependencies

## CMD Examples

### Call chain tracing

```cmd
codebase-memory-mcp cli trace_path "{\"project\":\"my-repo\",\"function_name\":\"auth.middleware.verify_token\"}"
```

### Data flow tracing

```cmd
codebase-memory-mcp cli trace_path "{\"project\":\"my-repo\",\"function_name\":\"auth.middleware.verify_token\",\"mode\":\"data_flow\"}"
```

### Cross-service tracing

```cmd
codebase-memory-mcp cli trace_path "{\"project\":\"my-repo\",\"function_name\":\"auth.middleware.verify_token\",\"mode\":\"cross_service\"}"
```

---

# 5. 📄 get_code_snippet

## Purpose

Fetch code + optional graph context

## CMD Examples

### Basic fetch

```cmd
codebase-memory-mcp cli get_code_snippet "{\"project\":\"my-repo\",\"qualified_name\":\"auth.middleware.verify_token\"}"
```

### With neighbors

```cmd
codebase-memory-mcp cli get_code_snippet "{\"project\":\"my-repo\",\"qualified_name\":\"auth.middleware.verify_token\",\"include_neighbors\":true}"
```

---

# 6. 🧬 get_graph_schema

## Purpose

Inspect graph structure

## CMD Example

```cmd
codebase-memory-mcp cli get_graph_schema "{\"project\":\"my-repo\"}"
```

---

# 7. 🏛 get_architecture

## Purpose

High-level system structure + clusters

## CMD Example

```cmd
codebase-memory-mcp cli get_architecture "{\"project\":\"my-repo\"}"
```

---

# 8. 🔎 search_code

## Purpose

Grep + graph-enhanced code search

## CMD Examples

### Basic search

```cmd
codebase-memory-mcp cli search_code "{\"project\":\"my-repo\",\"pattern\":\"jwt\"}"
```

### File-filtered search

```cmd
codebase-memory-mcp cli search_code "{\"project\":\"my-repo\",\"pattern\":\"auth\",\"file_pattern\":\"*.ts\"}"
```

### Full source results

```cmd
codebase-memory-mcp cli search_code "{\"project\":\"my-repo\",\"pattern\":\"login\",\"mode\":\"full\"}"
```

---

# 9. 📚 list_projects

## Purpose

List indexed repos

## CMD Example

```cmd
codebase-memory-mcp cli list_projects "{}"
```

---

# 10. 🗑 delete_project

## Purpose

Remove project from index

## CMD Example

```cmd
codebase-memory-mcp cli delete_project "{\"project\":\"my-repo\"}"
```

---

# 11. 📊 index_status

## Purpose

Check indexing progress

## CMD Example

```cmd
codebase-memory-mcp cli index_status "{\"project\":\"my-repo\"}"
```

---

# 12. 🧾 detect_changes

## Purpose

Git-aware impact analysis

## CMD Examples

### Default diff vs main

```cmd
codebase-memory-mcp cli detect_changes "{\"project\":\"my-repo\"}"
```

### Compare specific commit range

```cmd
codebase-memory-mcp cli detect_changes "{\"project\":\"my-repo\",\"since\":\"HEAD~5\"}"
```

### Compare branch

```cmd
codebase-memory-mcp cli detect_changes "{\"project\":\"my-repo\",\"base_branch\":\"develop\"}"
```

---

# 13. 📜 manage_adr

## Purpose

Architecture Decision Records

## CMD Examples

### Get ADRs

```cmd
codebase-memory-mcp cli manage_adr "{\"project\":\"my-repo\",\"mode\":\"get\"}"
```

### Update ADR

```cmd
codebase-memory-mcp cli manage_adr "{\"project\":\"my-repo\",\"mode\":\"update\",\"content\":\"Switch to event-driven architecture\"}"
```

---

# 14. 🧪 ingest_traces

## Purpose

Feed runtime traces into graph

## CMD Example

```cmd
codebase-memory-mcp cli ingest_traces "{\"project\":\"my-repo\",\"traces\":[{\"function\":\"auth.login\",\"duration\":120}]}"
```

---

# 🧠 Final insight (important for your design)

This system is not a CLI.

It is:

> a **graph-based cognitive interface to code**

And your CMD layer is just:

* a transport layer
* not the real product

---
````

---

## Get Code Snippet (ambiguous query)

```cmd id="x9k2ab"
codebase-memory-mcp cli get_code_snippet "{\"project\":\"C-msys64-home-admin-github-boucaron-fsp-push\",\"qualified_name\":\"FSPSendFileList\"}"
```

---

### Output

```json id="m3p7qz"
{
  "status": "ambiguous",
  "message": "2 matches for \"FSPSendFileList\". Pick a qualified_name from suggestions below, or use search_graph(name_pattern=\"...\") to narrow results.",
  "suggestions": [
    {
      "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.android.app.src.main.java.com.chopchop3d.fspsender.protocol.FSPSendFileList",
      "name": "android/app/src/main/java/com/chopchop3d/fspsender/protocol/FSPSendFileList.kt",
      "label": "Module",
      "file_path": "android/app/src/main/java/com/chopchop3d/fspsender/protocol/FSPSendFileList.kt"
    },
    {
      "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.android.app.src.main.java.com.chopchop3d.fspsender.protocol.FSPSendFileList.FSPSendFileList",
      "name": "FSPSendFileList",
      "label": "Class",
      "file_path": "android/app/src/main/java/com/chopchop3d/fspsender/protocol/FSPSendFileList.kt"
    }
  ]
}
```

---

## Get Code Snippet (resolved module query)

```cmd id="c4n8wd"
codebase-memory-mcp cli get_code_snippet "{\"project\":\"C-msys64-home-admin-github-boucaron-fsp-push\",\"qualified_name\":\"protocol.FSPSendFileList\"}"
```

---

### Output

```json id="t7v2lm"
{
  "name": "android/app/src/main/java/com/chopchop3d/fspsender/protocol/FSPSendFileList.kt",
  "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.android.app.src.main.java.com.chopchop3d.fspsender.protocol.FSPSendFileList",
  "label": "Module",
  "file_path": "C:/msys64/home/admin/github/boucaron/fsp-push/android/app/src/main/java/com/chopchop3d/fspsender/protocol/FSPSendFileList.kt",
  "start_line": 1,
  "end_line": 18,
  "source": "package com.chopchop3d.fspsender.protocol\n\nimport android.util.Log\n\nclass FSPSendFileList {\n\n    companion object {\n        private const val TAG = \"FSPSendFileList\"\n\n        fun sendCommand(): String {\n            val command = \"FILE_LIST\\n\"\n\n            Log.d(TAG, \"Sending command: $command\")\n\n            return command\n        }\n    }\n}"
}
```

---

## Trace Path

```cmd id="v1x9re"
codebase-memory-mcp cli trace_path "{\"project\":\"C-msys64-home-admin-github-boucaron-fsp-push\",\"function_name\":\"fsp_path_join\"}"
```

---

### Output

```json id="q8n5sk"
{
  "function": "fsp_path_join",
  "direction": "both",
  "callees": [],
  "callers": [
    {
      "name": "src/fsp_file_processor.c",
      "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.src.fsp_file_processor",
      "hop": 1
    },
    {
      "name": "src/fsp_walk.c",
      "qualified_name": "C-msys64-home-admin-github-boucaron-fsp-push.src.fsp_walk",
      "hop": 1
    }
  ]
}
```

---

