# JOC Jul-2019 · Week 4: Cool Ideas (Part 2) · Assignment 4

- Source: <https://www.youtube.com/watch?v=GTWvcV0gRyI> · Ultimate Gamer · published 2019-08-18
- Portal: "Your last recorded submission was on 2019-08-18, 16:10 IST"; due 2019-08-28 → **Jul-2019 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown).
- Q5's question text is cut off at the right edge of the recording; the missing words are marked `[…]`.

**1) Which of the following is a valid question that would be posed when 'Guess the Movie Name' game is played with the movie "SKYSCRAPER"?**
- [ ] S\*Y\*C\*A\*\*\*
- [ ] \*\*Y\*\*R\*\*E\*
- [x] \*\*Y\*\*\*A\*E\*
- [ ] S\*\*S\*\*A\*ER

**2) What is the output of the snippet of code shown below?**
```
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(A[1])
```
- [x] [4, 5, 6]
- [ ] [3, 6, 9]
- [ ] [1, 4, 7]
- [ ] [1, 2, 3]

**3) What is the output of the code shown?**
```
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print([A[row][1] for row in (0, 1, 2)])
```
- [ ] [4, 5, 6]
- [x] [2, 5, 8]
- [ ] [8, 4, 7]
- [ ] [8, 2, 3]

**4) What is the output of the code shown below?**
```
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print([A[i][i] for i in range(len(A))])
```
- [ ] [4, 5, 6]
- [ ] [2, 5, 8]
- [ ] [8, 4, 7]
- [x] [1, 5, 9]

**5) In "Guess the Movie Name" game, we initially have all blanks (or \*). Slowly as the person guesses a letter the question undergoes a change in s[…] corresponding letter is opened up). If the movie name is INTERSTELLER, which of the following can never be a state of the question during the run of […]**
- [x] IN\_ER\_\_ELL\_R
- [ ] INT\_R\_T\_LL\_R
- [ ] INT ER \_TELLER
- [ ] INTER\_TE\_\_ER

**6) What is the minimum number of people required to guarantee a collision in their day of birth?**
- [x] 8
- [ ] 7
- [ ] 6
- [ ] 13

**7) If there are k symbols in a Dobble game card, how many comparisons are needed at the maximum?**
- [ ] k/2
- [x] k²
- [ ] k
- [ ] 2k

**8) What is the maximum number that can be filled in 5\*5 Magic Square?**
- [ ] 9
- [ ] 15
- [x] 25
- [ ] None of the above

**9) The probability of a birth date collision in a non-leap year is**
- [x] more than that of leap year
- [ ] less than that of leap year
- [ ] same as that of leap year
- [ ] None of the above

---

## Second source: Mayank Patel

- Source: <https://www.youtube.com/watch?v=ekowaQ74hRk> · Mayank Patel · published 2019-08-20 · "Your last recorded submission was on 2019-08-20, 10:24 IST"; quiz due 2019-08-28, 23:59 IST (confirms the due date above).
- **Quiz Q1–Q9: same ticks as above.**

### Programming Assignment-1: Factorial (due 2019-08-29, 23:59 IST)

Given an integer number **n**, you have to print the factorial of this number. To know about factorial please click on this link.

**Input Format:**

A number **n**.

Output Format:

Print the factorial of **n**.

**Example:**

Input:
4

Output:
24

Author's code:
```python
n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f,end='')
```

### Programming Assignment-2: Matrix (due 2019-08-29, 23:59 IST)

You are provided with the number of rows (R) and columns (C). Your task is to generate the matrix having R rows and C columns such that all the numbers are in increasing order starting from 1 in row wise manner.

Input Format:
The first line contain two numbers R and C separated by a space.

Output Format:
Print the elements of the matrix with each row in a new line and elements of each row are separated by a space.

NOTE: There should not be any space after the last element of each row and no new line after the last row.

Example:

Input:
3 3

Output:
1 2 3
4 5 6
7 8 9

Explanation:
Starting from the first row, the numbers are present in the increasing order. Since it's a 3X3 matrix, the numbers are from 1 to 9.

Author's code:
```python
#input 3 6
a=[int(n) for n in input().split()]

matrix = [[i*a[1]+j+1 for j in range(a[1])] for i in range(a[0])]
for m in matrix:
    print(*m)
```
Sample test cases: `2 3` → `1 2 3 / 4 5 6`; `3 2` → `1 2 / 3 4 / 5 6`; `3 4` → `1 2 3 4 / 5 6 7 8 / 9 10 11 12`.

### Programming Assignment-3: The power of Randomness (due 2019-08-29, 23:59 IST)

You all have used the random library of python. You have seen in the screen-cast of how powerful it is.
In this assignment, you will sort a list let's say **list_1** of numbers in increasing order using the random library.

Following are the steps to sort the numbers using the random library.

**Step 1**: Import the randint definition of the **random** library of python. Check this page if you want some help.

**Step 2**: Take the elements of the **list_1** as input.

**Step 3**: randomly choose two indexes **i** and **j** within the range of the size of **list_1**.

**Step 4**: Swap the elements present at the indexes i and j. After doing this, check whether the **list_1** is **sorted or not**.

**Step 5**: Repeat step **3** and **4** until the array is **not sorted**.

**Input Format:**
The first line contains a single number **n** which signifies the number of elements in the **list_1**.
From the second line, the elements of the **list_1** are given with each number in a new line.

**Output Format:**
Print the elements of the **list_1** in a single line with each element separated by a space.
NOTE 1: There should **not** be any space after the last element.

Example:

Input:
4
3
1
2
5

Output:
1 2 3 5

Explanation:
The first line of the input is **4**. Which means that **n** is 4, or the number of elements in **list_1** is 4. The elements of **list_1** are **3, 1, 2, 5** in this order.
The sorted version of this list is **1 2 3 5**, which is the output.

NOTE 2: There are many ways to sort the elements of a list. The purpose of this assignment is to show the power of randomness, and obviously it's fun.

Author's code (a selection sort, which ignores the randomness requirement):
```python
import random
n=int(input())
list_1 = []
for i in range(n):
    list_1.append(int (input()))
list_2=[]
while list_1:
    minimum = list_1[0]
    for x in list_1:
        if x < minimum:
            minimum = x
    list_2.append(minimum)
    list_1.remove(minimum)
sarr = [str(a) for a in list_2]
print(' '.join(sarr))
```

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-08-27, 10:54 IST).
- **Accepted answers seen:** Q1 \*\*Y\*\*\*A\*E\* · Q2 [4, 5, 6] · Q3 [2, 5, 8] · Q4 [1, 5, 9] · Q5 IN\_ER\_\_ELL\_R · Q6 8 · Q7 k². These match the ticks above. Q8 (25 selected, marked correct) and Q9 were not fully shown.

### Programming Assignment-1: Factorial — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `8` | `40320` |
| 2 | `7` | `5040` |
| 3 | `10` | `3628800` |

Sample solutions (Provided by instructor):
```python
"""
Created on Fri Aug 17 10:04:41 2018

@author: descentis
http://sccilabs.org/amit_verma.html
"""

k = int(input())

fac = 1
for i in range(1,k+1):
    if(k==0):
        break
    fac=fac*i

print(fac)
```

### Programming Assignment-2: Matrix — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `4 4` | `1 2 3 4` / `5 6 7 8` / `9 10 11 12` / `13 14 15 16` |
| 2 | `5 5` | `1 2 3 4 5` / `6 7 8 9 10` / … / `21 22 23 24 25` |
| 3 | (cut off) | `1 2 3 4 5 6 7 8 9 10` / `11 … 20` / `21 … 30` / `31 … 40` … |

Sample solutions (Provided by instructor; lines after 24 not shown):
```python
"""
Created on Thu Aug 16 19:41:30 2018

http://sccilabs.org/amit_verma.html
@author: descentis
"""

a,b=map(int,input().split())

count=1
m = []
for i in range(1,a+1):
    l = []
    for j in range(1,b+1):
        l.append(count)
        count+=1
    m.append(l)

for i in range(a):
    for j in range(b):
        if(j==b-1):
            print(m[i][j], end="")
        else:
            print(m[i][j], end=" ")
    # … (rest not shown)
```

### Programming Assignment-3: The power of Randomness — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `6` / `6` / `4` / `3` / `2` / `1` / `1` | `1 1 2 3 4 6` |
| 2 | `5` / `5` / `4` / `3` / … | `1 2 3 4 5` |

Sample solutions (Provided by instructor; lines after 25 not shown):
```python
"""
Created on Fri Aug 17 16:04:10 2018

@author: descentis
http://sccilabs.org/amit_verma.html
"""

from random import randint
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

sorted = True

while(sorted):
    j = randint(0,n-1)
    i = randint(0,n-1)
    arr[i],arr[j] = arr[j],arr[i]
    for k in range(0,n-1):
        if (arr[k] > arr[k+1]):
            sorted = False

    if(sorted):
    # … (rest not shown)
```
