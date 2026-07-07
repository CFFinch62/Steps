# Tier 1 Assessment

Two checkpoints — this tier is short, so there's no capstone here; the
first real project lands in Tier 2 once decomposition is on the table.

---

## Checkpoint 1 — Sentences and Decisions (after Lesson 2)

1. What closes a block (like an `if`) in STEPS?
2. What error do you get if you type `else` instead of `otherwise`, and
   why does STEPS do this on purpose?
3. What will this print?
   ```steps
   set n to 7
   if n is greater than 10
       display "big"
   otherwise if n is greater than 5
       display "medium"
   otherwise
       display "small"
   ```
4. Rewrite this nested BARE logic as a flat STEPS `otherwise if` chain (you
   don't need to run it, just write the STEPS version):
   ```
   if x < 0
       print "negative"
   else
       if x == 0
           print "zero"
       else
           print "positive"
       end
   end
   ```

**Answer key**: 1. Indentation — STEPS has no `end` keyword for closing
control blocks  2. STEPS rejects `else` with an error pointing to
`otherwise`; it's a naming-consistency choice, since `if`/`otherwise
if`/`otherwise` all share the word "otherwise"  3. `medium`  4.
```steps
if x is less than 0
    display "negative"
otherwise if x is equal to 0
    display "zero"
otherwise
    display "positive"
```

---

## Checkpoint 2 — Loops and Tables (after Lesson 4)

1. Match each task to the loop form that fits best: (a) print "hello" 3
   times, (b) print every item in a list, (c) keep asking for input until
   it's valid.
2. What will this print?
   ```steps
   set colors to ["red", "green", "blue"]
   repeat for each color in colors
       display color
   ```
3. What will this print?
   ```steps
   set book to ["title": "Dune", "year": 1965]
   display book["title"]
   set book["year"] to 2021
   display (book["year"] as text)
   ```
4. You need to store one student's name, age, and grade together. Would
   you use a list or a table? Why?
5. You need to store every student's name in a class of 30. Would you use
   a list or a table? Why?

**Answer key**: 1. (a) `repeat N times`, (b) `repeat for each`, (c)
`repeat while`  2. `red` then `green` then `blue`, each on its own line
3. `Dune` then `2021`  4. A table — the three pieces of data are different
*kinds* of information about one thing, best looked up by name (`name`,
`age`, `grade`) rather than position  5. A list — all 30 items are the
same kind of thing (a name) in a simple sequence, with no meaningful key
other than "which one."
