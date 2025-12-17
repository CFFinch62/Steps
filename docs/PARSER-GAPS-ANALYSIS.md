# Steps Language - Parser Implementation Gaps

## Executive Summary

Analysis of the Steps language parser reveals **8 major gaps** between documented features and actual implementation. The most critical issue is **bracket notation for table/list assignment**, which is documented but completely non-functional.

---

## Critical Issues (Must Fix)

### 1. Table Bracket Assignment ❌ BROKEN
**Documentation:** Lines 722, 728-729 of LANGUAGE-REFERENCE.md
```steps
set person["city"] to "Boston"       # Add new key
set person["age"] to 26              # Update existing key
```

**Status:** Parser error - "Expected 'to' after variable name"

**Impact:** HIGH - This is used in 9 files of the price_calculator example program

**Workaround Used:** Create entire table as literal
```steps
set results to ["price": price, "margin": margin, "profit": profit, "markup": markup, "cost": cost]
```

**Is Workaround Documented?** ✅ YES - Table literals are documented (line 331)

---

### 2. List Bracket Assignment ❌ BROKEN
**Documentation:** Line 386 of LANGUAGE-REFERENCE.md
```steps
set my_list[0] to "new value"
```

**Status:** Parser error - "Expected 'to' after variable name"

**Impact:** HIGH - Cannot modify list elements after creation

**Workaround:** None available - lists cannot be modified by index

**Is Workaround Documented?** ❌ NO

---

## Medium Priority Issues

### 3. Type Checking Operations ❌ BROKEN
**Documentation:** Lines 664-671 of LANGUAGE-REFERENCE.md
```steps
type of 42              # Should return "number"
x is a number           # Should return boolean
x is a text
x is a boolean
x is a list
x is a table
```

**Status:** Parser error - "Expected statement, found 'of'" / "Expected statement, found 'is'"

**Impact:** MEDIUM - Useful for validation but not critical

**Workaround:** None available

**Is Workaround Documented?** ❌ NO

---

### 4. Text Split Operation ❌ BROKEN
**Documentation:** Line 683 of LANGUAGE-REFERENCE.md
```steps
"a,b,c" split by ","    # Should return ["a", "b", "c"]
```

**Status:** Executes but produces no output/result

**Impact:** MEDIUM - Useful for parsing but not critical

**Workaround:** None available

**Is Workaround Documented?** ❌ NO

---

### 5. Character At Operation ❌ BROKEN
**Documentation:** Line 678 of LANGUAGE-REFERENCE.md
```steps
character at 0 of "hello"    # Should return "h"
```

**Status:** Executes but produces no output/result

**Impact:** LOW - Can use other string methods

**Workaround:** None available

**Is Workaround Documented?** ❌ NO

---

## Low Priority Issues

### 6. Add To List Statement ⚠️ PARTIAL
**Documentation:** Line 700 of LANGUAGE-REFERENCE.md
```steps
add 4 to my_list
```

**Status:** Executes but produces no output (may work silently)

**Impact:** LOW - Needs verification

**Testing Needed:** Check if list is actually modified

---

### 7. Remove From List Statement ⚠️ PARTIAL
**Documentation:** Line 701 of LANGUAGE-REFERENCE.md
```steps
remove 2 from my_list
```

**Status:** Executes but produces no output (may work silently)

**Impact:** LOW - Needs verification

**Testing Needed:** Check if list is actually modified

---

## Working Features ✅

These documented features work correctly:

1. **Table Literal Creation** ✅
   ```steps
   set person to ["name": "Alice", "age": 25]
   ```

2. **Table Access** ✅
   ```steps
   set name to person["name"]
   ```

3. **Type Conversion** ✅
   ```steps
   set x to 42 as text
   set y to "42" as number
   ```
   *Note: Works in assignment, but `(x as text)` in display context may have issues*

4. **Text Operations** ✅
   - `contains` ✅
   - `starts with` ✅
   - `ends with` ✅
   - `added to` (concatenation) ✅
   - `length of` ✅

5. **List Operations** ✅
   - List literal creation ✅
   - List access by index ✅
   - `is in` membership test ✅
   - `length of` ✅

6. **Arithmetic** ✅
   - All basic operators (+, -, *, /) ✅

---

## Type Conversion Behavior

**Documented:** Lines 359-365 of LANGUAGE-REFERENCE.md

**Actual Behavior:**
- ✅ `set x to 42 as text` - Works, assigns "42" to x
- ✅ `set y to "42" as number` - Works, assigns 42 to y
- ⚠️ `display x as text` - May not work in all contexts
- ✅ `display (x as text)` - Works when parenthesized

**Recommendation:** Type conversion works but may need parentheses in complex expressions

---

## Summary of Fixes Needed

| Priority | Issue | Parser Work Required |
|----------|-------|---------------------|
| **CRITICAL** | Table bracket assignment | Add support for `set table[expr] to value` |
| **CRITICAL** | List bracket assignment | Add support for `set list[expr] to value` |
| **HIGH** | Type checking operations | Implement `type of`, `is a number`, etc. |
| **MEDIUM** | Text split operation | Implement `split by` |
| **MEDIUM** | Character at operation | Implement `character at N of` |
| **LOW** | Verify list add/remove | Test if these work silently |

---

## Recommendations

### For Immediate Release
1. **Update documentation** to remove or mark as "not yet implemented":
   - Table/list bracket assignment
   - Type checking operations
   - `split by` and `character at`

2. **Add to documentation** the working workarounds:
   - Table literal creation for building tables
   - Note that type conversion requires parentheses in some contexts

### For Next Parser Version
1. **Implement bracket assignment** (highest priority)
2. **Implement type checking** operations
3. **Implement missing text** operations
4. **Test and fix list** manipulation statements

---

## Answer to User's Question

**"Are the syntax changes you made using methods clearly documented?"**

**YES** ✅ - The table literal syntax I used is documented:
- Line 331: `["key": "value"]` shown as valid literal
- Line 725: Example of creating table with `set person to ["name": "Alice", "age": 25]`

The workaround is fully documented and is the correct way to create tables. The **problem** is that the documentation ALSO shows bracket assignment as working (lines 722, 728-729), which creates confusion since that feature isn't implemented.
