# JOC Jul-2022 · Week 4: Assignment 4

- Source: <https://www.youtube.com/watch?v=-_HmpUzFM3w> · Techies Talk · published 2022-08-15
- Portal: `noc22_cs122`, due 2022-08-24, 23:59 IST → **Jul-2022 session**
- `[x]` = option ticked by the video author before submitting → unverified

**1) Which of the following statements are true regarding the Magic Squares? (N = Number of rows or columns)**
- [x] A Magic Square is always a square matrix.
- [ ] A Magic Square can or cannot be a square matrix.
- [ ] The Sum of each row and each column is N(N+1)/2
- [x] The Sum of each row and each column is N(N<sup>2</sup> +1)/2.

**2) What will be the output of the following code?**

```python
'''
This is a sentence
'''
```
- [ ] This is a sentence.
- [ ] Error
- [x] No output
- [ ] The program will not run

**3) A perfect number is a number in which the sum of its proper divisors is equal to that number. For example, 6 is a perfect number as the sum of its divisors 1,2,3 is equal to 6. Which function returns True if the number is perfect?**

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

**4) Suppose there is a movie with 3 letters, how many combinations of names are possible?**
- [ ] 26
- [ ] 676
- [x] 17576
- [ ] 456976

**5) What are the possible outputs of the following program?**

```python
import random

n = random.randint(0,100)
print(n%5)
```
- [x] Any number in the range between 0,4 (Both inclusive).
- [ ] Any number in the range between 1,4 (Both inclusive).
- [ ] Any number in the range between 0,5 (Both inclusive).
- [ ] Any number in the range between 1,5 (Both inclusive).

**6) Birthday Paradox can be simulated with approximately __________ people.**
- [ ] 365
- [ ] 100
- [ ] 40
- [x] 20

**7) What is the command to print the last result of the ipython console?**
- [ ] ''
- [ ] -
- [x] _
- [ ] \\

**8) What will be the output of the following program?**

```python
L1 = ['starwars', 'godfather', 'passsenger', 'jaurassic park']
L2 = ['spiderman', 'jumanji', 'Passenger', 'Starwars']

for i in L1:
    for j in L2:
        if i[0] == j[0]:
            print(j)
```
- [ ] Passenger, Starwars
- [x] spiderman, jumanji
- [ ] spiderman, jumanji, Passenger, Starwars
- [ ] spiderman, Starwars

**9) In the 'Dobble Game', if there are 8 objects on 1 card and 10 objects on another, how many comparisons are possible?**
- [ ] 8
- [ ] 10
- [ ] 18
- [x] 80

**10) What will be the output of the following code?**

```python
import random

L = ['harry potter', 'matrix', 'spiderman', 'terminator', 'karate ki   ← line is cut off at the right edge of the question image

movie = random.choice(L)

count = 0

for character in movie:

    if(character == 'a' or character == 'A'):
        count = count+1

    elif(character == 'e' or character == 'E'):
        count = count+1

    elif(character == 'i' or character == 'I'):
        count = count+1

    elif(character == 'o' or character == 'O'):
        count = count+1

    elif(character == 'U' or character == 'u'):
        count = count+1

print(count, movie)
```
- [ ] Display the number of consonants and name of the movie.
- [ ] Display the number of letters and name of the movie.
- [x] Display the number of vowels and name of the movie.
- [ ] Display the number of special characters and name of the movie.
