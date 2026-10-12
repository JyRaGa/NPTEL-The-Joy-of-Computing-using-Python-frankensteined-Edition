# JOC Jan-2026 · Week 4: Assignment 4

- Source: <https://www.youtube.com/watch?v=IskmJzaIc8A> · NPTEL Solver · published 2026-02-05
- Portal: due 2026-02-18, 23:59 IST → **Jan-2026 session**
- `[x]` = option ticked by the video author before submitting → unverified (no score shown)

**Building a Mini Dobble Game Using Python**

**In this activity, a learner designs a simplified version of the popular *Dobble* game using Python. The goal of the game is simple: two cards are generated such that exactly one symbol is common between them, and the player must correctly identify that common symbol.**

**Step 1: Preparing the Symbol Set**

The game begins by importing two built-in Python modules:
- string → used to access alphabets easily
- random → used to generate randomness in the game

Using string.ascii_letters, a list of symbols is created that contains:
- lowercase letters (a–z)
- uppercase letters (A–Z)

This list becomes the **symbol pool** from which all card symbols are drawn.

Once a symbol is used, it is removed from the pool to prevent duplication.

**Step 2: Deciding Positions on Cards**

Each card contains **5 positions**, indexed from 0 to 4.

Two random positions are generated:
- pos1 → where the common symbol will appear on **Card 1**
- pos2 → where the common symbol will appear on **Card 2**

These positions are chosen randomly, which ensures that the common symbol does not always appear in the same place.

**Step 3: Selecting the Common Symbol**

One symbol is randomly selected from the symbol pool to act as the **common symbol** shared by both cards.

Immediately after selecting it, the symbol is **removed from the pool**, ensuring:
- it cannot accidentally appear again
- uniqueness across the rest of the cards

This guarantees the key rule of Dobble: **only one symbol matches.**

**Step 4: Creating the Cards**

Two lists are created:
- card1
- card2

Each list has **5 empty slots**, initialized with ZERO.

These lists represent the two cards shown to the player.

**Step 5: Handling Common and Non-Common Positions**
- If pos1 and pos2 are the same, the common symbol is placed at that index in both cards
- If they are different:
  - The common symbol is placed at pos1 in Card 1
  - The same symbol is placed at pos2 in Card 2
  - Two **different symbols** are placed in the swapped positions to avoid accidental matching

This logic ensures that:
- only one symbol is shared
- all other symbols differ across cards

**Step 6: Filling Remaining Positions Using a Loop**

A while loop runs from index 0 to 4.

For every index **except** pos1 and pos2:
- one new symbol is picked for Card 1
- a different new symbol is picked for Card 2
- both symbols are removed from the pool

This systematic filling ensures:
- no empty positions remain
- no duplicate symbols exist
- only one common symbol survives

**Step 7: Player Interaction**

The player is prompted with:

Spot the common symbol:

The input is stored in a variable and represents the player's guess.

This step introduces **human interaction** into the program, converting logic into a playable game.

**Step 8: Validating the Answer**

The program compares:
- the player's input
- the actual common symbol

If they match → "Right!" is displayed
Otherwise → "Wrong!" is displayed

This final comparison closes the game loop and gives instant feedback.

**1) What is the *maximum* number of unique symbols that can be safely used by this program without causing a runtime error?**
- [ ] 26
- [ ] Unlimited
- [ ] 10
- [x] 52

**2) Which statement about pos1 and pos2 is logically correct?**
- [x] They may or may not be equal
- [ ] They are always different
- [ ] They are fixed once generated
- [ ] They cannot be equal

**3) Why is same_symbol removed from the symbol list immediately after selection?**
- [ ] To improve randomness
- [ ] To reduce memory usage
- [x] To ensure it appears exactly once on each card
- [ ] To simplify the loop condition

**4) What problem does the condition if pos1 == pos2 prevent?**
- [ ] Index out-of-range error
- [x] Logical conflict in symbol placement
- [ ] Infinite looping
- [ ] Input mismatch

**5) When pos1 ≠ pos2, how many times does the while loop assign symbols?**
- [ ] 5
- [ ] 2
- [ ] 4
- [x] 3

**6) What is the most serious consequence if symbols are not removed inside the loop?**
- [ ] Cards become sorted automatically
- [x] Multiple common symbols may appear
- [ ] Loop runs indefinitely
- [ ] Cards become identical

**7) Which player input would be marked incorrect even if the symbol looks correct?**
- [ ] Input entered quickly
- [ ] Input with correct spacing
- [x] Lowercase input for an uppercase symbol
- [ ] Input after a delay

**8) Which statement is guaranteed true every time the program runs?**
- [ ] Symbols appear in alphabetical order
- [ ] Both cards are mirror images
- [ ] Cards share no symbols
- [x] Cards share exactly one symbol

---

**When One List Becomes Many (But Isn't)**

**Context**

Ravi is maintaining student records in Python. Each record is stored as a **list**, and sometimes a list even contains **another list** (nested list). Ravi assumes that assigning one list to another creates a *new copy*. What actually happens surprises him.

This case study walks through Ravi's understanding **step by step**.

**Part 1: List Assignment — No Copy at All**

Ravi starts with a list of marks.
```python
marks = [70, 80, 90]
backup = marks
```
Ravi thinks backup is a separate list.

Now he modifies backup:
```python
backup[0] = 100
print(marks)
print(backup)
```
**What Actually Happens**
- marks and backup **refer to the same list**
- No new list is created
- Any change through one name affects the other

Output

[100, 80, 90]

[100, 80, 90]

**Key Insight:**
List assignment copies the **reference**, not the data.

**Part 2: Shallow Copy — New List, Same Inner Objects**

Ravi now learns about the copy() method.
```python
marks = [[70, 80], [90, 95]]
backup = marks.copy()
```
This time, Ravi updates an inner list:
```python
backup[0][0] = 100
print(marks)
print(backup)
```
**What Happens Now**
- marks and backup are **different outer lists**
- BUT the **inner lists are shared**
- Modifying a nested list affects both

**Output :**

[[100, 80], [90, 95]]

[[100, 80], [90, 95]]

**Key Insight:**
Shallow copy copies the **outer list only**, not nested lists.

Shallow Copy with Slice Notation
```python
marks = [[1, 2], [3, 4]]
backup = marks[:]
backup[1][1] = 99

print(marks)
print(backup)
```
[[1, 2], [3, 99]]

[[1, 2], [3, 99]]

**Deep Copy — Complete Independence**

Ravi now wants a **fully independent copy**.
```python
import copy

marks = [[70, 80], [90, 95]]
backup = copy.deepcopy(marks)
backup[0][0] = 100
print(marks)
print(backup)
```
**What Happens Now**
- Outer list is copied
- Inner lists are copied
- Changes do **not** affect the original

Output:

[[70, 80], [90, 95]]

[[100, 80], [90, 95]]

**9)**
```python
a = [10, 20, 30]
b = a
b.append(40)
print(a)
```
**What will be printed?**
- [ ] [10, 20, 30]
- [x] [10, 20, 30, 40]
- [ ] Error
- [ ] [40]

**10)**
```python
a = [1, 2, 3]
b = a.copy()
b[0] = 99
print(a)
```
**Choose the correct output.**
- [ ] [1, 99, 3]
- [ ] [99, 2, 3]
- [x] [1, 2, 3]
- [ ] Error

**11)**
```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][1] = 99
print(a)
```
**What is printed?**
- [ ] Error
- [ ] [[1, 2], [3, 4]]
- [ ] [[1, 2], [3, 99]]
- [x] [[1, 99], [3, 4]]

**12)**
```python
a = [[5, 6], [7, 8]]
b = a[:]
b[1] = [0, 0]
print(a)
```
**Predict the output.**
- [ ] Error
- [x] [[5, 6], [7, 8]]
- [ ] [[5, 6], [0, 0]]
- [ ] [[0, 0], [7, 8]]

**13)**
```python
a = [[5, 6], [7, 8]]
b = a[:]
b[1][0] = 100
print(a)
```
**Select the correct output.**
- [ ] [[5, 6], [7, 8]]
- [ ] Error
- [ ] [[100, 6], [7, 8]]
- [x] [[5, 6], [100, 8]]

**14)**
```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 9
print(a)
```
**Select the correct output.**
- [ ] [[9, 2], [3, 4]]
- [ ] Error
- [x] [[1, 2], [3, 4]]
- [ ] [[1, 9], [3, 4]]

**15)**
```python
import copy

a = [[1, 2], [3, 4]]
b = a
c = a.copy()
d = copy.deepcopy(a)

b[0][0] = 10
c[1][1] = 20
d[0][1] = 30

print(a)
```
**What is the final output?**
- [ ] [[10, 30], [3, 20]]
- [ ] [[10, 2], [3, 4]]
- [ ] [[1, 2], [3, 4]]
- [x] [[10, 2], [3, 20]]
