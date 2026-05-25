# 📘 PR, Technical Review & Technical Reference Guide

This document defines how we conduct technical reviews and maintain shared engineering standards.

**Goal**: Improve clarity, reduce unnecessary friction, accelerate delivery, and ensure consistent, high-quality technical decision-making.

---

## 1. What is a Technical Review?

A **Technical Review** ensures the quality, correctness, and safety of changes to the system.

Reviews focus on:

* **Correctness**
* **Security**
* **Robustness & reliability**
* **Maintainability & long-term health**

Reviews treat the PR as a **complete system update**, including frontend, backend, database, APIs/contracts, infrastructure, and observability changes where relevant.

Where possible, rely on information already provided in the PR rather than requesting fragmented extra artifacts.

---

## 2. Review Principles

### 2.1 Shared technical foundation

Feedback should preferably be grounded in:

* The **Technical Reference Guide**, or
* A clearly explained technical risk (impact on behavior, performance, scalability, security, data integrity, or operational cost).

This promotes consistency and makes feedback more actionable.

### 2.2 When no guideline exists

* It is valid to raise new feedback.
* Treat it as **non-blocking** unless a clear technical risk exists.
* Consider proposing it as an addition to the Technical Reference Guide.

### 2.3 Collaborative & constructive culture

We assume positive intent. Reviews are **collaborative**, not adversarial.
Reviewers help strengthen the change; authors remain responsible for the final implementation. Clear, kind, and actionable comments are expected from everyone.

---

## 3. Decision Responsibility

* The **designated maintainer / tech lead** has final authority on merging.
* Blocking comments must reference either:
  * A rule from the Technical Reference Guide, **or**
  * A specific, explainable technical risk.
* Non-blocking feedback is welcome and valuable but does **not** prevent merging.

---

## 4. Technical Reference Guide

The Technical Reference Guide is our living, team-owned collection of agreed engineering standards and best practices. It exists to:

* Align decisions across the team
* Reduce ambiguity and repeated discussions
* Capture institutional knowledge over time

**Each entry should include**:

* The rule
* Rationale (why it matters)
* Example(s) when helpful

**Example**:

```markdown
## Spring Boot - Controllers

**Prefer @RequestParam over @PathVariable** for filtering and search operations when possible.

**Rationale**:  
@PathVariable reduces flexibility when supporting multiple filtering combinations or optional parameters.

**Example**:
- Good: `/users?status=ACTIVE&role=ADMIN`
- Avoid (unless truly needed): `/users/ACTIVE/ADMIN`
```

### Nature of the Guide

* Team-maintained and continuously evolving
* Not exhaustive — it covers common cases
* Deviations are allowed when intentionally justified

---

## 5. Process for Evolving the Guide

1. During reviews, prefix guide suggestions with **“Guide Proposal:”**
2. Create (or update) an entry with rule + rationale + example
3. Open a small PR against the guide (or add it directly if trivial)
4. Team discusses and reaches consensus (async or in tech sync)

This keeps the guide current without creating bureaucracy.

---

## 6. PR Expectations

Every PR must clearly describe:

* **What** changed
* **Why** it changed (motivation and trade-offs)
* **System impact** (frontend, backend, database, APIs/contracts, observability, etc.)
* Any intentional deviations from the Technical Reference Guide

A good PR description answers: “Why is this the right change now, and why is this approach better than the alternatives?”

---

## 7. Blocking vs Non-Blocking Feedback

### Blocking Issues (must be resolved before merge)

* Correctness / functional bugs or regressions
* Security vulnerabilities
* Data integrity or consistency risks
* Broken or incompatible APIs/contracts
* Unsafe or missing database migrations / schema changes
* Significant performance or scalability regressions

### Non-Blocking Feedback (valuable but does not block)

* Naming, style, or formatting suggestions (unless automated)
* Readability / cosmetic improvements
* Alternative implementations without clear risk
* Suggestions for future improvements or refactoring
* Preferences not covered by the Reference Guide

---

## 8. PR Review Checklist

### 1. Understanding the Change

* Do I fully understand the system impact?
* Is the “what + why” clearly described?

### 2. Correctness

* Any regressions or broken functionality?
* Are APIs/contracts consistent and backward-compatible when needed?

### 3. Data & Persistence

* Are migrations safe, versioned, and rollback-capable if necessary?
* Any data migration or integrity risks?

### 4. Architecture & Design

* Does it align with existing architecture and the Reference Guide?
* Is the solution overly complex?

### 5. Security & Compliance

* Any new attack surface or sensitive data handling?

### 6. Performance & Scalability

* Any obvious concerns under expected load?

### 7. Observability

* Are changes sufficiently logged, monitored, and alertable?

### 8. Feedback Quality

* Are my comments clear, specific, and actionable?
* Did I avoid duplicating the same point multiple times?

---

## 9. Automation & Enforcement

Many style, formatting, and basic consistency rules should be **automatically enforced** (linters, formatters, static analysis, contract tests, etc.).

Reviews should focus on high-value judgment calls, not things machines can check.

---

## 10. Merge Rule (Summary)

A PR may only be **blocked** for:

* Correctness issues
* Security risks
* Data integrity problems
* Broken contracts
* Unsafe/missing migrations

All other feedback is non-blocking or can be addressed in follow-up work.

---

**Final note**: This process exists to ship high-quality software faster, not to slow teams down with ceremony. When in doubt, favor pragmatism, clear communication, and continuous improvement of our shared standards.