# Tier 2 — STEPS Architecture

Five lessons. This is where STEPS earns its place in the suite: **a
program's structure stops being a matter of style and becomes something
the language enforces.** A BARE `sub` could live anywhere in one file; a
STEPS **step** cannot — it must live in its own file, inside a **floor**,
inside a **building**, or the program simply won't run. The other big new
idea lands in Lesson 4: for the first time in the suite, an error can be
**caught and recovered from** instead of stopping the program cold.

Students should have finished Tier 1 (sentence syntax, `otherwise if`,
the three loop forms, tables) before starting here.

---

## Lesson 1 — Your First Step: Decomposition Becomes Mandatory

**Objective**: Create a step in its own file, give it a floor, and call it
from a building.

**Vocabulary**: building, floor, step, `expects`, `returns`.

**Teach**: Show the real folder layout on screen before any code:

```
lesson_08_first_step/
    lesson_08_first_step.building
    helpers/
        greet.step
        get_lucky_number.step
        get_greeting.step
```

The building file declares what steps exist and where:

```steps
building: lesson_08_first_step
    floors:
        floor: helpers
            step: greet
            step: get_lucky_number
            step: get_greeting

    call greet

    call get_lucky_number storing result in lucky
    display "Your lucky number is: " added to (lucky as text)

    set name to input as text
    call get_greeting with name storing result in message
    display message

    exit
```

Each step is its own file:

```steps
step: greet
    belongs to: helpers
    expects: nothing
    returns: nothing

    do:
        display "Hello from the greet step!"
```

```steps
step: get_greeting
    belongs to: helpers
    expects: name
    returns: message

    do:
        set message to "Welcome " added to name added to "!"
        return message
```

Say the reframe directly: *"In BARE, a `sub` was a block of code with a
name, and you could put ten of them in one file with nobody stopping you.
Here, that's not allowed — `expects`/`returns` in the header tells you
exactly what a step needs and gives back before you read a single line of
its body, and it has to live somewhere specific. This is what 'read the
signature, not the implementation' means in real software, and STEPS
makes you do it whether you meant to or not."* Point out `expects:
nothing` / `returns: nothing` as the honest, explicit version of a BARE
`sub` that just prints — nothing is hidden or implied.

**Guided practice**: As a class, take a BARE `sub` from memory (e.g., the
Fahrenheit/Celsius converter) and rebuild it as a STEPS step: a `.step`
file with `belongs to`, `expects`, `returns`, and `do:`, called from a
building.

**Independent practice**: Worksheet 1.

**Wrap-up**: Exit ticket — what two things does a step's header tell you
before you've read its `do:` section at all?

**Differentiation**: *Extension* — a step with two parameters and a
returned value, called twice with different arguments. *Support* — one
step with `expects: nothing` / `returns: nothing`, called once, is a
complete goal for this lesson.

---

## Lesson 2 — Floors: Organizing a Multi-File Building

**Objective**: Organize several related steps into a floor, and split a
program's steps across more than one floor.

**Teach**: Extend Lesson 1's idea to multiple floors:

```steps
building: calculator
    floors:
        floor: math
            step: add_numbers
            step: subtract_numbers
            step: multiply_numbers
            step: divide_numbers
        floor: string
            step: greet_person

    call greet_person with "Alice"

    call add_numbers with 10, 5 storing result in sum
    display "10 + 5 = " added to (sum as text)

    exit
```

Each floor is its own folder (`math/add_numbers.step`,
`string/greet_person.step`) and each step declares `belongs to: math` or
`belongs to: string` to match. Ask: *"Why put `add_numbers` and
`greet_person` on different floors instead of all together?"* — the
answer is the actual design skill here: a floor is a *category*, and
deciding what belongs on which floor is planning a program's shape before
writing its logic, the same way an architect groups rooms by function
before drawing walls. A structural mismatch — a step's `belongs to` not
matching the folder it's actually in, or a `.building` file listing a step
that doesn't exist — is a clear, specific error, not a silent bug.

**Guided practice**: As a class, sketch (on paper, before touching the
keyboard) which floors a "quiz game" program would need and which steps
go on each.

**Independent practice**: Worksheet 2.

**Wrap-up**: Exit ticket — what has to match between a step's `belongs
to:` line and where its file actually lives?

**Differentiation**: *Extension* — a 3-floor building (e.g., `math`,
`display`, `validation`). *Support* — a 2-floor building with one step
each is a complete goal.

---

## Lesson 3 — Risers: Private Helpers and Encapsulation

**Objective**: Use a riser for logic that only one step needs, and explain
why a riser can't be called from anywhere else.

**Vocabulary**: riser, encapsulation.

**Teach**:

```steps
step: calculate_tip
    belongs to: math
    expects: amount, percent
    returns: tip

    riser: calculate_percentage
        expects: value, pct
        returns: result

        do:
            set result to value * (pct / 100)
            return result

    do:
        call calculate_percentage with amount, percent storing result in tip
        return tip
```

Ask students to try calling `calculate_percentage` directly from the
building or from a different step — it fails with a `RISER_NOT_FOUND`
error suggesting the step be moved or promoted. Land the idea: *"A riser
is a step's private notebook. Other steps aren't allowed to read it, on
purpose — if the logic turns out to be useful elsewhere, that's a signal
to promote it to a real step, not a bug to route around."* This is the
same instinct as BARE's strict `sub` scope rule (Tier 2 there), one level
higher up: now it's not just variables that are hidden, it's whole pieces
of logic.

**Guided practice**: As a class, find a step from Lesson 1 or 2 with a
calculation that's only used internally, and factor it out into a riser.

**Independent practice**: Worksheet 3.

**Wrap-up**: Exit ticket — what error do you get calling a riser from
outside its step, and what is that error actually telling you to do?

**Differentiation**: *Extension* — a step with two risers, one calling the
other. *Support* — take the `calculate_tip` example above, type it
exactly, and verify the `RISER_NOT_FOUND` error by trying to break it on
purpose.

---

## Lesson 4 — When Things Go Wrong: `attempt` / `unsuccessful` / `then continue`

**Objective**: Use `attempt`/`if unsuccessful`/`then continue` to keep a
program running after a recoverable error.

**Vocabulary**: recoverable error, `problem_message`.

**Teach**: Open with the philosophical pivot directly: *"BARE taught you,
on purpose, that an error stops the program cold — no try/catch, because
the lesson was prevention, not handling. That's still true of a bug. But
some 'errors' aren't bugs — they're a user typing letters where a number
belongs, or a file that isn't there yet. STEPS is where you learn the
difference and get a tool for the second kind."*

```steps
attempt:
    set num to input as number
if unsuccessful:
    display "Error: " added to problem_message
then continue:
    display "Done processing"
```

Walk through each part: `attempt:` wraps code that might fail; `if
unsuccessful:` runs only if it did, and `problem_message` holds a
plain-English description of what went wrong; `then continue:` always
runs, whether or not there was a problem — useful for cleanup that has to
happen either way. Contrast directly with a bug versus a recoverable
error: a `RISER_NOT_FOUND` error (Lesson 3) means the *program* is wrong
and should be fixed, not wrapped in `attempt`. Bad user input is different
— the program is fine, the input wasn't.

**Guided practice**: As a class, wrap a number-conversion `input` in
`attempt`, deliberately trigger the failure by typing letters, and read
`problem_message` together.

**Independent practice**: Worksheet 4.

**Wrap-up**: Exit ticket — give one example of something worth wrapping in
`attempt`, and one example of something that should just be allowed to
crash (a real bug).

**Differentiation**: *Extension* — a validation loop (Tier 1 territory)
combined with `attempt`, retrying until input both parses *and* passes a
range check. *Support* — the exact number-conversion example above,
triggered and read once, is a complete goal.

---

## Lesson 5 — Capstone: A Complete Multi-Floor Building

**Objective**: Design and build a multi-floor STEPS program using steps,
at least one riser, a table, and `attempt`/`unsuccessful` error handling.

**Teach**: Present capstone options:
- **Quiz Game** — a `questions` floor (steps to ask and score questions,
  a table per question with prompt/answer), a `scoring` floor, `attempt`
  around each answer input.
- **Price Calculator** — a `math` floor (with at least one riser for an
  internal calculation, mirroring `calculate_tip`), a `display` floor,
  `attempt` around every numeric input.
- **A project of the student's own design**, approved by the teacher,
  using at least two floors, one riser, one table, and one `attempt`
  block.

Require a written plan first: what floors, what steps on each, what each
step's `expects`/`returns` will be, and where `attempt` is needed — before
any code. Model showing this plan as a small diagram (boxes for floors,
arrows for which step calls which) — the STEPS IDE's `steps diagram`
command can generate this automatically from a finished building, which is
worth showing as "here's what your plan should end up matching."

**Guided practice**: Peer-review plans in pairs — a partner should be able
to point at the plan and say which floor handles the error input.

**Independent practice**: Build the capstone (spread across as many
sessions as needed).

**Wrap-up**: Showcase — each student runs their program and answers: what
does it do, which floor are you proudest of, and where did you use
`attempt` and why there specifically?

**Differentiation**: *Extension* — add a second riser, or a nested table
(a table whose values are themselves tables). *Support* — the Quiz Game
with a provided 2-floor skeleton (steps already named, `.step` files
started with just `do:` left blank) is the lowest-friction path.
