# STEPS Curriculum — Teacher's Guide

This assumes your students have finished BARE (ideally through Tier 2:
`sub`s, scope, lists) and covers what changes now, why it's worth the
friction, and where a BARE graduate specifically trips up. Read this
alongside [docs/TUTORIAL.md](../docs/TUTORIAL.md), which supplies the
actual lesson-by-lesson exercises.

## 1. Why STEPS, and why now

STEPS' own design philosophy (from its README) is "**visible structure,
mandatory decomposition**" — every program's architecture is explicit and
enforced, not left to a student's discipline. That's the single idea BARE
couldn't teach: BARE's `sub`s live wherever a student puts them in one
file, so a BARE program can grow into an unstructured pile of code without
ever throwing an error. STEPS makes that impossible. A **step** must live
in its own file; a **floor** is a folder of related steps; a **building**
is the whole program. Say this to students directly: *"BARE let you get
away with a messy program. STEPS won't — and that's not a punishment, it's
training for every real codebase you'll ever touch, where 'just put it all
in one file' stops working long before the program does."*

Two smaller but real reasons to move now, not later:

- **STEPS reads more like English**, using multi-word phrases (`is greater
  than`, `added to`, `otherwise if`) instead of BARE's math-class symbols.
  For students who found BARE's terseness comfortable, this is a genuine
  adjustment — but it pays off the moment they read someone else's code
  and can pronounce it in their head like a sentence.
- **STEPS introduces recoverable errors.** BARE was explicit that "an
  error stops the program, full stop" is a *feature*, not a gap — the
  lesson was prevention over handling. STEPS is where that lesson gets its
  second half: `attempt` / `if unsuccessful` / `then continue` teaches that
  some errors (bad input, a missing file) are expected, ordinary, and
  recoverable, while a program bug still is not. Frame it as: *"BARE
  taught you to write code that avoids the mistake. STEPS teaches you what
  to do when the mistake is the user's, not yours."*

## 2. Tier map against the existing tutorial

| Tier | Tutorial lessons | Core content |
|---|---|---|
| **1 — STEPS Sentences** | 1–7 | Buildings/exit, variables & 5 types, `input`, `if`/`otherwise if`/`otherwise`, three loop forms (`repeat N times`, `repeat for each`, `repeat while`), lists, tables |
| **2 — STEPS Architecture** | 8–14 (+ debugger/diagram lessons 15–16 as enrichment) | First step, `expects`/`returns` + `call ... with ... storing result in`, floors, a full multi-floor building, `attempt`/`unsuccessful`, files/CSV, randomness/games |

A capstone at the end of Tier 2 should be a small multi-floor building with
at least one step that takes parameters, one table, and one `attempt`
block — [projects/steps_euler/](../projects/steps_euler/) or
[projects/steps_instruments/](../projects/steps_instruments/) are good
models to show students before they design their own.

## 3. STEPS-specific misconceptions and gotchas (know these before students find them)

| What trips students up | What's actually happening | Where it comes up |
|---|---|---|
| Typing `else` | STEPS rejects it outright with a dedicated error pointing them to `otherwise` — this isn't a bug, it's a naming-consistency choice (`if`/`otherwise if`/`otherwise` all share a word). Every BARE graduate types `else` at least once. | Tier 1, first conditional lesson |
| Typing `end` to close a block | STEPS blocks are closed by **indentation**, not a keyword — the opposite of what BARE just spent two tiers reinforcing. `end` still exists in STEPS, but only for closing a `block:` comment. | Tier 1, first lesson with any block |
| Reaching for `+`, `<`, `>=` | Comparisons and some operators are words (`is greater than`, `is greater than or equal to`, `added to`) rather than symbols. This is the single biggest "it looks different but means the same thing" adjustment. | Tier 1, first math/comparison lesson |
| Putting a helper `sub`-equivalent anywhere convenient | A **step** must be its own file inside a floor folder; STEPS raises a structural error (missing `.building`/`.step` file, `belongs to` folder mismatch) rather than silently allowing a monolithic file. This is the load-bearing new idea — don't let students route around it. | Tier 2, first step lesson — give it real time |
| Trying to call a **riser** from outside its parent step | Risers are deliberately private helpers nested inside a single step; calling one from elsewhere raises `RISER_NOT_FOUND` with a message suggesting you promote it to a real step. This is encapsulation, taught by the error message itself. | Tier 2, once risers come up |
| Reaching for `break`/`continue` in a loop | STEPS has neither, on purpose — same minimalist instinct as BARE. Loop exit is structured through the loop's own condition instead. Students who ask "how do I just stop the loop early" should be pushed back to "what condition would make the loop stop naturally?" | Tier 1, loop lessons |
| An infinite `while`-style loop just runs forever | STEPS has a built-in **iteration limit** (10,000,000 by default) that stops runaway loops with a friendly error instead of a hang — a training wheel worth naming explicitly, the same way BARE's Stop button was. | Tier 1, `repeat while` lesson |
| Assuming recursion works exactly like BARE's | STEPS caps recursion at depth 100 with a full call-stack trace in the error. This is more visible (and more restrictive) than most students expect after BARE. | Tier 2/3 extension, if you cover recursion again here |

## 4. What to reuse from BARE's teaching habits

Everything in BARE's teachers-guide about **reading the error message out
loud**, **productive struggle**, and **pair programming** still applies —
STEPS' errors are, if anything, even more didactic than BARE's (they
include "Did you mean...?" fuzzy-match suggestions for misspelled step
names or table keys). Keep the "read it, don't guess" habit going; don't
let a more helpful error message become an excuse to stop reading them
carefully.

## 5. Differentiation

- **Fast finishers**: point them at
  [projects/steps_instruments/](../projects/steps_instruments/) — a real
  multi-file program reading live serial data and rendering a dashboard.
  It's far beyond what they're building, and that's the point: "here's
  what this structure buys you at real scale."
- **Struggling students**: the BARE-era move still works — shrink the
  program, not the concept. If the building/floor/step structure itself is
  the confusion, have them build a one-floor, one-step program first and
  only add a second floor once the first structure is solid.

## 6. Bridge forward

Close Tier 2 by naming what's coming: PLAIN keeps steps' idea of naming
what a function needs and returns, but relaxes the "one function per file"
rule — students get to *choose* how to organize a file instead of being
forced to. Frame that as a reward for having learned the discipline the
hard way first, not as STEPS being "replaced."
