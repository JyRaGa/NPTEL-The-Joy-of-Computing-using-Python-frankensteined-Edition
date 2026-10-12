# JOC Jul-2019 · Week 5 · Assignment 5

- Source: <https://www.youtube.com/watch?v=hNkCUqcnwKE> · Ultimate Gamer · published 2019-08-24
- Portal: "Your last recorded submission was on 2019-08-25, 00:33 IST" (re-submitted at 00:39 in the video, same ticks); due 2019-09-04 → **Jul-2019 session**
- `[x]` = option selected by the author; the page then showed "Thank you for taking the Assignment 5." → submitted, but no score shown, so unverified. Video ends with "We can not guarantee that these solutions are 100% correct."

**1) Binary search algorithm uses**
- [ ] Linear way to search values
- [ ] Divide and conquer method
- [x] Bubble sorting technique
- [ ] None of them

> ⚠ **Official accepted answer: "Divide and conquer method"** (see the official section at the end). The tick above is wrong.

**2) The number of swaps needed to sort the numbers [8, 22, 7, 9, 31, 5, 13] in ascending order, using bubble sort is**
- [x] 10
- [ ] 11
- [ ] 12
- [ ] 13

**3) Suppose a list is [2, 9, 5, 4, 8, 1]. After the first pass of bubble sort (while sorting in ascending order), the list becomes**
- [ ] 2,9,5,4,1,8
- [ ] 2,5,9,4,8,1
- [x] 2,5,4,8,1,9
- [ ] 2,1,5,4,8,9

**4) Which of the following is TRUE in the Monty Hall game with 3 doors?**
- [ ] Number of doors containing the bumper prize is greater than number of doors containing the goat
- [x] Number of doors containing the goat is greater than number of doors containing the bumper prize
- [ ] Number of doors containing the goat is equal to the number of doors containing the bumper prize
- [ ] The player just gets one chance to choose his door

**5) Which file format is supported by Python Speech Recognition library?**
- [ ] mp3
- [x] wav
- [ ] Both A and B
- [ ] None of the above

**6) Consider the secure Rock Paper Scissors game**
```
0->Rock
1->Paper
2 ->Scissors
Player 1's input : 1000010210
Player 2's input : 1012010211
Who won?
```
- [ ] Player 1
- [ ] Player 2
- [ ] Draw
- [x] Data Insufficient

**7) In the simple Monte Hall game, we had 3 doors and 1 door contained a prize. The player has to guess which door could possibly contain the prize. That door would be opened and if it contains the prize he wins it. If more doors are added, the player has more choices to guess. What do you think will happen to the probability (i.e. chance) of winning if more doors are added?**
- [ ] Increases
- [x] Decreases
- [ ] None of the above

**8) In rock, paper, scissors game, how many combinations of choices made by the players are possible?(Rock, Paper) and (Paper, Rock) are considered different combinations.)**
- [x] 9
- [ ] 27
- [ ] 18
- [ ] 6

**9) In Rock, Paper and Scissors game, if one of the players shows Scissors then which of the following is/are TRUE?**
1. He is guaranteed to win the game if the other player shows Rock.
2. He is guaranteed to win the game if the other player does not show Rock.
3. He is guaranteed to win the game if the other player shows Paper.
4. He is guaranteed to lose the game if the other player shows Paper.

- [ ] 1 and 4
- [ ] 2,3 and 4
- [ ] 2 and 3
- [x] Only 3

**10) The average number of key comparisons done in a successful sequential search in a list of length 9 is**
- [x] 5
- [ ] 6
- [ ] 10
- [ ] 45

---

## Second source: Mayank Patel

- Source: <https://www.youtube.com/watch?v=06rPbnYBNTU> · Mayank Patel · published 2019-08-31 · "Your last recorded submission was on 2019-08-31, 09:39 IST"; quiz due 2019-09-04, 23:59 IST. Page shows "Thank you for taking the Assignment 5." (no score).
- **Quiz Q1–Q10: same ticks as above**, including Q1 "Bubble sorting technique". Both sources tick it, but it still looks wrong; see the note at Q1.

### Programming Assignment-1: Cab and walk (due 2019-09-05, 23:59 IST)

Arun is working in an office which is **N** blocks away from his house. He wants to minimize the time it takes him to go from his house to the office.
He can either take the office cab or he can walk to the office.
Arun's velocity is **V1 m/s** when he is walking. The cab moves with velocity **V2 m/s** but whenever he calls for the cab, it always starts from the office, covers **N** blocks, collects Arun and goes back to the office.
The cab crosses a total distance of **N** meters when going from office to Arun's house and vice versa, whereas Arun covers a distance of (√2 ∗ N) while walking.
Help Arun to find whether he should walk or take a cab to minimize the time.

Input Format:
A single line containing three integer numbers N, V1, and V2 separated by a space.

Output Format:
Print 'Walk' or 'Cab' accordingly

Constraints:

1<=V1, V2 <=100

1<=N<=200

Example-1:

Input:
5 10 15

(Example-1's output was not captured; another shown example: Input `2 10 14` → Output `Walk`.)

Author's code (public test cases 3/3 passed):
```python
N, V1,V2 = [int (i) for i in input().split()]
if(N*2**0.5/V1<2*N/V2):
    print("Walk",end="")
else:
    print("Cab",end="")
```
Sample test cases: `2 10 14` → `Walk`; `7 14 10` → `Walk`; `10 5 5` → `Walk`.

### Programming Assignment-2: End-Sort (due 2019-09-05)

Given a list **A** of **N** distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order.

**Input Format:**
The first line of the input contains N distinct integers of list A separated by a space.

**Output Format**
Print the minimum number of moves required to sort the elements.

Example:

Input:
1 3 2 4 5

Output:
3

**Explanation:**
In the first move, we move 3 to the end of the list. In the second move, we move 4 to the end of the list, and finally, in the third movement, we move 5 to the end.

Author's code (public test cases 3/3 passed):
```python
arr=[int(arr) for arr in input().split()]
n = len(arr)
arr1 =sorted(arr);
f=0
for i in range(n):
    if arr[i] == arr1[f]:
        f=f+1
print(n-f,end="")
```
Sample test cases: `1 2 3 4 5` → `0`; `1 3 5 2 6` → `3`; `5 1 3 2 7` → `3`.

### Programming Assignment-3: Semi Primes (due 2019-09-05)

A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3\*5 is a semiprime number but 9 = 3\*3 is not .
Given an integer number **N**, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).

**Input Format:**
The first line contains an integer N.

**Output Format:**
Print 'Yes' if it is possible to represent N as a sum of two semiprimes 'No' otherwise.

**Example:**

Input:
30

Output:
Yes

**Explanation:**
N = 30 can be expressed as 15+15 where 15 is a semi-prime number (5\*3 = 15)

NOTE: N is less than equal to 200

Author's code (public test cases 3/3 passed):
```python
p1=[]
p2=[]
sp1=[]
sp2=[]
temp=[]
n = int(input())
for i in range(2,n):
    for j in range(2,i):
        if (i%j==0):
            break;
    else:
        p1.append(i)
        p2.append(i)

for i in p1:
    for j in p2:
        if i!=j and i*j<=n:
            sp1.append(i*j)
            sp2.append(i*j)

sp1.sort()
sp2.sort()

for i in sp1:
    for j in sp2:
        if (i+j)<=n:
            if (i+j) not in temp:
                temp.append(i+j)

temp.sort()

if n in temp:
    print("No", end="")
else:
    print("Yes", end="")
```
Public test results: `45` → `Yes`; `62` → `No`; `27` → `Yes` (all Passed).

> ⚠ The final `if` looks inverted: it prints "No" when N **is** a sum of two semiprimes. It passed the three public cases, but don't rely on it as a reference solution.

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-09-04, 16:14 IST).
- **Accepted answers:** **Q1 Divide and conquer method** · Q2 10 · Q3 2,5,4,8,1,9 · Q4 Number of doors containing the goat is greater than number of doors containing the bumper prize · Q5 wav · Q6 Data Insufficient · Q7 Decreases · Q8 9 · Q9 Only 3 · Q10 5 (marked correct).
- ⚠ **Q1 is confirmed wrong in both video sources above.** They ticked "Bubble sorting technique"; the accepted answer is "Divide and conquer method". Every other tick matches.

### Programming Assignment-1: Cab and walk — examples, private test cases and instructor solution

Example-1: Input `5 10 15` → Output `Cab`. Example-2: Input `2 10 14` → Output `Walk`.

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `100 40 60` | `Cab` |
| 2 | `200 50 80` | `Cab` |
| 3 | `100 50 50` | `Walk` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
http://sccilabs.org/amit_verma.html
"""

n,v1,v2 = input().split()

n = int(n)
v1 = int(v1)
v2 = int(v2)

st_d = pow(2,1/2)*n
st_t = st_d/v1

el_d = 2*n
el_t = el_d/v2

if(st_t<el_t):
    print("Walk")
else:
    print("Cab")
```

### Programming Assignment-2: End-Sort — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `20 3 1 2 6 7 8 21 19 5` | `8` |
| 2 | `4 1 3 5 6 2 7 9 8` | `7` |
| 3 | `1 2 3 4 5 6 7 8 9 15 14 13 12 11 10` | `5` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
http://sccilabs.org/amit_verma.html
"""

arr = [int(x) for x in input().split()]
arr1 = sorted(arr)
count = 0
for i in range(len(arr)):
    if arr[i] == arr1[count]:
        count+=1
print(len(arr)-count)
```

### Programming Assignment-3: Semi Primes — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `123` | `Yes` |
| 2 | `58` | `No` |
| 3 | `158` | `Yes` |

Sample solutions (Provided by instructor; line 7 runs off the right edge of the screen):
```python
"""

@author: descentis
http://sccilabs.org/amit_verma.html
"""

li = [12, 16, 20, 21, 24, 25, 27, 28, 29, 30, 31, 32, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, …]

N = int(input())
if (N in li):
    print('Yes')
else:
    print('No')
```
(That account's own accepted submission builds the list of semiprime sums and ends with `if n in last: print("Yes", end="") else: print("No", end="")`. That is the non-inverted form of the Mayank Patel code above.)
