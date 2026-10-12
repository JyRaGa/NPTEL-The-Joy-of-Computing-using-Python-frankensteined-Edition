# JOC Jul-2019 · Week 7 · Assignment 7

- Source: <https://www.youtube.com/watch?v=rL6sr4bLjzs> · Ultimate Gamer · published 2019-09-07
- Portal: "Your last recorded submission was on 2019-09-07, 19:02 IST" (the due date is outside the zoomed recording) → **Jul-2019 session** (by upload/submission date)
- `[x]` = option selected by the author; the page shows "Thank you for taking the Assignment 7." → submitted, but no score shown, so unverified. Video ends with "WE CAN NOT GUARANTEE THAT THESE SOLUTIONS ARE 100% CORRECT."

**1) In the function gmplot.GoogleMapPlotter(a, b, c), what are a, b and c?**
- [x] Latitude, Longitude, Zoom level
- [ ] Zoom Level, Latitude, Longitude
- [ ] x-coordinate of map, y-coordinate of map, zoom level
- [ ] zoom level, x-coordinate of map, y-coordinate of map

**2) What is the output shape of the program?**
```
import turtle
t=turtle.Pen()
for i in range(4):
        t.forward(60)
        t.left(90)
```
- [ ] Triangle
- [ ] Trapezium
- [x] Square
- [ ] Circle

**3) What is the output of following code snippet?**
```
from PIL import Image
im = Image.open("bride.jpg")
im.rotate(45).show()
```
- [x] Open, rotate, and display the image.
- [ ] Save the rotated image
- [ ] Open, display, rotate and display the rotated image
- [ ] None of the above

**4) State True or False**
**Turtle programming is same as that performed in Logo**
- [x] True
- [ ] False

**5) What is the output shape of the following program?**
```
import turtle
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
```
- [ ] Triangle
- [ ] Trapezium
- [ ] Square
- [x] Hexagon

**6) What is the correct sequence of cells in a 5\*5 matrix that should be displayed for spiral traversing animation?**
- [ ] (1,2), (2,2), (3,5), (5,5), (4,5)
- [x] (1,1), (1,2), (1,3), (1,4), (2,4)
- [ ] (1,5), (2,5), (3,5), (5,5), (4,5)
- [ ] (2,3), (2,4), (2,5), (1,5), (3,5)

> ✅ **Official accepted answer: `(1,1), (1,2), (1,3), (1,4), (2,4)`**, the ticked option (see the official section below). My earlier "doubtful" note was wrong. The course's spiral animation evidently uses this ordering, even though a textbook 5×5 spiral would continue to (1,5).

**7) Which of the following scenarios is considered as a win in snakes and ladders?**
- [ ] When one of the players climbs up a ladder, it is considered as a win.
- [ ] When one of the players rolls a six, it is considered as a win.
- [x] When one of the players reaches last cell, it is considered as a win.
- [ ] None of the above

**8) Which of the following statements is true about PIL?**
- [ ] PIL stands for Python Imaging Library.
- [ ] PIL is used to load images with different formats.
- [ ] PIL is used to manipulate images with different formats.
- [x] All of the above

---

## Second source: Mayank Patel

- Source: <https://www.youtube.com/watch?v=HE-C6h1HtOU> · Mayank Patel · published 2019-09-10 · "Your last recorded submission was on 2019-09-09, 11:07 IST"; **quiz due 2019-09-18, 23:59 IST** (fills the missing due date above).
- **Quiz Q1–Q8: same ticks as above**, including the doubtful Q6 `(1,1), (1,2), (1,3), (1,4), (2,4)`.

### Programming Assignment-1: Lower Triangular Matrix (due 2019-09-19, 23:59 IST)

A **Lower triangular matrix** is a **square matrix** (where the number of rows and columns are equal) where all the elements above the diagonal are zero.
For example, the following is an upper triangular matrix with the number of rows and columns equal to 3.

1 0 0
4 5 0
7 8 9

Write a program to convert a square matrix into a lower triangular matrix.

**Input Format:**
The first line of the input contains an integer number **n** which represents the number of rows and the number of columns.
From the second line, take **n** lines input with each line containing **n integer** elements. Elements are separated by space.

**Output format:**
Print the elements of the matrix with each row in a new line and each element separated by a space.

Example 1:

Input:
3
1 2 3
4 5 6
7 8 9

(The rest of Example 1 and Example 2 were scrolled past; only the tail of Example 2's output, `… 32 1 4 0 / 1 2 10 9`, was visible.)

Explanation:
In both the examples, elements which are above the diagonal are zero.

**NOTE: There should not be any extra space after the elements of the last column and no extra newline after the last row of the matrix.**

Author's code:
```python
n=int(input())
l=[]
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        l.append(temp)

for i in range(n):
    for j in range (n):
        if i<j:
            if j==n-1:
                print(0,end="")
            else:
                print(0,end=" ")
        else:
            if j==n-1:
                print(l[i][j],end="")
            else:
                print(l[i][j],end=" ")

    if i!=n-1:
        print()
```

### Programming Assignment-2: Symmetric (due 2019-09-19, 23:59 IST)

Given a square matrix of N rows and columns, find out whether it is symmetric or not.

**Input Format:**
The first line of the input contains an integer number **n** which represents the number of rows and the number of columns.
From the second line, take **n** lines input with each line containing **n integer** elements with each element separated by a space.

**Output Format:**
Print 'YES' if it is symmetric otherwise 'NO'

Example:

Input:
2
1 2
2 1

Output:
YES

Author's code (private test cases 1–3: Passed):
```python
n=int(input())
l=[]
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        l.append(temp)
x=0
for i in range(n):
    for j in range(n):
        if l[i][j]!=l[j][i]:
            x=x+1
if x==0:
    print("YES",end="")
else:
    print("NO",end="")
```
Sample test cases: `2 / 1 2 / 2 1` → `YES`; `3 / 1 2 3 / 4 5 6 / 7 8 9` → `NO`; `2 / 1 2 / 2 3` → `YES`.

### Programming Assignment-3: Binary Matrix (due 2019-09-19)

Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix. A binary matrix is a matrix in which all the elements are either 0 or 1.

**Input Format:**
The first line of the input contains two integer number **N** and **M** which represents the number of rows and the number of columns respectively, separated by a space.
From the second line, take **N** lines input with each line containing **M** integer elements with each element separated by a space.

**Output Format:**
Print 'YES' or 'NO' accordingly

Example:

Input:
3 3
1 0 0
0 0 1
1 1 0

Output:
YES

Author's code:
```python
n,m=map(int,input().split())
b=0
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        for k in temp:
            if k!=0 and k!=1:
                b=b+1
                break
if b==0:
    print("YES",end="")
else:
    print("NO",end="")
```

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-09-18, 21:46 IST).
- **Accepted answers seen:** Q1 Latitude, Longitude, Zoom level · Q2 Square · Q3 Open, rotate, and display the image. · Q4 True · Q5 Hexagon · **Q6 (1,1), (1,2), (1,3), (1,4), (2,4)** · Q7 When one of the players reaches last cell (marked correct). Q8 was not shown. All ticks above are correct.

### Programming Assignment-1: Lower Triangular Matrix — full examples, private test case and instructor solution

Example 1 Output:
1 0 0
4 5 0
7 8 9

Example 2:

Input:
4
12 2 5 6
10 11 4 1
32 1 4 10
1 2 10 9

Output:
12 0 0 0
10 11 0 0
32 1 4 0
1 2 10 9

Private test case 1:
```
7
16 9 16 15 7 42 47
17 39 14 28 48 4 1
29 36 5 13 13 45 50
34 34 13 18 20 27 41
37 23 16 24 32 35 19
28 13 40 1 29 36 50
37 22 42 22 43 40 48
```
Expected output:
```
16 0 0 0 0 0 0
17 39 0 0 0 0 0
29 36 5 0 0 0 0
34 34 13 18 0 0 0
37 23 16 24 32 0 0
28 13 40 1 29 36 0
37 22 42 22 43 40 48
```

Sample solutions (Provided by instructor):
```python
"""

@author: descentis

"""


a = int(input())


m = []
for i in range(1,a+1):
    l = list(map(int, input ().split ()))
    m.append(l)

for i in range(a):
    for j in range(a):
        if(i>=j):
            if(j==a-1):
                print(m[i][j], end="")
            else:
                print(m[i][j], end=" ")
        else:
            if(j==a-1):
                print(0, end="")
            else:
                print(0, end=" ")
    if(i!=a-1):
        print()
```

### Programming Assignment-2: Symmetric — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `3` / `5 6 7` / `6 3 2` / `7 2 1` | `YES` |
| 2 | `1` / `1` | `YES` |
| 3 | `3` / `1 3 2` / `2 3 1` / `1 2 2` | `NO` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True


a = int(input())


m = []
for i in range(1,a+1):
    l = list(map(int, input ().split ()))
    m.append(l)
if (isSymmetric(m, a)):
    print("YES")
else:
    print("NO")
```

### Programming Assignment-3: Binary Matrix — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `5 3` / `1 2 3` / `4 5 6` / `7 8 9` / `1 0 0` / `1 1 1` | `NO` |
| 2 | `4 6` / `1 1 0 0 1 1` / `1 1 1 1 1 1` / `0 0 0 0 1 0` / `1 0 1 0 1 0` | `YES` |
| 3 | `1 1` / `0` | `YES` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

def isBinaryMatrix(mat,M,N):
    for i in range(M):
        for j in range(N):
            # Returns false if element
            # is other than 0 or 1.
            if ((mat[i][j] == 0 or mat[i][j] == 1)==False):
                return False;

    # Returns true if all the
    # elements are either 0 or 1.
    return True;

a,b=map(int,input().split())


m = []
for i in range(1,a+1):
    l = list(map(int, input ().split ()))
    m.append(l)
if (isBinaryMatrix(m,a,b)):
    print("YES")
else:
    print("NO")
```
