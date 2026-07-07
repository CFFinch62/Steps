# Tier 1 — STEPS Sentences

Four lessons. This tier assumes a BARE graduate (Tier 2+): variables,
`if`/`else`, `while`, `input`, and ideally `sub`s already make sense. None
of that is re-taught here — every lesson below covers only what's actually
new about STEPS at the sentence-and-loop level, before Tier 2 gets into
the big structural idea (mandatory multi-file decomposition). Move fast;
this tier is vocabulary and one new data structure, not new computational
thinking yet — that starts in Tier 2.

---

## Lesson 1 — Reading STEPS: Sentences and Structure

**Objective**: Read and write basic STEPS syntax — word-based operators,
indentation-based blocks, and the `building` wrapper.

**Vocabulary**: sentence operator, indentation block.

**Teach**: Put up a minimal building next to an equivalent BARE program:

```steps
building: age_checker
    note: Ask for an age and describe the age group

    display "How old are you? "
    set age to input as number

    if age is less than 13
        display "You are a child."
    otherwise
        display "You are not a child."

    exit
```

Walk through the differences one at a time:
- `set age to input as number` replaces BARE's `age = num(input(...))` —
  the *idea* (get text, convert to a number, store it) is identical; only
  the words changed.
- `is less than` replaces `<`. STEPS spells out comparisons and several
  operators as phrases (`is greater than or equal to`, `added to` for
  string/number joining) instead of symbols.
- There is **no `end`** closing the `if`. STEPS blocks are closed by
  **indentation**, the same way Python works — the opposite of what two
  tiers of BARE just drilled in. Say this directly: *"You just spent a
  year training your hand to type `end`. Un-train it now, on purpose."*
- `otherwise` replaces `else`. Typing `else` out of habit produces a
  dedicated error telling you to use `otherwise` — this is a naming
  choice (every branch keyword shares the word "otherwise"), not a typo
  waiting to happen forever.

**Guided practice**: As a class, take a short BARE program from memory
(e.g., an even/odd checker) and translate it line-by-line into STEPS
sentences on the board.

**Independent practice**: Worksheet 1.

**Wrap-up**: Exit ticket — what closes an `if` block in STEPS, and what
happens if you type `else` instead of `otherwise`?

**Differentiation**: *Extension* — translate a longer BARE program (one
with a `while` loop) into STEPS from memory, then run it to check.
*Support* — start from the STEPS version above and make small changes
(different question, different threshold) before writing one from scratch.

---

## Lesson 2 — `otherwise if`: Multi-Way Decisions, a Third Way

**Objective**: Chain `otherwise if` to handle more than two outcomes.

**Teach**: Recall BARE's productive struggle: no `elseif` meant a
multi-branch decision was nested `if`/`else` blocks, indented one level
deeper each time, and most students eventually asked "isn't there a
better way to write this?" STEPS is that better way — but so is PLAIN's,
later, in a *different* shape again. Show the grade calculator:

```steps
if score is greater than or equal to 90
    display "Grade: A - Excellent!"
otherwise if score is greater than or equal to 80
    display "Grade: B - Good job!"
otherwise if score is greater than or equal to 70
    display "Grade: C - Satisfactory"
otherwise if score is greater than or equal to 60
    display "Grade: D - Needs improvement"
otherwise
    display "Grade: F - Please study more"
```

Point out that this is flat — every branch sits at the same indentation
level, unlike BARE's nested version, which drifted right with every added
case. Ask students who remember BARE's nested version to compare the two
side by side and say which is easier to read at five branches. Land the
point: *"You invented this yourself, or wanted to, back in BARE. STEPS
just built it in."*

**Guided practice**: As a class, convert a 2-level nested BARE `if`/`else`
(write one on the board) into a flat `otherwise if` chain.

**Independent practice**: Worksheet 2.

**Wrap-up**: Exit ticket — how many branches can an `otherwise if` chain
have, and does the indentation level change as you add more?

**Differentiation**: *Extension* — write a 5+ branch chain (e.g., a
letter-grade-with-plus-minus calculator). *Support* — a 3-branch chain
(child/teen/adult) is a complete goal for this lesson.

---

## Lesson 3 — Choosing the Right Loop

**Objective**: Pick the correct loop form — `repeat N times`, `repeat
while`, or `repeat for each` — for a given task, instead of forcing
everything through a `while`-plus-counter the way BARE required.

**Vocabulary**: counting loop, conditional loop, collection loop.

**Teach**: Put all three side by side:

```steps
repeat 5 times
    display (counter as text)
    set counter to counter + 1
```
```steps
repeat while countdown is greater than 0
    display (countdown as text)
    set countdown to countdown - 1
```
```steps
repeat for each fruit in fruits
    display "- " added to fruit
```

Ask, for each: *"Could I have written this with a `while` loop and a
counter, like BARE forced me to? Yes — so why wouldn't I?"* The answer is
the actual lesson: `repeat N times` says "exactly this many times" without
a counter variable to manage or get off-by-one on; `repeat while` says
"until this condition changes," which is what `while` was always for;
`repeat for each` says "once per item," and needs no index at all — no
`i = 0` to declare, no `i < len(list)` to get wrong. **Choosing the loop
that matches the task is itself the skill** — a BARE program had one tool
for every job; STEPS gives three, and picking wrong (say, using `for each`
when you need to also change every item's value) is a real design
decision, not a syntax error.

**Guided practice**: As a class, look at 3 short task descriptions
("print the numbers 1 to 10," "keep asking until the user enters a
password," "greet every name in a list") and decide which loop form fits
each — before writing any code.

**Independent practice**: Worksheet 3.

**Wrap-up**: Exit ticket — which loop form needs no counter variable at
all, and why?

**Differentiation**: *Extension* — a nested loop (a multiplication table
using two `repeat N times` loops, one inside the other). *Support* — match
each of the three loop forms to a task description before attempting to
write any of them from scratch.

---

## Lesson 4 — Tables: Looking Things Up by Name

**Objective**: Create a table, access and update values by key, and decide
when a table is the better structure over a list.

**Vocabulary**: table, key, value.

**Teach**:

```steps
set person to ["name": "Alice", "age": 25, "city": "Boston"]

display "Name: " added to person["name"]
display "Age: " added to (person["age"] as text)

set person["age"] to 26
set person["job"] to "Engineer"
```

This is a genuinely new data structure — BARE only had lists, where you
find something by *position* (`colors[0]` is "whatever's first"). A table
finds something by *name* (`person["age"]` is "whatever's stored under
the word age," no matter where it sits). Ask: *"If I wanted to store a
list of 5 students' test scores, would a list or a table make more
sense? What if I wanted to store one student's name, age, and grade all
together?"* Land the distinction: a list is for a sequence of similar
things; a table is for one thing's several named properties, or for
lookup by a meaningful key. Show a nested table (`grades` inside `student`
inside a table) as a preview of "data that has structure to it," which
comes back properly in later languages as records.

**Guided practice**: As a class, build a `book` table (title, author,
year, pages) and print each field by name.

**Independent practice**: Worksheet 4.

**Wrap-up**: Exit ticket — would you use a list or a table to store: (a)
every student's name in a class, (b) one student's name, age, and
homeroom? Why?

**Differentiation**: *Extension* — a table of tables (e.g., three
students, each a table of name/grade), looped over with `repeat for each`.
*Support* — one flat table with 3-4 fields, read and updated, is a
complete goal for this lesson.
