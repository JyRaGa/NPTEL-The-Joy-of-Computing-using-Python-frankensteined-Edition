# JOC Jan-2026 · Week 3: Assignment 3

- Source: <https://www.youtube.com/watch?v=G0KrE9G7oNM> · NPTEL Solver · published 2026-01-30
- Portal: due 2026-02-11, 23:59 IST → **Jan-2026 session**
- `[x]` = option ticked by the video author before submitting → unverified (no score shown). Note: Q6's tick contradicts the scenario text (`sort()` output), so treat it with care.

**Riya is building an Order Processing System for an online grocery store.**
**She uses a Python list because it maintains order and allows items to be added, removed, or updated dynamically.**

**1. Creating the Order List (Initialization)**
At the start of the day, the system has some confirmed orders.
```python
orders = ["Milk", "Bread", "Eggs"]
print(orders)
```
**How this works:**
- [] creates a list
- Items are stored in order
- Indexing starts from 0

Output:
['Milk', 'Bread', 'Eggs']

**2. Adding a New Order at the End (append)**
A customer orders **Butter,** which must be added last.
```python
orders.append("Butter")
print(orders)
```
**How this works:**
- append() adds **one item at the end**
- Existing order remains unchanged

**Output:**
['Milk', 'Bread', 'Eggs', 'Butter']

**3. Adding a Priority Order at a Specific Position (insert)**
A priority customer orders **Fruits,** which must come early.
```python
orders.insert(1, "Fruits")
print(orders)
```
**How this works:**
- insert(index, value) places the value at that index
- Elements from that position shift right

**Output:**
['Milk', 'Fruits', 'Bread', 'Eggs', 'Butter']

**4. Adding Multiple Orders Together (extend)**
A partner store sends additional orders.
```python
partner_orders = ["Rice", "Oil"]
orders.extend(partner_orders)
print(orders)
```
How this works:
- extend() adds elements **one by one**
- No nested list is created

**Output:**
['Milk', 'Fruits', 'Bread', 'Eggs', 'Butter', 'Rice', 'Oil']

**5. Accessing a Specific Order (Indexing)**
The system checks the **first order received.**
```python
print(orders[0])
```
**How this works:**
- Index 0 always refers to the first element

**Output:**
Milk

**6. Processing Orders in Batches (Slicing)**
The packaging team processes the first three orders together.
```python
batch_orders = orders[0:3]
print(batch_orders)
```
**How this works:**
- Start index included
- End index excluded
- Creates a **new list**

**Output:**
['Milk', 'Fruits', 'Bread']

**7. Updating an Incorrect Order (Assignment)**
A customer ordered **Milk** but wanted **Almond Milk.**
```python
orders[orders.index("Milk")] = "Almond Milk"
print(orders)
```
**How this works:**
- index() finds the position of "Milk"
- Assignment replaces the value at that index

**Output:**
['Almond Milk', 'Fruits', 'Bread', 'Eggs', 'Butter', 'Rice', 'Oil']

**8. Removing a Cancelled Order by Name (remove)**
The **Bread** order is cancelled.
```python
orders.remove("Bread")
print(orders)
```
**How this works:**
- remove() deletes the **first matching element**
- Remaining items shift lef

**Output:**
['Almond Milk', 'Fruits', 'Eggs', 'Butter', 'Rice', 'Oil']

**9. Sorting Orders Alphabetically (sort)**
For warehouse efficiency, orders are sorted.
```python
orders.sort()
print(orders)
```
**How this works:**
- sort() rearranges items alphabetically
- Sorting happens **in-place**

**Output:**
['Almond Milk', 'Butter', 'Eggs', 'Fruits', 'Oil', 'Rice']

**10. Clearing All Orders at End of Day (clear)**
After delivery, the system resets for the next day.
```python
orders.clear()
print(orders)
```
**How this works:**
- Removes all elements
- List still exists but becomes empty

**Output:**
[]

---

**1)**
```python
orders = ["Milk", "Bread", "Eggs"]
orders.append("Butter")
print(orders)
```
**What will be displayed after execution?**
- [ ] ['Milk', 'Bread', 'Eggs']
- [ ] ['Butter', 'Milk', 'Bread', 'Eggs']
- [ ] Error
- [x] ['Milk', 'Bread', 'Eggs', 'Butter']

**2)**
```python
orders = ["Milk", "Bread", "Eggs"]
orders.insert(1, "Fruits")
print(orders)
```
**Which sequence is produced?**
- [ ] ['Milk', 'Bread', 'Eggs', 'Fruits']
- [ ] Error
- [x] ['Milk', 'Fruits', 'Bread', 'Eggs']
- [ ] ['Fruits', 'Milk', 'Bread', 'Eggs']

**3)**
```python
orders = ["Milk", "Bread", "Eggs"]
orders.extend(["Rice", "Oil"])
print(orders)
```
**Which list is printed?**
- [ ] ['Milk', 'Bread', 'Eggs', ['Rice', 'Oil']]
- [ ] Error
- [ ] ['Rice', 'Oil', 'Milk', 'Bread', 'Eggs']
- [x] ['Milk', 'Bread', 'Eggs', 'Rice', 'Oil']

**4)**
```python
orders = ["Milk", "Fruits", "Bread"]
print(orders[0])
```
**Which value appears on the screen?**
- [ ] Error
- [ ] Bread
- [x] Milk
- [ ] Fruits

**5)**
```python
orders = ["Milk", "Fruits", "Bread", "Eggs"]
print(orders[1:3])
```
**Which option correctly represents the printed list?**
- [ ] ['Milk', 'Fruits']
- [ ] ['Bread', 'Eggs']
- [ ] ['Fruits', 'Bread', 'Eggs']
- [x] ['Fruits', 'Bread']

**6)**
```python
orders = ["Milk", "Bread", "Eggs"]
orders.append("Butter")
orders.sort()
print(orders)
```
**After execution, which arrangement is obtained?**
- [ ] ['Butter', 'Bread', 'Eggs', 'Milk']
- [ ] ['Bread', 'Butter', 'Eggs', 'Milk']
- [ ] Error
- [x] ['Milk', 'Bread', 'Eggs', 'Butter']

**7)**
```python
orders = ["Milk", "Bread", "Eggs"]
orders.insert(1, "Fruits")
orders.remove("Bread")
print(orders)
```
**What does the list finally contain?**
- [ ] ['Milk', 'Eggs']
- [ ] Error
- [ ] ['Fruits', 'Milk', 'Eggs']
- [x] ['Milk', 'Fruits', 'Eggs']

**8)**
```python
orders = ["Milk", "Bread"]
orders.extend(["Eggs", "Butter", "Rice"])
print(orders[1:4])
```
**Which elements are shown?**
- [x] ['Bread', 'Eggs', 'Butter']
- [ ] ['Eggs', 'Butter', 'Rice']
- [ ] Error
- [ ] ['Milk', 'Bread', 'Eggs']

**9)**
```python
orders = ["Milk", "Bread", "Eggs"]
orders[orders.index("Milk")] = "Almond Milk"
orders.sort()
print(orders)
```
**Which list is displayed?**
- [ ] ['Bread', 'Eggs', 'Almond Milk']
- [ ] Error
- [x] ['Almond Milk', 'Bread', 'Eggs']
- [ ] ['Milk', 'Bread', 'Eggs']

**10)**
```python
orders = ["Milk", "Bread", "Eggs"]
orders.insert(0, "Rice")
orders.sort()
print(orders[1:3])
```
**Which option correctly matches the program behavior?**
- [ ] ['Bread', 'Eggs']
- [ ] ['Milk', 'Rice']
- [ ] Error
- [x] ['Eggs', 'Milk']

---

**Student Performance Analyzer**

**Ravi is a Teaching Assistant who is preparing a small Python utility to analyze student scores collected from a programming lab. The data comes in raw lists, but the final processed results must be immutable, so Ravi uses tuples.**

**Step 1: Raw Student Marks (List)**
Ravi starts with a list of marks obtained by students:
```python
marks = [35, 78, 92, 45, 60, 88, 49, 100]
```
This list is **mutable**, meaning values can change.

**Step 2: Filtering Passed Students (List Comprehension)**
Only students scoring **50 or more** are considered passed.
```python
passed = [m for m in marks if m >= 50]
```
- The expression m for m in marks generates values
- The condition if m >= 50 filters values
- The result is a **new list,** not modifying the original

Result:
passed = [78, 92, 60, 88, 100]

**Step 3: Adding Bonus Marks (List Comprehension)**
Each passed student gets **5 bonus marks**, but the total should not exceed **100.**
```python
bonus_marks = [min(m + 5, 100) for m in passed]
```
- min(m + 5, 100) ensures marks do not exceed 100
- This still produces a **list**

Result:
bonus_marks = [83, 97, 65, 93, 100]

**Step 4: Converting List to Tuple**
Ravi wants to freeze the final results so they cannot be changed accidentally
```python
final_scores = tuple(bonus_marks)
```
Result:
final_scores = (83, 97, 65, 93, 100)

**Step 5: Creating Score–Index Pairs :**
Ravi now wants to tag each score with its **index position.**
```python
indexed_scores = [(i, final_scores[i]) for i in range(len(final_scores))]
```
Result:
indexed_scores = [(0, 83), (1, 97), (2, 65), (3, 93), (4, 100)]
Each element is a **tuple inside a list.**

**11) What is the value of passed?**
```python
marks = [35, 78, 92, 45, 60, 88, 49, 100]
passed = [m for m in marks if m >= 50]
```
- [ ] [35, 78, 92, 45, 60, 88, 49, 100]
- [x] [78, 92, 60, 88, 100]
- [ ] (78, 92, 60, 88, 100)
- [ ] [50, 60, 88, 100]

**12)**
```python
passed = [78, 92, 60, 88, 100]
bonus_marks = [min(m + 5, 100) for m in passed]
```
**What does bonus_marks contain?**
- [ ] [83, 97, 65, 93, 105]
- [ ] [78, 92, 60, 88, 100]
- [x] [83, 97, 65, 93, 100]
- [ ] (83, 97, 65, 93, 100)

**13) What is the type of final_scores?**
```python
final_scores = tuple(bonus_marks)
```
- [ ] List
- [ ] Set
- [ ] Dictionary
- [x] Tuple

**14) What is the output of:**
```python
indexed_scores = [(i, final_scores[i]) for i in range(len(final_scores))]
print(indexed_scores[2])
```
- [ ] (2, 97)
- [ ] (1, 97)
- [x] (2, 65)
- [ ] 65

**15) What happens if the following line is executed?**
```python
final_scores[0] = 90
```
- [ ] The value updates successfully
- [ ] The tuple converts into a list
- [x] A runtime error occurs
- [ ] Only the first element changes
