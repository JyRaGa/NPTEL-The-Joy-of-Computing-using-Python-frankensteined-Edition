# JOC Jan-2023 · Week 3 : Assignment 1

- Source: <https://www.youtube.com/watch?v=k0CEbHOpNo4> · Techies Talk · published 2023-02-12
- Portal: `noc23_cs20`, due 2023-02-15, 23:59 IST → **Jan-2023 session**
- `[x]` = option ticked by the video author → unverified

**1) ____________ is the method to insert an item into a specified position in a list.**
- [ ] Push
- [ ] Write
- [x] Insert
- [ ] All of the above

**2) Which method returns the number of occurrences of an element in a list.**
- [ ] Number of
- [ ] Total
- [x] Count
- [ ] Length

**3) The function random.randint(1,100) in python generates.**
- [x] A random integer between 1 to 100 with 1 and 100 both inclusive
- [ ] A random integer between 1 to 100 with 1 and 100 both exclusive
- [ ] A random integer between 1 to 100 with only 100 inclusive
- [ ] None of the above

**4) The method open("file1.txt", r+) opens the file file1.txt in ___________________.**
- [ ] Read only mode
- [ ] Write only mode
- [x] Read Write mode
- [ ] None of the above

**5) Consider the list L= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]. What will be the output of the statement L [3:6]?**
- [x] [2, 3, 5]
- [ ] [0, 1, 1]
- [ ] [1, 2, 3]
- [ ] none

**6) What is the output of this code?**

```python
a,b=1,0
a=a^b
b=a^b
a=a^b
print(a)
```
- [x] 0
- [ ] 1
- [ ] 2
- [ ] This code will raise a runtime error

**7) What is the output of the following code?**

```python
def foo(l):
    a = l[0]
    for i in l:
        if i < a:
            a = i
    return a

print(foo([2, 3, 5, 1, 7, 6]))
```
Answer box (typed by author): `1`

**8) What is the output of the following code?**

```python
def bar(string):
    left = 0
    right = len(string) - 1
    while(left < right):
            if(string[left] != string[right]):
                    return False
            left += 1
            right -= 1
    return True

print(bar("telugu"))
print(bar("malayalam"))
```
- [x] False True
- [ ] True False
- [ ] True True
- [ ] False False

**9) Explain what the output will be when the code given below is executed.**

```python
def func(list1):
  while (len(list1) > 2):
    k=list1[0]
    for i in list1:
      if k<i:
        k=i
    list1.remove(k)

    j=list1[0]
    for i in list1:
      if j>i:
        j=i
    list1.remove(j)
  return list1

list2=func([1,4,3,6,5,3,7,8,9,4])
#sum is a function which returns the sum of all of the values of all the elements of a list
print(sum(list2)/len(list2))
```
- [ ] The program throws an error
- [ ] 5
- [ ] 5.5
- [x] 4.5

**10) Which among the following statements is True with respect to the code given below?**

```python
count = 0
for i in range(10):
    for j in range(5):
        count += i *j
print(count)
```
- [ ] count=50
- [ ] The following code throws up an error.
- [ ] count=550
- [ ] count=450

> No tick was visible for Q10 in any captured frame (the cursor hovered "The following code throws up an error." at t≈243s, then the author scrolled up and submitted).
