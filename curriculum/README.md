# Learn to Program with STEPS — Bridging from BARE

This is a short, two-tier curriculum for students who have finished the
**BARE** curriculum (all three tiers, or at minimum Tier 2) and are moving
on to **STEPS**. It is deliberately not a from-scratch curriculum the way
BARE's is — STEPS already ships a complete 14-lesson tutorial
([docs/TUTORIAL.md](../docs/TUTORIAL.md), with runnable code in
[projects/tutorial/](../projects/tutorial/)) that teaches the language well
on its own. What this folder adds is the piece that's missing: the
**bridge** — what's actually new here versus BARE, why it's worth learning,
where a BARE graduate will get tripped up, and how the existing tutorial
lessons map onto that story.

**Start here if you're a teacher**: read
[teachers-guide.md](teachers-guide.md) in full. It's the "why" and the
"watch out for" that sits on top of the existing tutorial's "how."

## Why STEPS comes after BARE

BARE taught real functions, real scope, and real data — on purpose, in a
language small enough to hold in your head. STEPS keeps every one of those
ideas and adds the thing BARE deliberately left out: **enforced program
architecture**. In BARE, a `sub` is just a block of code with a name. In
STEPS, every reusable piece of logic is a **step** that must live in its
own file, inside a **floor**, inside a **building** — a real, if small,
taste of what it means to organize a program instead of just writing one.
Alongside that, STEPS reads more like English sentences than BARE does,
adds a second data structure (tables, i.e. dictionaries), a second kind of
`if`-chaining (`otherwise if`), and — for the first time in the suite —
lets a program **recover from an error instead of crashing**.

## The two tiers

| Tier | Comes after | Folder | New big idea |
|---|---|---|---|
| **1 — STEPS Sentences** | BARE Tier 2+ | [tier1-sentences/](tier1-sentences/) | Sentence-style operators, `otherwise if`, three loop forms, tables — the same computational thinking BARE taught, said a new way, plus one new data structure |
| **2 — STEPS Architecture** | Tier 1 | [tier2-architecture/](tier2-architecture/) | Buildings/floors/steps/risers and `attempt`/`unsuccessful` — programs as *structured, multi-file things*, and errors as *recoverable*, not fatal |

Each tier folder has the same three documents as BARE's tiers:
**`lessons.md`** (teacher-facing lesson plans), **`worksheets.md`**
(student-facing handouts), and **`assessment.md`** (checkpoint quizzes,
plus a capstone rubric in Tier 2). These are intentionally shorter than
BARE's — every lesson here covers only what's new about STEPS, not a
full re-teaching of programming fundamentals a BARE graduate already has.

Because a STEPS-bound student has already done variables, conditionals,
loops, functions, and lists in BARE, Tier 1 moves fast — it's mostly
vocabulary and syntax translation, not new concepts. Tier 2 is where the
real new material lives and deserves the bulk of class time.

## How this relates to the rest of the STEPS project

- [docs/TUTORIAL.md](../docs/TUTORIAL.md) is the primary hands-on material
  for both tiers — the teachers-guide maps its 14 lessons onto the two
  tiers above. Use it directly; this curriculum doesn't duplicate it.
- [docs/LANGUAGE-REFERENCE.md](../docs/LANGUAGE-REFERENCE.md) and
  [docs/STDLIB.md](../docs/STDLIB.md) are the reference manuals — point
  students there the same way BARE points students at its own spec.
- [projects/steps_euler/](../projects/steps_euler/) (ten Project Euler
  solutions using helper steps) is good Tier 2 extension/capstone
  material — the same role BARE's Tier 3 examples play.
- [projects/steps_instruments/](../projects/steps_instruments/) (a real
  NMEA-0183 marine-instrument dashboard reading live serial data) is a
  good "look what's actually possible" motivator for advanced or older
  students finishing Tier 2 — it's well beyond anything BARE could build,
  which is the point.
- The STEPS GUI IDE has a built-in debugger (breakpoints, call stack,
  variable inspector) and a `steps diagram` command that draws a picture
  of a building's floor/step structure — genuinely useful the moment
  Tier 2 introduces multi-file programs, since students can *see* the
  architecture they're building instead of just imagining it.
