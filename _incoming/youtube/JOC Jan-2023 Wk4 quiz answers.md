# JOC Jan-2023 · Week 4: Assignment 4

- Source: <https://www.youtube.com/watch?v=WRc7yMIHkI4> · Techies Talk · published 2023-02-12
- Portal: `noc23_cs20`, due 2023-02-22, 23:59 IST → **Jan-2023 session**
- `[x]` = option ticked by the video author → unverified

**1) Which of the following statements are true with regards to magic square?**
- [x] The sum of each row should be m.
- [x] The sum of each column should be m.
- [x] The sum of each diagonal should be m.
- [ ] None of the above.

**2) Which of the following statements hold true about N in the magic square? N denotes the number of rows and columns in the square.**
- [ ] N should be even.
- [x] N should be odd.
- [ ] N can be even or odd.
- [ ] N can take any value.

**3) Which of the following statements are true regarding the Magic Squares? (N = Number of rows or columns)**
- [x] A Magic Square is always a square matrix.
- [ ] A Magic Square can or cannot be a square matrix.
- [ ] The Sum of each row and each column is N(N+1)/2
- [x] The Sum of each row and each column is N(N<sup>2</sup>+1 )/2.

**4) What will be the output of the following code?**

```python
'''
This is a sentence
'''
```
- [ ] This is a sentence.
- [ ] Error
- [x] No output
- [ ] The program will not run.

**5) Which of the following operator is used to raise the exponent to a number?**
- [ ] ^
- [ ] *
- [x] **
- [ ] ***

**6) Suppose there is a movie with 3 letters, how many combinations of names are possible?**
- [ ] 26
- [ ] 676
- [x] 17576
- [ ] 456976

**7) What should be the value of a, b, c, d respectively?**

| | | |
|---|---|---|
| 6 | a | 8 |
| b | 5 | c |
| 2 | d | 4 |

- [ ] 1,3,9,7
- [ ] 9,3,7,1
- [x] 1,7,3,9
- [ ] 7,3,9,1

**8) What will be the output of the following code?**

```python
L1 = ['harry potter', 'matrix', 'spiderman', 'avengers', 'john wick']
L2= ['drishyam', 'spiderman', 'bahubali', 'dhoom', 'race', 'matrix']

L = []


for i in range(len(L1)):

    flag = 0

    for j in range(len(L2)):

        if(L1[i] == L2[j]):
            flag = 1
            break
        else:
            flag = 0

    if(flag == 0):
        L.append(L1[i])

print(L)
```
- [x] Print unique movies of list L1
- [ ] Print unique movies of list L2
- [ ] Print unique movies of list L1 and L2
- [ ] Shows an error

**9) What will be the output of the following code?**

```python
for i in range(5,20):
    if(i%5 == 0):
        print(i**2)
```
- [ ] Print all perfect squares with square roots between 5-20 and divisible by 5.
- [ ] Print all perfect squares with square roots between 5-20 and not divisible by 5.
- [ ] Print all perfect squares with square roots between 5-19 and not divisible by 5.
- [x] Print all perfect squares with square roots between 5-19 and divisible by 5.

**10) A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. For example, 6 is a perfect number as the sum of its divisors 1,2,3 is equal to 6.
Which function will return True if the number is a perfect number?**

- [x] Option 1
  ```python
  def perfect_number(num):
      ans=0
      for i in range(1,num):
          if(num%i==0):
              ans = ans + i
      if(ans==num):
          return True
      else:
          return False
  ```
- [ ] Option 2
  ```python
  def perfect_number(num):
      ans=0
      for i in range(1,num):
          if(num%i==0):
              ans+=i
      if(ans==num):
          return False
      else:
          return True
  ```
- [ ] Option 3
  ```python
  def perfect_number(num):
      ans=0
      for i in range(3,num):
          if(num%i==0):
              ans = ans + i
      if(ans==num):
          return True
      else:
          return False
  ```
- [ ] Option 4
  ```python
  def perfect_number(num):
      ans=0
      for i in range(1,num):
          if(num%i==0):
              ans = ans + i
      if(ans!=num):
          return True
      else:
          return False
  ```
