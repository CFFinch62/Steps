# Tier 2 Assessment

Two checkpoints plus the capstone rubric.

---

## Checkpoint 1 — Steps, Floors, and Risers (after Lesson 3)

1. What three things must a step have that a BARE `sub` never required?
2. Why won't this building run? What's wrong?
   ```steps
   building: broken_demo
       floors:
           floor: helpers
               step: greet

       call greet
       exit
   ```
   (Assume no `.step` file for `greet` exists anywhere in the project.)
3. What happens if you try to call a riser from a step other than the one
   that defines it?
4. Why can't a riser just be called from anywhere, the way a step can?

**Answer key**: 1. It must live in its own file, declare which floor it
`belongs to`, and declare what it `expects` and `returns`  2. The
building lists `greet` under the `helpers` floor, but there's no matching
`greet.step` file — a structural error, not a runtime bug  3. A
`RISER_NOT_FOUND` error, suggesting the logic be moved into the calling
step or promoted to a real step  4. A riser is intentionally private to
its parent step — this is encapsulation: hiding a helper detail that
nothing else should depend on.

---

## Checkpoint 2 — Error Handling (after Lesson 4)

1. What does `problem_message` contain, and when does it get set?
2. What's the difference between wrapping something in `attempt` and just
   letting the program crash?
3. What will this program do if the user types `"abc"` when asked for a
   number?
   ```steps
   attempt:
       set n to input as number
   if unsuccessful:
       display "That wasn't a number."
   then continue:
       display "Moving on."
   ```
4. Give one example of a problem that belongs inside `attempt`, and one
   that's a real bug and shouldn't be caught at all.
5. True or False: `then continue:` only runs if there was no error.

**Answer key**: 1. A plain-English description of what went wrong, set
automatically when the code inside `attempt` fails  2. `attempt` lets the
program keep running after the failure with your own handling code; a
crash stops the program immediately with no recovery  3. It displays
"That wasn't a number." followed by "Moving on." — the program doesn't
crash  4. Belongs in `attempt`: converting user input to a number, or
opening a file that might not exist. A real bug: calling a riser from
outside its step, or a step called with the wrong number of arguments —
these mean the *program* is wrong, not the input  5. **False** —
`then continue:` always runs, whether or not the `attempt` block failed.

---

## Capstone Rubric

Score each category 0-3.

| Category | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Correctness** | Doesn't run, or a core feature is missing entirely | Runs but a core feature is broken in common cases | Works correctly for the project's core requirements | Also handles at least one edge case (bad input, an empty table) cleanly via `attempt` |
| **Architecture** | All logic crammed into one step, or floors that don't reflect any real grouping | At least two floors exist but the grouping is arbitrary | Floors reflect a sensible grouping of related steps; each step's `expects`/`returns` matches what it actually does | Also uses at least one riser correctly, for logic that genuinely belongs to only one step |
| **Data structures** | No table used where one would clearly help | A table exists but is used superficially | At least one table used meaningfully (structured data looked up by key, not just a list in disguise) | Also uses a table of tables, or a table alongside a list, where it genuinely fits the data |
| **Error handling & explanation** | No `attempt` used anywhere risky, or can't explain the program | At least one `attempt` block exists, in a plausible place | `attempt`/`unsuccessful` used where user input could realistically fail, and the student can explain why there specifically | Can also clearly distinguish, out loud, an error worth catching from a real bug worth letting crash |

A student scoring 2+ across all four categories has met the tier's goal
and is ready to move to PLAIN.
