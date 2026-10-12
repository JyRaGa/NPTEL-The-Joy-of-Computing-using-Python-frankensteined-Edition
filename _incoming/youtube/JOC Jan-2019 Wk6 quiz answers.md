# JOC Jan-2019 · Week 6 · Assignment 6

- Source: <https://www.youtube.com/watch?v=lhU22sV37eU> · Ultimate Gamer · published 2019-03-09
- Portal: "Due date for this assignment: 2019-03-13, 23:59 IST."; "Your last recorded submission was on 2019-03-09, 22:34 IST" → **Jan-2019 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown). Video ends with "…CAN NOT GUARANTEE THAT THESE …NS ARE 100% CORRECT." Alternate videos for this week (not transcribed): Study Fun `dCSDSizxSFU`, Amanpal Singh `Z_FSSXm7zcU`.

**1) Complete the following recursive function for calculating the factorial of a number.**
```
def fact(num):
     if(num==0):
          return 1
     else:
          return _________
```
- [ ] fact(num-1)
- [ ] num\*fact(num)
- [x] num\*fact(num-1)
- [ ] (num-1)\*fact(num)

**2) What is the output of the following recursive function?**
```
def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)
print(test(4,7))
```
- [ ] 13
- [ ] 7
- [x] 17
- [ ] 10

**3) State True or False.**
**Recursion and iteration are similar programming techniques.**
- [ ] True
- [x] False

**4) Which of the following statements is true?**
- [ ] Both Caesar cipher and Substitution cipher are the same
- [ ] Caesar and Substitution cipher are totally unrelated
- [x] Caesar cipher is a special case of Substitution cipher
- [ ] Substitution cipher is a special case of Caesar cipher

**5) If AMIT is encoded as ZLHS and SIMRAN is encoded as RHLQZM, then how would SOUJANYA be encoded as?**
- [ ] RNTIZGFD
- [ ] RTNIZMXZ
- [ ] RTNIZMZX
- [x] RNTIZMXZ

**6) What is a Cipher?**
- [x] An algorithm for performing encryption and decryption.
- [ ] An encrypted message
- [ ] Both A and B
- [ ] None of the above

**7) How many winning configurations are possible for a player in the Tic Tac Toe game?**
- [ ] 2
- [ ] 4
- [ ] 6
- [x] 8

**8) What is the game strategy used in the Tic Tac Toe game?**
- [ ] Divide and Conquer
- [x] Min-Max Strategy
- [ ] Greedy Strategy
- [ ] None of the above

**9) Which of these statements is true?**
- [ ] Recursion can solve a few problems which Iteration cannot.
- [ ] Iteration can solve a few problems which Recursion cannot.
- [x] Anything that Recursion can solve can be solved by Iteration.
- [ ] Recursion and Iteration are totally unrelated.


---

## Second source and programming assignments: Amanpal Singh

- Source: <https://www.youtube.com/watch?v=Z_FSSXm7zcU> · Amanpal Singh · published 2019-03 ("Joy of computing using Python Assignment 6 March 2019") · a 79-second time-lapse screen recording; the quiz page is at the very end.
- Quiz page: "Due date for this assignment: 2019-03-13, 23:59 IST."; "Your last recorded submission was on 2019-03-06, 14:07 IST". The "Submit Answers" button is still showing, so these ticks are not yet resubmitted and no score is shown.
- **Quiz Q1–Q9: same ticks as Ultimate Gamer, except Q6.** Amanpal ticked **"An encrypted message"**, which looks wrong; the other source's tick, "An algorithm for performing encryption and decryption.", is the sensible answer to "What is a Cipher?".
  - Q1 `num*fact(num-1)` · Q2 17 · Q3 False · Q4 Caesar cipher is a special case of Substitution cipher · Q5 RNTIZMXZ · Q7 8 · Q8 Min-Max Strategy · Q9 Anything that Recursion can solve can be solved by Iteration.

### Programming Assignment-1: Computing Paradox

Same task as in Jul-2019 Week 6 (position of the k-th song after sorting). The statement scrolls past too fast to read in this video, but the example is shown: Input `4` / `1 3 4 2` / `2` → Output `3` (N = 4, k = 2, A = {1, 3, 4, 2}).

Author's code (the video shows no score for this one):
```python
x=input()

arr = [int(i) for i in input().split()]
#1 5 9 8 6 2 4 7

l=len(arr)

pos=input()
pos=int(pos)
item=arr[pos-1]
#print(item)
#print(arr)
arr.sort()
#print(arr)
for i in range(l):
    if(arr[i]==item):
        print(i+1)
#print(arr[item-1],end="")
```
The first input line (the count) is read and ignored. Because the song lengths are unique, `arr[i]==item` matches once.

### Programming Assignment-2: Dictionary: ⚠ differs from Jul-2019

In the Jan-2019 run the dictionary holds **squares**, not cubes (the Jul-2019 statement uses i\*i\*i).

Example: Input `8` → Output `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}`. Explanation: "Here n is 8, we will start from i=1, hence the first element of the dictionary [is (1: 1) and the second] the dictionary becomes (2: 4) and so on. Hence the output will be {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, …".

The editor's note reads "You are supposed to write the code for the function printDict … main part of the code."

| Sample test | Input | Output |
|---|---|---|
| 1 | `3` | `{1: 1, 2: 4, 3: 9}` |
| 2 | `4` | `{1: 1, 2: 4, 3: 9, 4: 16}` |
| 3 | `5` | `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}` |

Author's code (**3 out of 3 tests passed, 100.0/100**; the editor shows `printDict()` as the fixed last line, line 10):
```python
def printDict():
    x = {}
    i=input()
    i=int(i)
    for l in range(1,i+1):
    #print(i)
    #print(i*i)
        x.update({l:l*l})
    print (x)
printDict()
```
(The leading comment lines are shown at the `for` indentation in the portal editor; in a pasted copy they sit at column 0, which Python ignores.)

### Programming Assignment-3: Functions

The video only shows the page title while it loads; the statement and code were not captured.
