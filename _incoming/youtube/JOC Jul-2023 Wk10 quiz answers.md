# JOC Jul-2023 · Week 10: Assignment 10

- Source: <https://www.youtube.com/watch?v=6wGLF57gidM> · Techies Talk · published 2023-09-25 · "NPTEL The Joy of Computing using Python Week10 Quiz Assignment Solutions | July 2023" (386 s screen recording)
- Portal: `noc23_cs108`, "Due date: 2023-10-04, 23:59 IST." → **Jul-2023 session**. Each question is 1 point; 11 questions this week.
- `[x]` = option the author selected (some selections were not yet made when the question was on screen). No score is shown.
- Q1 text is small in the video; options are my best reading.

**1) What is the output of the following code?**
```python
 1  s = 'Hello Everyone'
 2  print(s.lower())
```
- [ ] HELLO EVERYONE
- [ ] Hello Everyone
- [ ] helloeveryone
- [ ] hello everyone

**2) In flames game when we will stop the iteration over FLAMES?**
- [x] When only one letter is left in flames.
- [ ] Only once.
- [ ] Only the letter remaining times.
- [ ] None of the above.

**3) Output of the following code will be?**
```python
 1  a = ['','h','e','l','','l','o']
 2  print('.'.join(a))
```
- [ ] hello
- [ ] h.e.l.l.o
- [ ] .h.e.l..l.o
- [ ] .h.e.l.l.o

**4) Which code snippet represents replacing all vowels with '_' in a string?**

Option A
```python
 1  s='The joy of Computing'
 2
 3  s.replace('a', '_')
 4  s.replace('e', '_')
 5  s.replace('i', '_')
 6  s.replace('i', '_')
 7  s.replace('o', '_')
 8  s.replace('u', '_')
 9
10  print(s)
```
- [ ] (Option A)

Option B
```python
 1  s='The joy of Computing'
 2
 3  s.replace('_', 'a')
 4  s.replace('_', 'e')
 5  s.replace('_', 'i')
 6  s.replace('_', 'o')
 7  s.replace('_', 'u')
 8
 9  print(s)
```
- [ ] (Option B)

Option C
```python
 1  s='The joy of Computing'
 2
 3  s = s.replace('_', 'a')
 4  s = s.replace('_', 'e')
 5  s = s.replace('_', 'i')
 6  s = s.replace('_', 'o')
 7  s = s.replace('_', 'u')
 8
 9  print(s)
```
- [ ] (Option C)

Option D
```python
 1  s='The joy of Computing'
 2
 3  s = s.replace('a', '_')
 4  s = s.replace('e', '_')
 5  s = s.replace('i', '_')
 6  s = s.replace('o', '_')
 7  s = s.replace('u', '_')
 8
 9  print(s)
```
- [x] (Option D)

(Option A lists 'i' twice; transcribed as shown.)

**5) What will be the output of the following list slicing.**
```python
 1  s = 'The Joy of Computing'
 2
 3  print(s[3:12])
```
- [ ] 'Joy of C'
- [x] ' Joy of C'
- [ ] 'Joy of Co'
- [ ] ' Joy of Co'

**6) What does the following code represent?**
```python
 1  s = 'Sheher mein'
 2  a = 'aeiouAEIOU'
 3  for i in range(len(s)):
 4      if(s.index(s[i])%2 == 0):
 5          print(i)
 6          if(s[i] in a):
 7              s = s.replace(s[i], '_')
 8
 9
10  print(s)
```
- [ ] Replacing all letters at odd index with '_'.
- [ ] Replacing all vowels at odd index with '_'.
- [x] Replacing all vowels at even index with '_'.
- [ ] Replacing all letters at even index with '_'.

**7) What will be the output of the following code?**
```python
 1  import numpy as np
 2
 3  b = np.array([[1,2],[3,4]])
 4
 5  print(np.sum(b, axis = 1))
```
- [ ] [4 6]
- [x] [3 7]
- [ ] [3 4]
- [ ] None of the above

**8) What is the correct way to display the transpose of a matrix?** (checkboxes: more than one can be selected)

Option A
```python
import numpy as np

b = np.array([[1,2],[3,4]])

print(b.T())
```
- [ ] (Option A)

Option B
```python
import numpy as np

b = np.array([[1,2],[3,4]])

print(b.transpose())
```
- [x] (Option B)

Option C
```python
import numpy as np

b = np.array([[1,2],[3,4]])

print(b.T)
```
- [x] (Option C)

Option D
```python
import numpy as np

b = np.array([[1,2],[3,4]])

print(b.transpose)
```
- [ ] (Option D)

**9) Are Lossy and Lossless compressions the same?**
- [ ] Yes, they are identical.
- [x] No, they are different.
- [ ] It depends on the context.
- [ ] Not enough information provided.

**10) What is the shape of the following numpy array?**
`numpy.array([ [1,2,3], [4,5,6] ])`
- [x] (2,3)
- [ ] (3,2)
- [ ] (3,3)
- [ ] (2,2)

**11) What will be the output of the following code?**
```python
 1  import numpy as np
 2
 3  a = np.array([[8,9,20],[10,31,22]])
 4  b = np.array([[1,2,3],[4,5,6]])
 5
 6  print(a-b)
```
- [ ] [[6 6 6] [6 6 6]]
- [ ] [[ -7 -7 -17] [ -6 -26 -16]]
- [x] [[ 7 7 17] [ 6 26 16]]
- [ ] [[ 9 11 23] [14 36 28]]
