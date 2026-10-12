# JOC Jul-2019 · Week 2: Introduction to Python · Assignment 2

- Source: <https://www.youtube.com/watch?v=ZRLZ5CAMBfQ> · Ultimate Gamer · published 2019-08-05
- Portal: "Your last recorded submission was on 2019-08-05, 19:19 IST"; due 2019-08-14 → **Jul-2019 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified. Video ends with: "WE CAN NOT GUARANTEE THAT THESE SOLUTIONS ARE 100% CORRECT."
- Code is shown as plain portal text (not code blocks); indentation reproduced as displayed.

**1) In Python, a variable must be declared before it is assigned a value.**
- [ ] True
- [x] False

**2) What is the output of the following program?**
```
for i in range(2):
        print(i,end="")

for i in range(4,6):
        print(i,end="" )
```
- [ ] 014
- [ ] 015
- [x] 0145
- [ ] 01

**3) What is the output if the following code snippet?**
```
a=4.5
b=15
print(a+b)
```
- [ ] 19
- [ ] 20
- [x] 19.5
- [ ] No output. An error is thrown.

**4) What is the output of the following program?**
```
i = 1
while True:
        if i%3 == 0:
                break
        print(i,end="")
        i + = 1
```
- [ ] 12
- [ ] 123
- [ ] 1
- [x] No output is displayed due to syntax error.

**5) What is the output of the following program?**
```
i = 2
while True:
    if i%3 == 0:
        break
    print(i,end="")
    i += 2
```
- [ ] 12
- [x] 24
- [ ] 246
- [ ] 2468

**6) Which of the following is correct variable name in Python?**
- [ ] _a
- [ ] __1
- [x] Both are correct
- [ ] None of the above

**7) What is the output of this expression in Python, 3\*1\*\*3?**
- [x] 3
- [ ] 27
- [ ] 9
- [ ] 1

**8) State True or False.**
**Python is a case-sensitive language.**
- [x] True
- [ ] False

**9) Which of the following is not a keyword in Python?**
- [ ] yield
- [x] add
- [ ] global
- [ ] elif

**10) What would be the value of variable y if the following set of instructions are executed?**
```
x=4.5
y=int(x)
```
- [x] 4
- [ ] 5
- [ ] 4.5
- [ ] None of the above

---

## Second source: Mayank Patel

- Source: <https://www.youtube.com/watch?v=Winl2Yjoq9c> · Mayank Patel · published 2019-08-20 · `noc19_cs41`; "Your last recorded submission was on 2019-08-11, 21:18 IST"; quiz due 2019-08-21, 23:59 IST.
- **Quiz Q1–Q10: same ticks as above** (independent second submission, still no score shown).

### Programming Assignments-1: Addition

In this assignment, you will have to take two numbers (integers) as input and print the addition.

**Input Format:**
The first line of the input contains two numbers separated by a space.

**Output Format:**
Print the addition in single line

**Example:**

Input:
4 2

Output:
6

**Explanation:**
Since the addition of numbers 4 and 2 is 6, hence the output is 6.

Author's code:
```python
#A,B = raw_input().split(" ")
#A = int(A)
#B = float(B)
x, y = map(int, input().split(" "))
print(x+y)
```

### Programming Assignment-2: Small

Given two numbers (integers) as input, print the smaller number.

**Input Format:**
The first line of input contains two numbers separated by a space

**Output Format:**
Print the smaller number

**Example:**

Input:
2 3

Output:
2

Author's code:
```python
x, y = map(int, input().split())
if x<y:
  print(x)
else:
  print(y)
```

### Programming Assignment-3: Loops ,List and Sum (due 2019-08-22, 23:59 IST)

You all have seen how to write loops in python. Now is the time to implement what you have learned.

Given an array **A** of **N** numbers (integers), you have to write a program which prints the sum of the elements of array **A** with the corresponding elements of the reverse of array **A**.
If array **A** has elements **[1,2,3]**, then reverse of the array **A** will be **[3,2,1]** and the resultant array should be **[4,4,4]**.

**Input Format:**

The first line of the input contains a number N representing the number of elements in array A.
The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)

**Output Format:**

Print the resultant array elements separated by a space. (no space after the last element)

**Example:**

Input:
4
2 5 3 1

Output:
3 8 8 3

**Explanation:**
Here array A is [2,5,3,1] and reverse of this array is [1,3,5,2] and hence the resultant array is [3,8,8,3].

Author's code:
```python
r=input()
#input_string = input("Enter a list element separated by space ")
st=input()
list1  = st.split(' ')
list2  = list1.copy()
list1.reverse()
res_list = []
for i in range(0,len(list1)):
    res_list.append(int(list1[i]) + int(list2[i]))

for i in res_list:
  print(i,end=" ")
```
(The author's code prints a space after the last element, even though the statement says not to.)

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-08-21, 14:03 IST).
- Accepted answers seen: **Q1 False · Q2 0145 · Q3 19.5 · Q4 No output is displayed due to syntax error. · Q5 24 · Q6 Both are correct · Q7 3 · Q8 True.** All match the ticks above. Q9 and Q10 were not shown.

### Programming Assignments-1: Addition — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `100 100` | `200` |
| 2 | `5 10` | `15` |
| 3 | `5 12` | `17` |
| 4 | `8 4` | `12` |

Sample solutions (Provided by instructor):
```python
x,y = input().split(" ")
x = int(x)
y = int(y)

print(x+y)
```

### Programming Assignment-2: Small — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `100 10` | `10` |
| 2 | `0 1` | `0` |
| 3 | `10 9` | `9` |
| 4 | `9 6` | `6` |

Sample solutions (Provided by instructor):
```python
x,y = input().split(" ")
x = int(x)
y = int(y)

if(x<y):
    print(x)
else:
    print(y)
```

### Programming Assignment-3: Loops ,List and Sum — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `5` / `4 3 2 1 3` | `7 4 4 4 7` |
| 2 | `8` / `1 1 11 1 1 1 1 1` | `2 2 12 2 2 12 2 2` |
| 3 | `3` / `3 2 1` | `4 4 4` |
| 4 | `1` / `1` | `2` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

N = int(input())
A = [int(i) for i in input().split(" ")]
B = []
for i in range(len(A)-1, -1,-1):
    B.append(A[i])
C = []
for i in range(len(B)):
    C.append(A[i]+B[i])
for i in range(len(C)):
    if(i==len(C)-1):
        print(C[i])
    else:
        print(C[i],end=" ")
```
