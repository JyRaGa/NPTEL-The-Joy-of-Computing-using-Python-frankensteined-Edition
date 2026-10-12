# JOC Jan-2023 · Week 2 : Assignment 1

- Source: <https://www.youtube.com/watch?v=LUJjG8wQf40> · Techies Talk · published 2023-02-07
- Portal: `onlinecourses.nptel.ac.in/noc23_cs20` → **Jan-2023 session**
- `[x]` = option ticked by the video author before submitting (not NPTEL "Accepted Answers") → unverified

**1) What are the applications of Python?**
- [ ] Image processing and graphic design applications
- [ ] Enterprise and business applications development
- [ ] Operating systems
- [x] All of the above
- [ ] None of the above

**2) Which of the following is not the correct variable name**
- [ ] Abc
- [ ] Abd23
- [x] 32asd
- [ ] Ab_cd_23

**3) Write the output of the following code.**

```python
L = [1,2,3,4,5,6,7,8,9]

print(L[::-1])
```
- [ ] [1,2,3,4,5,6,7,8,9]
- [ ] [1,2,3,4,5,9,8,7,6]
- [x] [9,8,7,6,5,4,3,2,1]
- [ ] Error

**4) Predict the output of the following code:**

```python
L = [[1,2,3],[0,4,5],[0,0,6]]
```
```python
for i in range (3):
    for j in range(2,i-1,-1):
        print(L[i][j], end = "")
```
- [ ] 3,2,1,5,4,6
- [x] 3 2 1 5 4 6
- [ ] 0,0,0,0,0,0
- [ ] 0 0 0 0 0 0

**5) Find all the error(s)in the following code:**

```python
n = 10
l = []
for i in range(10,n+10):
l.append(i**i)

for i in range (10,0,-1):
print(l[i])
```
- [x] Index out of range
- [x] Syntax error
- [ ] Variable not defined
- [ ] 'int' object does not support item assignment

**6) What is the output of the following code:**

```python
def add_items(x,y):
    x+= [1,2]
    y+= (3,4)
l = [0]
t = (5,)
add_items(l, t)
print(l,end="")
print(t)
```
- [ ] [0,1,2] (5,3,4)
- [x] [0,1,2] (5,)
- [ ] [0] (5,3,4)
- [ ] [0] (5,)

**7) What is the correct syntax for defining a function in Python?**
- [x] def function name():
- [ ] function function_name():
- [ ] function_name():
- [ ] def function_name:

**8) What is the purpose of the continue statement in a for loop?**
- [ ] To skip the rest of the current iteration and move on to the next one
- [ ] To terminate the loop and exit the loop block
- [ ] To return to the top of the loop and start a new iteration
- [x] To skip the current iteration and move on to the next one, but only if a certain condition is met

**9) How do you check if a number is even in Python?**
- [x] if number % 2 == 0
- [ ] if number.is_even()
- [ ] if number % 2 is 0
- [ ] if number.even()

**10) What should be the value of _ to print all numbers from 0-10?**

```python
for i in range( _ ):
    print(i)
```
- [ ] 11 ← cursor on this option at the moment of clicking; the ticked frame was not captured
- [ ] 9
- [ ] 10
- [ ] None of the above
