# JOC Jul-2019 · Week 10: Cool Ideas (Part 8) · Assignment 10

- Source: <https://www.youtube.com/watch?v=pe50ZtMkJL4> · ultimate gamer · published 2019-09-29
- Portal: "Your last recorded submission was on 2019-09-29, 13:16 IST" (the due date is cut off at the frame edge) → **Jul-2019 session** (by upload/submission date)
- `[x]` = option selected by the author; the page shows "Thank you for taking the Assignment 10." → submitted, but no score shown, so unverified.

**1) What is the relationship between RANBIR and ALIA according to the game FLAMES?**
- [ ] Love
- [x] Marriage
- [ ] Friends
- [ ] Enemy

**2) What is the output of the following program?**
```
import numpy as np
a = np.array([1,2,3,5,8])
b = np.array([0,3,4,2,1])
c=a+b
c = c*a
print (c[2])
```
- [ ] 20
- [x] 21
- [ ] 26
- [ ] 27

**3) What is the output of the statement a.size if a is a numpy array defined as a = np.array([[1,2,3],[0,1,4]])?**
- [ ] 4
- [ ] 5
- [x] 6
- [ ] 7

**4) What is the output of the following Python program?**
```
import numpy as np
a = np.array([[0, 1, 0], [1, 0, 1]])
a += 3
b=a+3
print (a[1,2] + b[1,2])
```
- [ ] 10
- [x] 11
- [ ] 12
- [ ] 13

**5) If the string s="Python" then what is the output of the statement s[::-1]?**
- [ ] "Python"
- [ ] "onthPy"
- [ ] "Pythno"
- [x] "nohtyP"

**6) State True or False.**
**numpy.asanyarray(input) converts input to an ndarray. Here, input can be scalars, lists, lists of tuples, tuples, tuples of tuple[…]** (the rest of the line is cut off at the frame edge)
- [x] True
- [ ] False

**7) Which of the following attributes is used to obtain picture size using PIL in Python?**
- [ ] shape
- [x] size
- [ ] area
- [ ] volume

**8) What is the output of the statement print(s.upper()) if s='SImRan' ?**
- [x] SIMRAN
- [ ] SIMran
- [ ] SiMrAn
- [ ] None of the above

---

## ✅ Official accepted answers and programming assignments (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-10-02, 22:43 IST).
- **Accepted answers seen:** Q1 Marriage · Q2 21 · Q3 6 · Q4 11 · Q5 "nohtyP" · Q6 True · Q7 size · Q8 SIMRAN (selected). **All ticks above are correct.** Q7's fourth option is "volume".

### Programming Assignment-1: Special Character

Given a string **S**, check whether it contains any special character or not. Print 'YES' if it does els[e 'NO' …] (cut off at the right edge)

**Input Format:**

The first line contains the string S

**Output Format:**

Print 'YES' or 'NO'

**Example:**

Input:
Hi$my*name

Output:
YES

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `123romeo hi` | `NO` |
| 2 | `This is an alpha23numeric` | `NO` |
| 3 | `@#$%` | `YES` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

import re

# Function checks if the string
# contains any special character
def run(string):

    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    if(regex.search(string) == None):
        print("NO")

    else:
        print("YES")

S = input()

run(S)
```
(Note: the space in test 1 and 2 is not treated as special.)

### Programming Assignment-2: Jumps (due 2019-10-10, 23:59 IST)

One day Ajit got a strange feeling of jumping from one point to another. The jumping will be done in one dimension only.
He will start from a point **0** and from there he will perform a lot of jumps. He can only jump in a s[pecific sequence]: **1jump, 2jump, 3jump, 1jump, 2jump, 3jump, 1jump,** and so on. (1>2>3>1>2>3>1.....)

1-jump means that if Ajit is at the point x, he will jump to the point x+1.
2-jumps mean that if Ajit is at the point x, he will jump to the point x+2.
3-jumps mean that if Ajit is at the point x, he will jump to the point x+3.

Before the start Ajit asks you: will he arrive at the point a after some number of jumps?

**Input Format:**
The first line contains a single number a denoting the point Ajit asks about.

**Output Format:**
Output "YES" without a quotes if Ajit can arrive at point a or "NO" without quotes otherwise.

Example-1:

Input:
0

Output:
YES

Explanation:
He started at point 0

Example-2:

Input:
2

Output:
NO

Explanation:
From 0 he can take 1 jump to reach point 1 but after that he can take only 2 jumps which will le[ad …] Jump sequence (1>2).

NOTE: The value of a can be as large as 10¹⁸. Please make your program efficient or you may […]

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `110011010` | `NO` |
| 2 | `178235689434` | `YES` |
| 3 | `9999999912133332` | `YES` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

x = int(input())

if((x%6==0) or (x%6==1) or (x%6==3)):
    print("YES")
else:
    print("NO")
```

### Programming Assignment-3 (title cut off): Q = √(2CD/H)

Write a program that calculates and prints the value according to the given formula:
**Q = Square root of [(2 \* C \* D)/H]**
Following are the fixed values of **C** and **H**:
**C** is 50. **H** is 30.
**D** is the variable whose values should be input to your program in a comma-separated sequenc[e …]

Input Format:
A sequence of values for D with each value separated by a comma.

Output Format:
Print the sequence of Q values with each value separated by a comma.

Example:

Input:
100,150,180

Output:
18,22,24

Private test inputs: `23,31,24,53,31` · `91,34,51,64,23,54,65,76,23,98,45,76,23,43,12` · `1,2,3,4,5,6,7,8,9,10,21,43,56,87,23,14,25,36,47,58,69,15,27,38,59,53,64,75,86,97,97…` (expected outputs not shown).

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))
```
