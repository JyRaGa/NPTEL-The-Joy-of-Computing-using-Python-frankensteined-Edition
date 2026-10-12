# JOC Jan-2019 · Week 3: Cool Ideas (Part 1) · Assignment 3

- Source: <https://www.youtube.com/watch?v=a5npNQeqw24> · Ultimate Gamer · published 2019-02-16
- Portal: "Due date for this assignment: 2019-02-20, 23:59 IST."; "Your last recorded submission was on 2019-02-16, 21:33 IST" → **Jan-2019 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown). Video ends with "We can not guarantee that these (quiz assignment) solutions are 100% correct."

**1) If the list t = [2, 5, 7, 9, 10, 11, 12], what will be the output of the statement t[2:4]?**
- [ ] [7,10]
- [ ] [7,9,10]
- [x] [7,9]
- [ ] [5,7,9]

**2) If the word in your mind is SIT, in how many ways can you pose the jumbled question?**
- [ ] 5
- [x] 6
- [ ] 7
- [ ] 3

> ⚠ Doubtful: the jumbled question should not be the word itself, so it is 3! − 1 = **5**. The same channel ticked 5 for the identical "HIT" question in Jul-2019 Week 3.

**3) What does the count method return when applied on a list?**
- [x] It returns the number of occurrences of an element in a list.
- [ ] It returns the number of elements present in the list.
- [ ] It returns the index of last element of the list.
- [ ] None of the above

**4) In the game FizzBuzz, what should be the output for the number 105?**
- [ ] Fizz
- [ ] Buzz
- [x] FizzBuzz
- [ ] Either A or B

**5) Which of the following libraries is used to create 2D graphs in Python?**
- [x] Matplotlib
- [ ] Plot
- [ ] Plotting
- [ ] Plotgraph

**6) What will be the output of the following Python program?**
```
numbers=["one","two","three"]
for each in numbers:
        print(each)
```
- [ ] one<br>three<br>two
- [ ] one
- [ ] one<br>two
- [x] one<br>two<br>three

**7) What does the function random.randrange(50,100) return in Python?**
- [ ] It returns a random number from 51 to 99.
- [ ] It returns a random number from 51 to 100.
- [x] It returns a random number from 50 to 99.
- [ ] It returns a random number from 50 to 100.

**8) How is trimmed mean calculated?**
- [ ] Sort the values then remove top 10% or bottom 10% of the values
- [x] Sort the values then remove top 10% and bottom 10% of the values
- [ ] Sort the values then remove top 10% of the values
- [ ] Sort the values then remove bottom 10% of the values

**9) Which of the following can be an output of random.randint(1,1000) but can never be an output of random.randrange(1,1000) ?**
- [x] 1
- [ ] 0
- [ ] -1
- [ ] 1000

> ⚠ Tick looks wrong: `randint(1,1000)` includes 1000, while `randrange(1,1000)` stops at 999 → **1000**. Both can return 1.

---

## Programming assignments (Week 3)

- Source: <https://www.youtube.com/watch?v=tL9Zap17_IE> · Ultimate Gamer · published 2019-02-12 · `noc19_cs09` (visible in the URL bar). Due 2019-02-21, 23:59 IST.
- **Verified:** after submission each assignment shows a pass count ("4 out of 4 tests passed" for PA1, "3 out of 3 tests passed" for PA2 and PA3), and PA1 and PA2 also show "You scored 100.0/100".

### Programming Assignment-1 (Max and Min; title not captured)

(Only the end of the statement was captured.)

**Output Format:**

Print maximum and minimum separated by a space

Example:

Input:

1 2 3 4 5

Output:

5 1

Author's code (4 out of 4 tests passed, 100/100):
```python
x=[int(i) for i in input().split()]
print(max(x),min(x)).split()
```
(Prints the right answer, then crashes on `None.split()`; the grader still passed it. Jul-2019's version of this assignment asks for the **second** max/min instead.)

### Programming Assignment-2: Multiple of 3 (due 2019-02-21, 23:59 IST)

Given a list **A** of numbers, you have to print those numbers which are **not multiples** of 3.

**Input Format:**

The first line contains the numbers of list A separated by a space.

**Output Format:**

Print the numbers in a single line separated by a space which are not multiples of 3.

Example:

Input:

1 2 3 4 5 6

Output:

1 2 4 5

Explanation:
Here the elements of A are 1,2,3,4,5,6 and since 3,6 are the multiples of 3 hence after removing them the list becomes 1,2,4,5.

Author's code (3 out of 3 tests passed, 100/100):
```python
x=[int(i) for i in input().split()]
for j in x:
  if(j%3!=0):
    print(j,end=" ")
```

### Programming Assignment-3 (Digits; same statement as Jul-2019 Week 3 PA-3)

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

Author's code (3 out of 3 tests passed):
```python
x=input("")
l=[]
for i in x:
    l.append(i)
c0=l.count('0')
c1=l.count('1')
if(c0==1 or c1==1):
    print("YES")
else:
    print("NO")
```
Sample test cases: `10` → `YES`; `1011` → `YES`; `0011` → `NO`.
