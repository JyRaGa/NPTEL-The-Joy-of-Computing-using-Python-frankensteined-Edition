# JOC Jan-2024 · Week 4: Assignment 4

- Source: <https://www.youtube.com/watch?v=0QrM-zt7bn0> · Study_Ease · published 2024-02-16
- Portal: `noc24_cs57`, due 2024-02-21, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked by the video author before submitting → unverified (video ends at "Submit Answers", no score)

**1) Select the correct statements regarding Magic Square:**
- [x] Magic Square of Order 1 is Trivial
- [ ] Sum of 2 magic squares is a magic square
- [x] Magic Square of Order 2 is not possible
- [ ] The magic constant (the sum of row/columns/diagonal elements) for a 7*7 possible magic square is 260

**2) For which of the matrices would the following code snippet return True?**

```python
def does_something(matrix):
  r = len(matrix)
  if r == 0 or r != len(matrix[0]):
    return False
  expected = sum(matrix[0])

  for row in matrix:
    if sum(row) != expected:
      return False
  for j in range(r):
    if sum(matrix[i][j] for i in range(r)) != expected:
      return False
  if sum(matrix[i][r - 1 - i] for i in range(r)) != expected:
    return False

  return True
```
- [x] Option 1
  ```
  8 1 6
  3 5 7
  4 9 2
  ```
- [x] Option 2
  ```
  2 9 4
  7 5 3
  6 1 8
  ```
- [x] Option 3
  ```
  6 1 8
  7 5 3
  2 9 4
  ```
- [x] Option 4
  ```
  2 7 6
  9 5 1
  4 3 8
  ```

**3) Suppose you want to simulate the Birthday Paradox by generating random birthdays for a group of people. Which library function would you most likely use to create random integers representing birthdays?**
- [x] random.randint()
- [ ] time.time()
- [ ] random.random()
- [ ] None of the above

**4) Which of the following are functions in the date-time module of Python?**
- [x] datetime.now ()
- [ ] datetime.present()
- [x] date.today()
- [ ] date.now()

**5) The "Masked Gun" game is a simple guessing game where the player attempts to unlock a masked gun by correctly guessing a secret 4-digit code. Arrange the steps in the correct sequence to create a Python code for a game.**
**1) Implement Game Loop:**
**- Set up a loop for the main game logic.**
**2) Display Masked Gun:**
**- Create a function to visually represent the masked gun.**
**3) Generate Secret Code**
**- Write a function to generate a random 4-digit secret code.**
**4) Provide Feedback and Manage Attempts for Guessing**
**- Display feedback based on the correctness of the guess and keep track of the number of attempts left for guessing**
**5) End Game:**
**- End the game when the player correctly guesses the code or runs out of attempts.**
**6) Validate and Compare Guess with Secret Code**
**- Check if the entered guess is a 4-digit numeric code and compare the player's guess with the generated secret code.**
**Enter your answer as a sequence without commas (NAT):**
**(Hint: Use the Logic like Guess the Movie game discussed in the lecture)**

Answer entered: `321645`

**6) To implement a magic square, we use the concept of matrices. Select all the statements that are True in this context.**
- [x] One possible Implementation of matrices is through nested lists in Python.
- [x] NumPy is one of the standard libraries associated with implementing matrices.
- [ ] Implementation of matrices is only through lists in Python.
- [ ] None of the above

**7) Consider the given dataset of 60 people born in 2000. Run your code using the given data to check the count of people whose birthdays fall exactly on a Tuesday.**

**Dataset:** (two-column table on the portal; listed here in person order)

```
Person 1:  January 4, 2000
Person 2:  February 8, 2000
Person 3:  March 14, 2000
Person 4:  April 18, 2000
Person 5:  May 23, 2000
Person 6:  June 27, 2000
Person 7:  August 1, 2000
Person 8:  September 5, 2000
Person 9:  October 10, 2000
Person 10: November 14, 2000
Person 11: January 1, 2000
Person 12: January 6, 2000
Person 13: January 11, 2000
Person 14: January 16, 2000
Person 15: February 2, 2000
Person 16: February 9, 2000
Person 17: February 19, 2000
Person 18: March 2, 2000
Person 19: March 11, 2000
Person 20: April 3, 2000
Person 21: April 18, 2000
Person 22: May 5, 2000
Person 23: May 19, 2000
Person 24: June 4, 2000
Person 25: June 22, 2000
Person 26: July 8, 2000
Person 27: July 24, 2000
Person 28: August 10, 2000
Person 29: August 27, 2000
Person 30: September 15, 2000
Person 31: October 3, 2000
Person 32: October 21, 2000
Person 33: November 6, 2000
Person 34: November 21, 2000
Person 35: December 7, 2000
Person 36: December 23, 2000
Person 37: January 8, 2000
Person 38: January 14, 2000
Person 39: February 1, 2000
Person 40: February 9, 2000
Person 41: February 18, 2000
Person 42: March 7, 2000
Person 43: March 15, 2000
Person 44: April 1, 2000
Person 45: April 11, 2000
Person 46: May 3, 2000
Person 47: May 14, 2000
Person 48: May 29, 2000
Person 49: June 11, 2000
Person 50: June 25, 2000
Person 51: July 9, 2000
Person 52: July 21, 2000
Person 53: August 2, 2000
Person 54: August 18, 2000
Person 55: September 1, 2000
Person 56: September 9, 2000
Person 57: September 21, 2000
Person 58: October 5, 2000
Person 59: October 19, 2000
Person 60: November 2, 2000
```
- [ ] 8
- [ ] 9
- [ ] 10
- [x] 11

**8) What is the output of the following snippet of code?**
**Hint:**
**1. If L = [1, 2, 3, 4, 5], then L[1: 3] is the list [2, 3]. Slicing a list is very similar to slicing a string. All the rules that you h… to list-slicing.** *(right edge cut off in the recording)*
**2. If P = [1, 2, 3] and Q = [4, 5, 6] then P + Q is the list [1, 2, 3, 4, 5, 6]. Again, list concatenation is very similar to strin…** *(right edge cut off)*

```python
L = [90, 47, 8, 18, 10, 7]
S = [L[0]]      #list containing just one element
for i in range(1,len(L)):
    flag = True
    for j in range(len(S)):
        if L[i] < S[j]:
            before_j= S[:j]#elements in S before index j
            new_j= [L[i]] #list containing just one element
            after_j=S[j:] #elements in S
                          #starting from index j
            # what is the size of S now?
            S = before_j + new_j + after_j
            # what is the size of S now?
            flag = False
            break
    if flag:
        S.append(L[i])
print(S)
```
- [ ] [90, 47, 8, 18, 10, 7]
- [ ] [7, 10, 18, 8, 47, 90]
- [x] [7, 8, 10, 18, 47, 90]
- [ ] [90, 47, 18, 10, 8, 7]

**9) What does the random. choice () function do?**
- [ ] Generates a random integer.
- [x] Selects a random element from a sequence.
- [ ] Chooses a random floating-point number.
- [ ] Generates a random Boolean value.

**10) Identify the magic squares from the following:**
- [x] Option 1
  ```
  1  14 15 4
  12 7  6  9
  8  11 10 5
  13 2  3  16
  ```
- [x] Option 2
  ```
  16 2  3  13
  5  11 10 8
  9  7  6  12
  4  14 15 1
  ```
- [ ] Option 3
  ```
  7  12 1  14
  2  13 16 3
  11 6  9  4
  15 8  5  10
  ```
- [ ] Option 4
  ```
  4  14 15 1
  9  7  6  12
  5  10 11 8
  16 2  3  13
  ```
