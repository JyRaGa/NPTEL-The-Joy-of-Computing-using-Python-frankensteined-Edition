# JOC Jul-2022 · Week 10: Assignment 10

- Source: <https://www.youtube.com/watch?v=A2p4zimg5lE> · Techies Talk · published 2022-09-26
- Portal: `noc22_cs122`, due 2022-10-05, 23:59 IST → **Jul-2022 session**
- `[x]` = option ticked by the video author before submitting → unverified

**1) Which math problem flames is related to?**
- [ ] kadane's problem
- [x] Josephus problem
- [ ] Conjecture Collatz
- [ ] Dijkstra Problem

**2) Which of the following is the task of s.upper()(Given the string name is 's')?**
- [ ] It converts the first character into uppercase.
- [ ] It converts every vowel into uppercase.
- [x] It converts every single character into uppercase.
- [ ] It converts consonants into uppercase.

**3) What is the output of the following code?**

```python
s = 'The Joy of Computing'
print(s[:])
```
- [x] 'The Joy of Computing'
- [ ] ' Joy of C'
- [ ] 'Joy of C'
- [ ] Error

**4) What will be the output of the following program?**

```python
import numpy as np

b = np.array([[1, 2]]), [3, 4]
print(np.sum(b))
```
- [ ] [[3, 7]]
- [x] [[4, 6]]
- [ ] [[5, 5]]
- [ ] [[4, 4]]

**5) What will be the output of the following program?**

```python
s = 'I am amazed'
s.replace('a', 'z')
print(s)
```
- [ ] I zm zmzzed
- [ ] I zm zmazed
- [ ] I am zmzzed
- [x] I am amazed

**6) What are the consequences of image compression?**
- [x] Less size
- [x] Lower quality
- [ ] More size
- [ ] Higher quality

**7) What will be the output of the following program?**

```python
s = 'JOC'
print('#'.join(s))
```
- [ ] JOC
- [ ] #J#O#C#
- [ ] #J#O#C
- [x] J#O#C

**8) How to take a transpose of a matrix?**

- [ ] Option 1
  ```python
  import numpy as np

  b = np.array([[1,2],[3,4]])

  print(b.T())
  ```
- [x] Option 2
  ```python
  import numpy as np

  b = np.array([[1,2],[3,4]])

  print(b.transpose())
  ```
- [x] Option 3
  ```python
  import numpy as np

  b = np.array([[1,2],[3,4]])

  print(b.T)
  ```
- [ ] Option 4
  ```python
  import numpy as np

  b = np.array([[1,2],[3,4]])

  print(b.transpose)
  ```

**9) Consider the following code.**

```python
import numpy as np

a = np.array([[8,9,20],[10,31,22]])
b = np.array([[1,2,3],[4,5,6]])
```
**What print(a+b) will produce?**
- [ ] Option 1
  ```
  [[6 6 6]
   [6 6 6]]
  ```
- [ ] Option 2
  ```
  [[ -7 -7 -17]
   [ -6 -26 -16]]
  ```
- [ ] Option 3
  ```
  [[ 7 7 17]
   [ 6 26 16]]
  ```
- [x] Option 4
  ```
  [[ 9 11 23]
   [14 36 28]]
  ```

**10) what is the output of the following code?**

```python
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.reshape(3,4))
```
- [x] Option 1
  ```
  [[ 1 2 3 4]
   [ 5 6 7 8]
   [ 9 10 11 12]]
  ```
- [ ] Option 2
  ```
  [[ 1 2 3]
   [ 4 5 6]
   [ 7 8 9]
   [10 11 12]]
  ```
- [ ] Error
