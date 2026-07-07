# Tier 2 Student Worksheets

---

## Worksheet 1 — Your First Step

1. Create a building called `greeting_demo` with one floor (`helpers`)
   containing one step, `greet`, that expects nothing, returns nothing,
   and displays a message. Call it from the building.
2. Add a second step, `add_numbers`, that expects two numbers and returns
   their sum. Call it with two different pairs of numbers and display
   both results.
3. **Predict, then run**: what happens if your `.building` file lists a
   step under `floors:` that doesn't have a matching `.step` file?

---

## Worksheet 2 — Floors

1. Type and run a building with two floors — `math` (with `add_numbers`,
   `subtract_numbers`) and `string` (with `greet_person`) — calling at
   least one step from each floor.
2. Plan (on paper first) the floors and steps you'd need for a "quiz
   game" program. Write down each floor's name and which steps belong to
   it, before writing any code.
3. **Predict, then run**: what error do you get if a step's `belongs to:`
   line names a floor that doesn't match the folder it's actually saved
   in?

---

## Worksheet 3 — Risers

1. Type and run:
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
2. **Predict, then run**: try calling `calculate_percentage` directly from
   your building (not through `calculate_tip`). What error do you get?
3. Take a step you wrote in Worksheet 1 or 2 and factor part of its logic
   out into a riser.

---

## Worksheet 4 — Error Handling

1. Type and run, entering both a number and letters when prompted:
   ```steps
   attempt:
       set num to input as number
   if unsuccessful:
       display "Error: " added to problem_message
   then continue:
       display "Done processing"
   ```
2. Write a program that asks for two numbers and divides them, using
   `attempt` to catch a division problem and display a friendly message
   instead of crashing.
3. For each situation below, say whether it belongs inside an `attempt`
   block or should just be allowed to crash: (a) converting user input to
   a number, (b) calling a riser from outside its step, (c) reading a file
   that might not exist, (d) a step whose `expects` doesn't match how it's
   called.

---

## Worksheet 5 — Capstone Plan

Write a short plan (turned in, not typed into the IDE) for your capstone:
1. Which project are you building (Quiz Game, Price Calculator, or your
   own idea)?
2. List every floor you'll need and which steps belong to each.
3. For each step, write its `expects` and `returns`.
4. Where will you use a riser, and why does that logic belong there and
   not in its own step?
5. Where will you use `attempt`/`unsuccessful`, and what could go wrong
   there that makes it worth catching?
