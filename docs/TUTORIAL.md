# Steps Programming Language - Interactive Tutorial

> **Learn Steps step-by-step with hands-on examples!**

This tutorial will guide you through the Steps programming language with practical examples you can run and modify. Each lesson builds on the previous one, introducing new concepts gradually.

---

## Table of Contents

1. [Getting Started](#lesson-1-getting-started)
2. [Variables and Data Types](#lesson-2-variables-and-data-types)
3. [User Input and Output](#lesson-3-user-input-and-output)
4. [Making Decisions](#lesson-4-making-decisions)
5. [Loops and Repetition](#lesson-5-loops-and-repetition)
6. [Working with Lists](#lesson-6-working-with-lists)
7. [Working with Tables](#lesson-7-working-with-tables)
8. [Creating Your First Step](#lesson-8-creating-your-first-step)
9. [Steps with Parameters](#lesson-9-steps-with-parameters)
10. [Organizing with Floors](#lesson-10-organizing-with-floors)
11. [Building a Complete Project](#lesson-11-building-a-complete-project)

---

## How to Use This Tutorial

Each lesson has:
- **Concept**: What you'll learn
- **Example Program**: A working Steps program in `/projects/tutorial/`
- **Try It**: Exercises to practice
- **Key Takeaways**: Summary of important points

### Running the Examples

```bash
# From the Steps directory
python -m steps.main run projects/tutorial/lesson_01_hello

# Or use the IDE
python -m steps_ide.main
# Then open the lesson's .building file and press F5
```

---

## Lesson 1: Getting Started

### Concept: Your First Program

Every Steps program is a **building**. The simplest building just displays a message and exits.

### Example: `lesson_01_hello.building`

```steps
building: lesson_01_hello
    note: My first Steps program!
    
    display "Hello, Steps!"
    display "Welcome to programming!"
    
    exit
```

### What's Happening?

- `building: lesson_01_hello` - Declares this is a building named "lesson_01_hello"
- `note:` - A comment explaining what the code does
- `display` - Shows text to the user
- `exit` - Ends the program

### Try It

1. Run the program
2. Change the messages to say something different
3. Add more `display` statements

### Key Takeaways

✓ Every program starts with `building: name`  
✓ Use `display` to show output  
✓ Use `note:` for comments  
✓ End with `exit`

---

## Lesson 2: Variables and Data Types

### Concept: Storing and Using Data

Variables hold data. Steps has five data types: **number**, **text**, **boolean**, **list**, and **table**.

### Example: `lesson_02_variables.building`

See `/projects/tutorial/lesson_02_variables/lesson_02_variables.building`

### What's Happening?

- `set variable_name to value` - Creates or updates a variable
- Variables can hold different types of data
- You can do math with numbers
- You can combine text with `added to`

### Try It

1. Create a variable with your age
2. Calculate your age in months (age × 12)
3. Display the result

### Key Takeaways

✓ Use `set` to create variables
✓ Numbers can be whole or decimal
✓ Text goes in "quotes"
✓ Booleans are `true` or `false`

---

## Lesson 3: User Input and Output

### Concept: Interactive Programs

Programs are more interesting when they interact with users!

### Example: `lesson_03_input.building`

See `/projects/tutorial/lesson_03_input/lesson_03_input.building`

### What's Happening?

- `set variable to input as type` - Gets input from the user
- `as number` - Converts input to a number
- `as text` - Keeps input as text (default)

### Try It

1. Ask for the user's favorite color
2. Ask for their lucky number
3. Display a message using both

### Key Takeaways

✓ Use `input as number` for numeric input
✓ Use `input as text` for text input
✓ Always display a prompt before asking for input

---

## Lesson 4: Making Decisions

### Concept: Conditional Logic

Programs need to make decisions based on conditions.

### Example: `lesson_04_decisions.building`

See `/projects/tutorial/lesson_04_decisions/lesson_04_decisions.building`

### What's Happening?

- `if condition` - Executes code if condition is true
- `otherwise if condition` - Checks another condition
- `otherwise` - Executes if all conditions are false
- Comparison operators: `is equal to`, `is greater than`, `is less than`

### Try It

1. Ask for a temperature
2. Display "Hot" if > 80, "Cold" if < 60, "Nice" otherwise
3. Add more temperature ranges

### Key Takeaways

✓ Use `if` for conditional execution
✓ Use `otherwise if` for multiple conditions
✓ Use `otherwise` as a catch-all
✓ Conditions use English phrases like "is equal to"

---

## Lesson 5: Loops and Repetition

### Concept: Repeating Actions

Loops let you repeat code multiple times.

### Example: `lesson_05_loops.building`

See `/projects/tutorial/lesson_05_loops/lesson_05_loops.building`

### What's Happening?

- `repeat N times` - Repeats code N times
- `while condition` - Repeats while condition is true
- `for each item in list` - Iterates over a list

### Try It

1. Create a countdown from 10 to 1
2. Ask the user to guess a number (1-10) until they get it right
3. Display all even numbers from 2 to 20

### Key Takeaways

✓ Use `repeat N times` for fixed repetition
✓ Use `while` for conditional repetition
✓ Use `for each` to process lists
✓ Be careful to avoid infinite loops!

---

## Lesson 6: Working with Lists

### Concept: Collections of Data

Lists store multiple values in order.

### Example: `lesson_06_lists.building`

See `/projects/tutorial/lesson_06_lists/lesson_06_lists.building`

### What's Happening?

- `[1, 2, 3]` - Creates a list
- `add value to list_name` - Adds to the end
- `remove value from list_name` - Removes first occurrence
- `list_name[index]` - Accesses an item (0-based)
- `length of list_name` - Gets the number of items

### Try It

1. Create a shopping list
2. Add 5 items
3. Display each item with a number
4. Remove an item and display the updated list

### Key Takeaways

✓ Lists hold multiple values
✓ Use `add` and `remove` to modify lists
✓ Access items with `[index]` (starts at 0)
✓ Use `length of` to get the size

---

## Lesson 7: Working with Tables

### Concept: Key-Value Storage

Tables (dictionaries/maps) store data with named keys.

### Example: `lesson_07_tables.building`

See `/projects/tutorial/lesson_07_tables/lesson_07_tables.building`

### What's Happening?

- `["key": value]` - Creates a table
- `table["key"]` - Accesses a value
- `set table["key"] to value` - Sets a value
- Tables can store any type of data

### Try It

1. Create a table for a book (title, author, year, pages)
2. Display each piece of information
3. Update the year and display again

### Key Takeaways

✓ Tables store key-value pairs
✓ Use `["key"]` to access values
✓ Keys are text, values can be any type
✓ Great for structured data

---

## Lesson 8: Creating Your First Step

### Concept: Reusable Code

Steps are reusable pieces of code. They're like functions in other languages.

### Example: `lesson_08_first_step/`

See the complete project in `/projects/tutorial/lesson_08_first_step/`

### What's Happening?

- Steps go in their own `.step` files
- Steps belong to floors
- Use `call step_name` to run a step
- Steps can return values

### Try It

1. Create a step that displays your name
2. Call it multiple times from the building
3. Create another step that displays the date

### Key Takeaways

✓ Steps are reusable code units
✓ One step per file
✓ Steps must belong to a floor
✓ Use `call` to execute a step

---

## Lesson 9: Steps with Parameters

### Concept: Passing Data to Steps

Steps can accept input (parameters) and return output.

### Example: `lesson_09_parameters/`

See the complete project in `/projects/tutorial/lesson_09_parameters/`

### What's Happening?

- `expects: param1, param2` - Declares parameters
- `returns: result` - Declares return value
- `call step_name with arg1, arg2 storing result in variable` - Calls with arguments
- Parameters are like variables inside the step

### Try It

1. Create a step that adds two numbers
2. Create a step that greets a person by name
3. Create a step that calculates the area of a rectangle

### Key Takeaways

✓ Use `expects:` to declare parameters
✓ Use `returns:` to declare return value
✓ Use `with` to pass arguments
✓ Use `storing result in` to capture return value

---

## Lesson 10: Organizing with Floors

### Concept: Grouping Related Steps

Floors organize related steps into logical groups.

### Example: `lesson_10_floors/`

See the complete project in `/projects/tutorial/lesson_10_floors/`

### What's Happening?

- Floors are folders containing related steps
- Each floor has a `.floor` file listing its steps
- Steps declare which floor they belong to
- Floors help organize large projects

### Try It

1. Create a "math" floor with add, subtract, multiply steps
2. Create a "text" floor with uppercase, lowercase steps
3. Use steps from both floors in your building

### Key Takeaways

✓ Floors group related functionality
✓ One floor per folder
✓ Floor files list all steps
✓ Good organization makes code easier to understand

---

## Lesson 11: Building a Complete Project

### Concept: Putting It All Together

Let's build a complete project using everything we've learned!

### Example: `lesson_11_complete_project/`

See the complete project in `/projects/tutorial/lesson_11_complete_project/`

This is a **Contact Manager** that demonstrates:
- Multiple floors (contacts, display, input)
- Steps with parameters
- Lists and tables
- User input
- Control flow
- Loops

### What's Happening?

The project is organized into:
- **contacts floor**: Managing contact data
- **display floor**: Showing information
- **input floor**: Getting user input
- **Main building**: Coordinating everything

### Try It

1. Run the contact manager
2. Add some contacts
3. Search for a contact
4. Modify it to add phone numbers
5. Add a feature to delete contacts

### Key Takeaways

✓ Real projects use multiple floors
✓ Each floor has a clear purpose
✓ Steps are small and focused
✓ Good organization makes projects maintainable

---

## Next Steps

Congratulations! You've completed the Steps tutorial! 🎉

### Where to Go From Here

1. **Read the Language Reference** (`docs/LANGUAGE-REFERENCE.md`) for complete details
2. **Explore Example Projects** in `/projects/` for more complex examples
3. **Build Your Own Project** - Start small and grow it!
4. **Use the IDE** (`python -m steps_ide.main`) for a better development experience

### Project Ideas

- **Calculator**: Basic arithmetic with a menu
- **Quiz Game**: Ask questions and keep score
- **Todo List**: Add, complete, and remove tasks
- **Grade Calculator**: Input grades and calculate average
- **Simple Database**: Store and search records
- **Text Adventure**: A choose-your-own-adventure game

### Getting Help

- Check the **User Guide** (`docs/USER-GUIDE.md`)
- Review the **Language Reference** (`docs/LANGUAGE-REFERENCE.md`)
- Look at existing projects for examples
- Experiment in the REPL (`python -m steps_repl.main`)

---

## Summary of Key Concepts

| Concept | Syntax | Example |
|---------|--------|---------|
| Display output | `display` | `display "Hello!"` |
| Create variable | `set` | `set age to 25` |
| Get input | `input as type` | `set name to input as text` |
| Condition | `if` / `otherwise` | `if age is greater than 18` |
| Loop (fixed) | `repeat N times` | `repeat 5 times` |
| Loop (conditional) | `while` | `while count is less than 10` |
| Loop (list) | `for each` | `for each item in list` |
| Create list | `[]` | `set nums to [1, 2, 3]` |
| Create table | `[:]` or `["key": val]` | `set person to ["name": "Alice"]` |
| Call step | `call` | `call greet with "Bob"` |
| Return value | `return` | `return result` |

Happy coding with Steps! 🏗️


