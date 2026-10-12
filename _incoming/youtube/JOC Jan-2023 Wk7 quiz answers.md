# JOC Jan-2023 · Week 7 : Assignment 1

- Source: <https://www.youtube.com/watch?v=3TMLjIFxLJw> · Techies Talk · published 2023-03-03
- Portal: `noc23_cs20` → **Jan-2023 session**
- `[x]` = option ticked by the video author → unverified

**1) Which of the following is/are uses of functions?**
- [ ] Gives a higher-level overview of the task to be performed
- [ ] Reusability- uses the same functionality at various places
- [ ] A better understanding of code
- [x] All of the above
- [ ] None of the above

**2) What is the output of the following spiral print python function?**

```python
def spiralprint(m, n, spiralmatrix):
    k = 0
    l = 0
    while (k < m and l < n):
        for i in range(l, n):
            print(spiralmatrix[k][i], end=" ")
        k += 1
        for i in range(k, m):
            print(spiralmatrix[i][n - 1], end=" ")
        n -= 1
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(spiralmatrix[m - 1][i], end=" ")
            m -= 2
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(spiralmatrix[i][l], end=" ")
            l += 2
spiralmatrix = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

rows = 3
cols = 6
spiralprint(rows, cols, spiralmatrix)
```
- [ ] 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
- [x] 1 2 3 4 5 6 12 18 17 16 15 14 13
- [ ] 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
- [ ] 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

**3) Which of the following library moves the turtle backward?**
- [ ] turtle.back(distance)
- [ ] turtle.bk(distance)
- [ ] turtle.backward(distance)
- [x] All of the above

**4) Which of the following library has to be imported to plot the route map using GPS locations in python?**
- [ ] gmplot
- [ ] csv
- [x] both
- [ ] None

**5) bytes, bytearray, memoryview are type of the ___ data type.**
- [ ] Mapping Type
- [ ] Boolean Type
- [x] Binary Types
- [ ] All of the above
- [ ] None of the above

**6) In the Snakes and Ladders game, the least number of times a player has to roll a die with the following ladder positions is ______________
ladders = { 3: 20, 6: 14, 11: 28, 15: 34, 17: 74, 22: 37, 38: 59, 49: 67, 57: 76, 61: 78, 73: 86, 81: 98, 88: 91 }**
- [ ] 4
- [x] 5
- [ ] 6
- [ ] 7

**7) Which of the following code snippet will create a tuple in python?**
- [x] name = ('kiran','bhushan','madan')
- [ ] name = {'kiran','bhushan','madan'}
- [ ] name = ['kiran','bhushan','madan']
- [ ] None of the above

**8) What does the following program plot?**

```python
import random
import matplotlib.pyplot as plt
rn=random.randint(0,9)
print(rn)
l=[0 for i in range(10)]
y=[]
for i in range(10):
  x=int(input())
  y.append(i)
  if x==rn:
    l[x]+=1
plt.plot(y,l)
plt.show()
```
- [ ] Plots the random number generated in each iteration
- [x] Plots the number of times the given input matches with the random number generated
- [ ] Plots the input entered for each iteration
- [ ] none of the above

**9) Sentiment analysis involves working with ___________**
- [ ] a piece of information is useful or not
- [ ] a piece of information is biased or unbiased
- [ ] a piece of information is true or false
- [x] a piece of information is positive or negative

**10) What does the following code snippet in python compute**

```python
text1 = input()
len1 = len(text1)
text2 = input()
len2 = len(text2)
for i in range(0,len1-len2+1):
    j = 0
    while ((j < len2) and (text1[i + j] == text2[j])):
        j = j + 1
    if (j==len2):
        print(text2)
```
- [ ] checks whether the two given texts are the same
- [ ] searches for text2 in text1
- [x] finds all the occurrences of text2 in text1
- [ ] none of the above
