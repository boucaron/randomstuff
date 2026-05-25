# 📘 PR Review - Crunch/Rush Mode

**Goal**: Ship fast. Zero noise unless it actually blocks.

---

### 1. Core Rule

**Only block for real problems.** Everything else is non-blocking.

### 2. What Blocks a Merge

Block only if the change has:

- Correctness / functional bugs or regressions
- Security issues
- Data integrity risks
- Broken APIs or contracts
- Unsafe or missing database migrations

That’s it.

### 3. Non-Blocking (Do NOT block for these)

- Style, naming, formatting
- Readability suggestions
- “I would have done it differently”
- Alternative implementations with no clear risk
- Future improvements / nice-to-haves
- Anything not covered above

### 4. Technical Reference Guide

- If it violates the Guide → comment it.
- If it’s a clear violation with risk → block.
- Otherwise → non-blocking (or propose updating the Guide).

### 5. Decision Making

- Tech lead / maintainer makes the final call.
- Blocking comments must be short and clear (risk or Guide reference).
- Author can merge once blockers are resolved.

### 6. PR Minimums (in a rush)

- Clear title + “What & Why”
- Mention impacted areas (BE, FE, DB, API)
- Migration + rollback plan if relevant

---

**Crunch Mode Mindset**:

- Default = **Merge**.
- Only stop the line for actual danger.
- Non-blocking comments are still welcome but must not hold up merging.
- Speed > Perfection.