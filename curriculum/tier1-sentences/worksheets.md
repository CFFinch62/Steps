# Tier 1 Student Worksheets

---

## Worksheet 1 — Reading STEPS

1. Type and run:
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
2. **Predict, then run**: what happens if you change `otherwise` on line 9
   to `else`?
3. Translate this BARE program into STEPS:
   ```
   n = num(input("Enter a number: "))
   if n < 0
       print "negative"
   else
       print "not negative"
   end
   ```

---

## Worksheet 2 — `otherwise if`

1. Type and run:
   ```steps
   if score is greater than or equal to 90
       display "Grade: A - Excellent!"
   otherwise if score is greater than or equal to 80
       display "Grade: B - Good job!"
   otherwise if score is greater than or equal to 70
       display "Grade: C - Satisfactory"
   otherwise
       display "Grade: F - Please study more"
   ```
   Try it with `score` set to 95, 82, 71, and 40.
2. Write a 3-branch `otherwise if` chain that prints "child," "teenager,"
   or "adult" based on an age entered with `input`.
3. This BARE program is 3 levels of nested `if`/`else`. Rewrite it as a
   flat STEPS `otherwise if` chain:
   ```
   if n < 0
       print "negative"
   else
       if n == 0
           print "zero"
       else
           print "positive"
       end
   end
   ```

---

## Worksheet 3 — Choosing the Right Loop

For each task below, write which loop form you'd use (`repeat N times`,
`repeat while`, or `repeat for each`) **before** writing any code, then
write the STEPS code.

1. Print the numbers 1 through 10.
2. Keep asking the user to guess a number until they guess correctly.
3. Print every name in a list called `students`.
4. **Predict, then run**: what does this print, and how many times does
   the loop body run?
   ```steps
   set fruits to ["apple", "banana", "cherry"]
   repeat for each fruit in fruits
       display "- " added to fruit
   ```

---

## Worksheet 4 — Tables

1. Type and run:
   ```steps
   set person to ["name": "Alice", "age": 25, "city": "Boston"]
   display "Name: " added to person["name"]
   display "Age: " added to (person["age"] as text)
   set person["age"] to 26
   display "New age: " added to (person["age"] as text)
   ```
2. Build a `book` table with keys `title`, `author`, `year`, and `pages`.
   Display all four fields, then update `year` and display it again.
3. For each of these, write whether a **list** or a **table** is the
   better fit, and why:
   - Every score on a class quiz
   - One student's name, grade, and homeroom number
   - A shopping list
   - A single product's name, price, and quantity in stock
