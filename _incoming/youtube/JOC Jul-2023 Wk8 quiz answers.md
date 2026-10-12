# JOC Jul-2023 · Week 8: Assignment 8

- Source: <https://www.youtube.com/watch?v=Ks4H5dj5BqI> · MY SWAYAM · published 2023-09-09 (208 s screen recording)
- Portal: `noc23_cs108`, "Due date: 2023-09-20, 23:59 IST." → **Jul-2023 session**. Each question is 1 point.
- `[x]` = option the author selected while scrolling (only Q1, Q3 and Q4 selections are visible). No score is shown. Small, blurry text: Q1 and Q8 options are my best reading.

**1) What is the correct initialisation of tuples?**
- [ ] Dates = [12,23,3,4]
- [x] Dates = (12,23,3,4)
- [ ] Dates = {12,23,3,4}
- [ ] Both B and C

**2) What operations can be done on tuples?**
- [ ] Tuples are appendable.
- [ ] We can delete a value from tuples.
- [ ] Both A and B.
- [ ] We can count the number of instances of an element.

**3) What will be the output of the following code?**
```python
t = (1,2,3,4,5)

for i in range(-1,-len(t), -1):
    print(t[i])
```
- [ ] 1,2,3,4,5
- [ ] 5,4,3,2,1
- [x] 5,4,3,2
- [ ] 1,2,3,4

**4) What will be the output of the following code?**
```python
 1  word = 'facebook'
 2  new = ''
 3
 4  for w in word:
 5      i = ord(w)
 6
 7      j = ((( i+26 ) - 97 ) % 26 ) + 97
 8
 9      new = new + chr(j)
10
11  print(new)
```
- [x] facebook
- [ ] gbdfcppl
- [ ] ezbdannj
- [ ] ytvxuhhd

**5) When the following program will clap?**
```python
 1  print('Enter a letter between a-z')
 2
 3  player1 = str(input())
 4  player2 = str(input())
 5
 6  while(True):
 7
 8      if(ord(player1.lower())+1 == ord(player2.lower())):
 9          print('clap')
10          break
11      else:
12          player1 = str(input())
13          player2 = str(input())
14
```
- [ ] When both players will enter the same letters.
- [ ] When player 2 will enter the next letter with respect to player 1.
- [ ] When player 1 will enter the next letter with respect to player 2.
- [ ] It will never clap.

**6) Which statement is correct about the following program?**
```python
 1  import random
 2  import matplotlib.pyplot as plt
 3
 4  l = []
 5  count = 0
 6
 7  for i in range(10):
 8      guess = random.randint(1, 10)
 9      pick = random.randint(1, 10)
10
11      if(guess!=pick):
12          count+=1
13          l.append(count)
14      else:
15          count-=1
16          l.append(count)
17
18  plt.plot(l)
19  plt.show()
```
- [ ] The graph will go up when guess and pick are the same.
- [ ] The graph will go down when guess and pick are the same.
- [ ] The graph will go up when guess and pick are not the same.
- [ ] Both B and C

**7) What does NLTK do?**
- [ ] Helps to work with human language data.
- [ ] Helps to convert machine data into human language.
- [ ] Helps to work on gibberish language.
- [ ] Helps to translate dog language into human language.

**8) What is the output of the following code?**
```python
string = 'hey!there'

a = sorted(string)
a.reverse()

print(a)
```
- [ ] ['!', 'e', 'e', 'e', 'h', 'h', 'r', 't', 'y']
- [ ] ['h', 'e', 'y', '!', 't', 'h', 'e', 'r', 'e']
- [ ] ['y', 't', 'r', 'h', 'h', 'e', 'e', 'e', '!']
- [ ] None of the above

**9) While converting an image into black and white during enhancement you cannot convert it back into a colored image.**
- [ ] True
- [ ] False

**10) How does vader help in sentiment analysis?**
- [ ] It calculates whether the statement is negative, positive or neutral.
- [ ] It takes care of the intensity of a statement.
- [ ] Both A and B
- [ ] None of the above
