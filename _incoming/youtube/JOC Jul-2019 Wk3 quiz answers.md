# JOC Jul-2019 · Week 3: Cool Ideas (Part 1) · Assignment 3

- Source: <https://www.youtube.com/watch?v=o624TIuBud8> · Ultimate Gamer · published 2019-08-09
- Portal: `noc19_cs41` (visible in the URL bar); "Your last recorded submission was on 2019-08-09, 21:30 IST"; due 2019-08-21, 23:59 IST → **Jul-2019 session**
- `[x]` = option selected by the author; the page then showed "Thank you for taking the Assignment 3." → submitted, but no score shown, so unverified. Video ends with "We can not guarantee that these solutions are 100% correct."

**1) What will be the output of following program?**
```
numbers = [1, 2, 3, 4]
numbers.append([5,6,7,8])
print(len(numbers))
```
- [ ] 4
- [x] 5
- [ ] 8
- [ ] 12

**2) What will be displayed by the following code?**
```
list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)
```
- [x] [4,3]
- [ ] [1,3]
- [ ] [1,4]
- [ ] [1,2,3]

**3) What does the function random.randrange(49,150) return in Python?**
- [ ] It returns a random number from 49 to 150
- [x] It returns a random number from 49 to 149
- [ ] It returns a random number from 50 to 150
- [ ] It returns a random number from 50 to 149

**4) Which of the following options is the possible outcome of the function shown below?**

random.randrange(1,100,10)
- [ ] 22
- [ ] 9
- [ ] 101
- [x] 91

**5) What can be the output of the following code snippet?**
```
list = [55, 66, 77, 88, 99]
print(random.choice(list))
```
- [ ] 100
- [ ] 99
- [ ] 55
- [x] Either B or C

**6) If the word in your mind is HIT, in how many ways can you pose the jumbled question?**
- [x] 5
- [ ] 6
- [ ] 7
- [ ] 8

**7) How is trimmed mean calculated?**
- [ ] Sort the values then remove top 10% or bottom 10% of the values
- [x] Sort the values then remove top 10% and bottom 10% of the values
- [ ] Sort the values then remove top 10% of the values
- [ ] Sort the values then remove bottom 10% of the values

**8) State True or False.**
**Matplotlib in Python can only generate line graphs.**
- [ ] True
- [x] False

**9) What is the output of the following matplotlib program?**
```
from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
plt.plot(x,y)
plt.show()
```
- [x] A straight line
- [ ] A parabola
- [ ] A zig-zag pattern
- [ ] None of the above

---

## Second source: Mayank Patel

- Source: <https://www.youtube.com/watch?v=66kRPAjaOB8> · Mayank Patel · published 2019-08-20 · "Your last recorded submission was on 2019-08-19, 10:55 IST"; quiz due 2019-08-21, 23:59 IST.
- **Quiz:** same ticks as above **except Q6 (HIT jumbled question): Mayank ticked 6, Ultimate Gamer ticked 5.** The two sources disagree. 5 (= 3! − 1, excluding the word itself) is the usual answer for this course; Jan-2019 Wk3 had the same question with SIT.

### Programming Assignment-1: Max and Min (due 2019-08-22, 23:59 IST)

Given a list of numbers (integers), find **second maximum** and **second minimum** in this list.

**Input Format:**

The first line contains numbers separated by a space.

**Output Format:**

Print second maximum and second minimum separated by a space

Example:

Input:

1 2 3 4 5

Output:

4 2

Author's code:
```python
st=input()
list1  = [int(x) for x in st.split(' ')]
length = len(list1)
list2=sorted(list1)
print(list2[length-2],list2[1],end='')
```
Sample test cases (partly visible): `2 3 4 5 6` → `5 3`; `1 3 5 7` → `5 3`.

### Programming Assignment-2 (title and first lines not captured)

**Output Format:**

Print the numbers in a single line separated by a space which are not multiples of 5.

Example:

Input:

1 2 3 4 5 6 5

Output:

1 2 3 4 6

Explanation:
Here the elements of A are 1,2,3,4,5,6,5 and since 5 is the multiple of 5, after removing them the list becomes 1,2,3,4,6.

Author's code:
```python
x = input()
num = list(map(int, x.split()))
l =[]
for i in num:
    if i%5 != 0:
        l.append(i)
print(*l, sep = " ")
```
Sample test cases: `2 3 4 5 6` → `2 3 4 6`; `21 47 32 43` → `21 47 32 43`; `8 9 6 5 3` → `8 9 6 3`.

### Programming Assignment-3: Digits (due 2019-08-22, 23:59 IST)

You are given a number **A** which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the digits same by just flipping one digit then print '**YES**' else print '**NO**'.

**Input Format:**

The first line contains a number made up of 0's and 1's.

**Output Format:**

Print 'YES' or 'NO' accordingly without quotes.

Example:

Input:

101

Output:
YES

Explanation:
If you flip the middle digit from 0 to 1 then all the digits will become same. Hence output is YES.

Author's code:
```python
str=input()
zeros = 0
ones = 0

# Traverse through given string and
# count numbers of 0's and 1's
for i in range(0, len(str)):
    ch = str[i];
    if (ch == '0'):
        zeros = zeros + 1
    else:
        ones = ones + 1

if(zeros == 1 or ones == 1):
    print("YES",end='')
else:
    print("NO",end='')
```

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline).
- **Accepted answers:** Q1 5 · Q2 [4,3] · Q3 It returns a random number from 49 to 149 · Q4 91 · Q5 Either B or C · **Q6 5** · Q7 Sort the values then remove top 10% and bottom 10% of the values · **Q8 False** · Q9 A straight line.
- All Ultimate Gamer ticks above are correct. **The Q6 disagreement is settled: the accepted answer is 5, so Mayank's 6 is wrong.**

### Programming Assignment-1: Max and Min — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `10 10` | `10 10` |
| 2 | `1 1 1 1` | `1 1` |
| 3 | `1 2 3 4 5 6 7 8` | `7 2` |
| 4 | `1 2` | `1 2` |

Sample solutions (Provided by instructor):
```python
"""
Created on Sat Dec 15 19:56:01 2018

@author: descentis
# for any question, please contact me
http://sccilabs.org/amit_verma.html

"""

a = [int(x) for x in input().split()]

a.sort() #this command sorts the list in ascending order

print(a[-2],a[1])
```

### Programming Assignment-2: Multiple of 5 (title confirmed) — private test cases and instructor solution

Given a list **A** of numbers (integers), you have to print those numbers which are **not multiples** of 5.

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `87 34 12 90 34 23 98 67 12 23` | `87 34 12 34 23 98 67 12 23` |
| 2 | `23 87 56 34 12 61 58 64 29 98 2 16 2 6 9` | `23 87 56 34 12 61 58 64 29 98 2 16 2 6 9` |
| 3 | `1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19` | `1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19` |

Sample solutions (Provided by instructor):
```python
"""
Created on Mon Dec 17 09:56:52 2018

# for any question, contact me
@author: descentis
http://sccilabs.org/amit_verma.html
"""

a = [int(x) for x in input().split()]

b = []

for i in a:
    if(i%5!=0):
        b.append(i)

for i in range(len(b)):
    if(i==len(b)-1):
        print(b[i],end="")
    else:
        print(b[i],end=" ")
```

### Programming Assignment-3: Digits — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `11` | `NO` |
| 2 | `10` | `YES` |
| 3 | `0` | `YES` |

Sample solutions (Provided by instructor):
```python
"""
Created on Mon Dec 17 11:18:04 2018

@author: descentis
http://sccilabs.org/amit_verma.html
"""

A = input()
ls = []
li = str(A)
for j in li:
    ls.append(int(j))
count_z = 0
count_o = 0
for k in ls:
    if(k==1):
        count_o += 1
    if(k==0):
        count_z += 1

if((count_o == 1) or (count_z == 1)):
    print("YES")

else:
    if((count_o == 0) or (count_z == 0)):
        print("NO")
    else:
        print("NO")
```
