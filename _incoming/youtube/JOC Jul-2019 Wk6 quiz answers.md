# JOC Jul-2019 · Week 6: Cool Ideas (Part 4) · Assignment 6

- Source: <https://www.youtube.com/watch?v=ziiT0QyNpPY> · Ultimate Gamer · published 2019-09-01
- Portal: "Your last recorded submission was on 2019-09-01, 12:10 IST"; due date cut off at the frame edge ("2019-09-1…", most likely 2019-09-11, following the weekly pattern 08-28 → 09-04) → **Jul-2019 session**
- `[x]` = option selected by the author; the page shows "Thank you for taking the Assignment 6." → submitted, but no score shown, so unverified. Video ends with "WE CAN NOT GUARANTEE THAT THESE SOLUTIONS ARE 100% CORRECT."

**1) What is the output of the following program?**
```
x = "abcdef"
i = "a"
while i in x:
        print(i, end = " ")
```
- [ ] i i i ...infinite times
- [ ] a b c d e f ...infinite times
- [ ] a b c d e f
- [x] a a a a a...infinite times

**2) Which of the following arithmetic operators can be used with strings?**
- [ ] ++
- [ ] –
- [x] +
- [ ] None of the above

**3) What is the output of the following code snippet?**
```
line = "What will have so will"
L = line.split('a')
for i in L:
    print(i, end=' ')
```
- [ ] ['What', 'will', 'have', 'so', 'will']
- [x] Wh t will h ve so will
- [ ] What will have so will
- [ ] ['Wh', 't will h', 've so will']

**4) Fill in the code to complete the following function for computing factorial:**
```
def factorial(n):
  if n == 0:
    return 1
  else:
    return .......
```
- [ ] factorial(n-1)\*n
- [ ] n\*(n-1)
- [ ] n\*factorial(n-1)
- [x] Either A or C

**5) A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward. Fill in the code to complete the following function for checking whether a string is a palindrome.**
```
def isPalindrome(s):
  if len(s) != 1:
    return True
  elif s[0] != s[-1]:
    return False
  else:
    return isPalindrome(s.substring(1, len(s) - 1))
```
- [ ] s[0] != s[-1]:
- [ ] s[0] != s[len(s)]:
- [ ] s[1] != s[len(s)-1]:
- [ ] s[1] != s[len(s)]:

> ⚠ No option is ticked here, even on the submitted page. The `elif` line in the code shown already matches option A, so the blank is that condition → **s[0] != s[-1]:**. The code is reproduced as shown, including `len(s) != 1` and `.substring`.

**6) What is the output of the following recursive function?**
```
def test(i,j):
  if(i==0):
    return j
  else:
    return test(i-1,i+j)
print(test(4,7))
```
- [x] 17
- [ ] 7
- [ ] 13
- [ ] 10

**7) What is the game strategy used in the Tic Tac Toe game?**
- [ ] Divide and Conquer
- [x] Min-Max Strategy
- [ ] Greedy Strategy
- [ ] None of the above

**8) What does the following function do?**
```
def fun(n):
  if (n == 0 or n == 1):
    return n
  if (n%3 != 0):
    return 0
  return fun(n/3)
```
- [ ] It returns 1 when n is a multiple of 3, otherwise returns 0
- [x] It returns 1 when n is a power of 3, otherwise returns 0
- [ ] It returns 0 when n is a multiple of 3, otherwise returns 1
- [ ] It returns 0 when n is a power of 3, otherwise returns 1

**9) Which of the following statements is correct regarding recursion and iteration?**
- [ ] The code size in case of recursion is smaller than that of iteration
- [ ] The time taken for execution of program in case of recursion is more than that of iteration
- [ ] Iteration is terminated through base case and recursion is terminated when the iterator condition is not satisfied
- [x] Both A and B

**10) If COMPUTER is denoted as KPDITWQC and SCIENCE is denoted as YKHQLKQ, how is SET denoted by this encoding scheme?**
- [x] YQW
- [ ] RAVP
- [ ] OXS
- [ ] FML

---

## Second source: Mayank Patel

- Source: <https://www.youtube.com/watch?v=pPzKBMCk4rk> · Mayank Patel · published 2019-09-07 · "Your last recorded submission was on 2019-09-07, 13:42 IST"; **due 2019-09-11, 23:59 IST** (confirms the due date above). Page shows "Thank you for taking the Assignment 6." (no score).
- **Quiz:** same ticks as above, and **Q5 is ticked here: `s[0] != s[-1]:`**, which matches the note above. The author also typed "Ques 5 has some p[roblem]" in Notepad over the question, presumably about the `len(s) != 1` / `.substring` errors in the given code.

### Programming Assignment-1: Computing Paradox (due 2019-09-12, 23:59 IST)

You are provided with a playlist containing **N** songs, each has a unique positive integer length. Assume you like all the songs from this playlist, but there is a song, which you like more than others.
It is named "Computing Paradox".

You decided to sort this playlist in increasing order of songs length. For example, if the lengths of the songs in the playlist were {1, 3, 5, 2, 4} after sorting it becomes {1, 2, 3, 4, 5}.
Before the sorting, "Computing Paradox" was on the **k**<sup>th</sup> position (1-indexing is assumed for the playlist) in the playlist.

Your task is to find the position of "Computing Paradox" in the sorted playlist.

**Input Format:**
The first line contains two numbers **N** denoting the number of songs in the playlist.
The second line contains **N** space separated integers **A₁, A₂, A₃,..., A_N** denoting the lengths of songs.
The third line contains an integer **k**, denoting the position of "Computing Paradox" in the initial playlist.

**Output Format:**

Output a single line containing the position of "Computing Paradox" in the sorted playlist.

**Example:**

**Input:**
4
1 3 4 2
2

**Output:**
3

**Explaination:**
N equals to 4, k equals to 2, A equals to {1, 3, 4, 2}. The answer is 3 because {1, 3, 4, 2} -> {1, 2, 3, 4}.

Author's code (private test cases 1–3: Passed):
```python
x=int(input())
A=[int(i) for i in input().split(" ")]
B = sorted(A)
k=int(input())
position=A[k-1]
if position in B:
    index=B.index(position)+1
    print(index,end=' ')
```
Sample test cases: `5 / 1 2 3 9 4 / 5` → `4`; `5 / 1 2 3 9 4 / 1` → `1`; `6 / 1 3 5 2 4 6 / 3` → `5`.

### Programming Assignment-2: Dictionary (due 2019-09-12)

Given a positive integer number **n**, you have to write a program that generates a dictionary **d** which contains **(i, i\*i\*i)** such that i is the key and **i\*i\*i** is its value, where **i** is from **1 to n (both included)**.
Then you have to just print this dictionary **d**.

Example:
Input: 4

will give output as
{1: 1, 2: 8, 3: 27, 4: 64}

**Input Format:**
Take the number **n** in a single line.

**Output Format:**
Print the dictionary **d** in a single line.

Example:

Input:
8

Output:
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}

Explanation:

Here **n** is 8, we will start from **i=1**, hence the first element of the dictionary is **(1: 1)**, as i becomes **2**, the second element of the dictionary becomes **(2: 8)** and so on.
Hence the output will be **{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}**.

Author's code (private test cases 1–3: Passed):
```python
n=int(input())
dicti={}
for i in range(n):
    dicti[i+1]=(i+1)**3
print(dicti,end=" ")
```

### Programming Assignment-3: Functions (due 2019-09-12)

Given an integer number **n**, define a function named **printDict()** which can print a dictionary where the keys are numbers between **1** and **n** (both included) and the values are square of keys.
The function **printDict()** doesn't take any argument.

Input Format:
The first line contains the number **n**.

Output Format:
Print the dictionary in one line.

Example:

Input:
5

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

NOTE: You are supposed to write the code for the function **printDict()** only. The function has already been called in the main part of the code.

Author's code (private test cases 1–3: Passed):
```python
def printDict():
    n=int(input())
    dic={}
    for i in range(n):
        dic[i+1]=(i+1)**2;
    print(dic,end=' ')
printDict()
```

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline).
- **Accepted answers seen:** Q1 a a a a a...infinite times · Q2 + · Q3 Wh t will h ve so will (selected) · Q4 Either A or C · **Q5 s[0] != s[-1]:** · Q6 17 · Q7 Min-Max Strategy · Q8 It returns 1 when n is a power of 3, otherwise returns 0 · Q9 Both A and B. Q10 YQW was selected; its result was not shown.
- **Q5:** the accepted answer is `s[0] != s[-1]:`, but the page shows "Yes, the answer is correct. **Score: 0**". The question appears to have been zero-weighted because of the broken code that Mayank noticed. Ultimate Gamer leaving it blank therefore cost nothing.

### Programming Assignment-1: Computing Paradox — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `16` / `11 22 33 21 47 37 23 14 32 2 3 1 6 45 24 16` / `1` | `5` |
| 2 | `6` / `1 2 3 4 5 7` / `6` | `6` |
| 3 | `6` / `39 45 7 24 30 32` / `3` | `1` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
key=a[k-1]
a.sort()
for i in range(len(a)):
    if key==a[i]:
        print(i+1)
        break
```

### Programming Assignment-2: Dictionary — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `12` | `{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331, 12: 1728}` |
| 2 | `15` | `{1: 1, …, 12: 1728, 13: 2197, 14: 2744, 15: 3375}` |
| 3 | `25` | `{1: 1, …, 15: 3375, 16: 4096, 17: 4913, 18: 5832, 19: 6859, 20: 8000, 21: 9261, 22: 10648, 23: 12167, 24: 13824, 25: 15625}` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i*i

print(d)
```

### Programming Assignment-3: Functions — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `16` | `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256}` |
| 2 | `6` | `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}` |
| 3 | `13` | `{1: 1, …, 12: 144, 13: 169}` |

Sample solutions (Provided by instructor):
```python
'''
Author: Descentis
'''
def printDict():
    n = int(input())
    d=dict()
    for i in range(1,n+1):
        d[i]=i**2
    print(d)
printDict()
```
