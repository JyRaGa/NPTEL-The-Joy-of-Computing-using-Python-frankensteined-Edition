# JOC Jan-2024 · Week 10: Assignment 10

- Source: <https://www.youtube.com/watch?v=2OXdmqLhAts> · Study_Ease · published 2024-04-01
- Portal: `noc24_cs57`, due 2024-04-03, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked by the video author ("Your last recorded submission was on 2024-04-02, 01:06 IST") → unverified, no score shown

**1) In the Josephus problem, a group of soldiers forms a circle, and every kᵗʰ soldier is eliminated until only one remains. What would be the output of the following code:**

```python
def josephus(n, k):
        if n == 1:
                return 1
        else:
                return (josephus(n - 1, k) + k - 1) % n + 1
n = 25 #Number of soldiers
k = 3 #Elimination factor
result = josephus(n, k)
print(result)
```
- [ ] 3
- [x] 14
- [ ] 19
- [ ] 13

**2) What is the purpose of the lower() and upper() methods in Python when applied to strings?**
- [x] **lower()** converts a string to all lowercase letters, while **upper()** converts a string to all uppercase letters.
- [ ] **lower()** converts a string to all uppercase letters, while **upper()** converts a string to all lowercase letters.
- [ ] Both **lower()** and **upper()** methods perform the same task of converting a string to title case.
- [ ] **lower()** removes all whitespace from a string, while **upper()** adds whitespace to each character in a string.

**3)**

```python
original_string = "apple, banana, cherry, apple, date"
modified_string = original_string.replace("apple", "orange")
print(modified_string)
```
**What will be the output of the code snippet provided above?**
- [x] orange, banana, cherry, orange, date
- [ ] orange, banana, cherry, apple, date
- [ ] apple, banana, cherry, apple, date
- [ ] apple, banana, cherry, orange, orange

**4) Slicing in lists works in the same manner as slicing in strings. If P is a non-empty list of length n, we wish to create a list Q that has the first n−1 elements in P. Select the correct implementation(s) of this program.**
- [x] `Q = P[0: len(P) - 1]`
- [x] `Q = P[:len(P) - 1]`
- [x] `Q = P[0:-1]`
- [x] `Q = P[:-1]`

**5) Select all correct options about the matrix given below.**
**`matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]`**
- [x] `len(matrix)` is the number of rows in the matrix
- [x] `len(matrix[0])` is the number of columns of the matrix
- [x] The dimension of matrix is 4×3
- [ ] The dimension of matrix is 3×4

**6) L is a non-empty list of integers and x is an integer. Assume that both L and x have already been defined. The following code does not throw any error when executed. Lines 1 and 6 will be used to refer to the state of the variables before and after key sections of the code are executed.**

```python
pass                    # before
count = 0
while len(L) > 0:
        L.remove(x)
        count += 1
pass                    # after
```
**If the value of count is 10 at the end of the execution of the code (line 6), which of the following statements are true?**
- [x] x is an element of L at line 1.
- [ ] L has at least two different (unequal) elements in it at line 1
- [ ] Length of L is 10 at line 1
- [x] Length of L is 0 at line 6

---

**Assume that L is a non-empty list of positive integers. Also assume that the list is a distinct collection of numbers, i.e., no two numbers are alike. Consider the following code. Answer questions 7 and 8 based on this code.**

```python
S = 0
for x in L:
        S += x

flag = False
y = -1
for x in L:
        if x * len(L) == S:
                flag = True
                y = x
                break
```

**7) If flag is True at the end of execution of the code given above, which of the following statements are true? Note that the options should be true for any list L that satisfies the conditions given in the common data. Multiple options could be correct.**
- [x] y is an element in the list L
- [ ] y is the greatest number in the list
- [x] y is the average (arithmetic mean) of the numbers in the list
- [x] y is the element at index `len(L) // 2` in the list L

**8) Assume that L is a list of the first n positive integers, where `n>0`. Under what conditions will the variable flag be `True` at the end of the execution of the code given above?**
- [x] n is an odd integer
- [ ] n is an even integer
- [ ] n is a complex number
- [ ] None of the above

**9) Which NumPy function is used to create a matrix of a specified shape with random values between 0 and 1?**
- [ ] `np.random.randn()`
- [ ] `np.random.random()`
- [x] `np.random.rand()`
- [ ] `np.random.randint()`

**10) Select the correct implementation of a program that creates a text file named pattern.txt with the following contents:**

```
az
by
cx
dw
ev
fu
gt
hs
ir
jq
kp
lo
mn
```
- [ ] Option 1
  ```python
  f = open('pattern.txt', 'r')
  letters = 'abcdefghijklmnopqrstuvwxyz'
  n = len(letters) // 2
  for i in range(n):
      line = letters[i] + letters[-1 - i]
      if i != n - 1:
          line = line + '\n'
      f.write(line)
  f.close()
  ```
- [ ] Option 2
  ```python
  f = open('pattern.txt', 'w')
  letters = 'abcdefghijklmnopqrstuvwxyz'
  n = len(letters) // 2
  for i in range(n):
      line = letters[i] + letters[-1 - i]
      f.write(line)
  f.close()
  ```
- [x] Option 3
  ```python
  f = open('pattern.txt', 'w')
  letters = 'abcdefghijklmnopqrstuvwxyz'
  n = len(letters) // 2
  for i in range(n):
      line = letters[i] + letters[-1 - i]
      if i != n - 1:
          line = line + '\n'
      f.write(line)
  f.close()
  ```
- [ ] Option 4
  ```python
  f = open('pattern.txt', 'w')
  letters = 'abcdefghijklmnopqrstuvwxyz'
  n = len(letters)
  for i in range(n):
      line = letters[i] + letters[-1 - i]
      if i != n - 1:
          line = line + '\n'
      f.write(line)
  f.close()
  ```
