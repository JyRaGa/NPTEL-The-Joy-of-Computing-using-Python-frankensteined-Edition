# JOC Jul-2019 · Week 9: Cool Ideas (Part 7) · Assignment 9

- Source: <https://www.youtube.com/watch?v=eIMUWqigD6I> · Ultimate Gamer · published 2019-09-23
- Portal: "Your last recorded submission was on 2019-09-23, 19:42 IST" (the due date is cut off at the frame edge) → **Jul-2019 session** (by upload/submission date)
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown). Video ends with "WE CAN NOT GUARANTEE THAT THESE SOLUTIONS ARE 100% CORRECT."
- The code is reproduced as the portal rendered it. Q8 shows spaces where underscores would be (`add node`, `add edge`).

**1) In networkx, in order to draw Erdos Renyi graph there is a function 'gnp random graph(n,p)'. What are n and p here?**
- [ ] n is the number of edges and p is the probability of edge creation
- [x] n is the number of nodes and p is the probability of edge creation
- [ ] n is the number of edges and p is the probability of node creation
- [ ] n is the number of nodes and p is the probability of node creation

**2) Which of the following is NOT a Graph visualisation software/tool?**
- [ ] Gephi
- [ ] Cytoscape
- [ ] Networkx
- [x] Eclipse

**3) What is the output of the following code snippet?**
```
import networkx as nx
G=nx.Graph()
print(G.nodes())
```
- [ ] [A]
- [x] [ ]
- [ ] None
- [ ] Null

**4) What is the output of the following program?**
```
import networkx as nx
G=nx.path_graph(4)
print(G.nodes())
```
- [x] [0,1,2,3]
- [ ] [1,2,3,4]
- [ ] [A,B,C,D]
- [ ] None of the above

**5) If the area of India is 10400 km², calculate the area of Maharashtra. (If points are placed randomly in the map of India, then number of points in India(except Maharashtra) is 90 and number of points in Maharashtra is 23.)**
- [ ] 2657.77m²
- [x] 2657.77Km²
- [ ] 2500.33km²
- [ ] 2500.33m²

> Note: 2657.77 = 10400 × 23/90, which treats 90 as the total number of points. If you read "except Maharashtra" literally, the answer is 10400 × 23/113 ≈ 2116.8, which is not an option, so the ticked option is the intended one.

**6) Sentence tokenisation is possible through NLTK in Python.**
- [x] Yes
- [ ] No

**7) Stylometry is based on the observation that authors tend to write in unique ways**
- [x] Yes
- [ ] No

**8) What should be the output of the following program?**
```
import network as nx
G=nx.Graph()
for i in range(3):
G.add node(i)
G.add edge(1,2)
G.add edge(2,3)
G.add edge(1,3)
nx.draw()
```
- [ ] A triangle graph
- [ ] A graph with 3 edges and an isolated node
- [ ] A graph with 3 edges and no isolated node
- [x] Error

> ✅ Official accepted answer: **Error** (see the official section at the end). Background: it depends on how you read the code. As displayed (`import network`, missing underscores, no indentation, `nx.draw()` without G) it is an Error. If the intended code is `add_node`/`add_edge`, the graph has nodes 0–3 with a 1-2-3 triangle and node 0 isolated → "A graph with 3 edges and an isolated node".

**9) What should be passed as an argument in the function given below?**
```
G.add_nodes_from(*)
```
- [ ] Dictionary
- [ ] Set
- [ ] List
- [x] All of the above

---

## Second source: Mayank Patel

- Source: <https://www.youtube.com/watch?v=FKE4PdlwY0Q> · Mayank Patel · published 2019-09-30 · "Your last recorded submission was on 2019-09-29, 13:18 IST"; **quiz due 2019-10-02, 23:59 IST** (fills the missing due date above).
- **Quiz Q1–Q9: same ticks as above**, including Q8 "Error". This page also shows the Q8 code with spaces (`G.add node(i)`, `G.add edge(1,2)`) and `import network as nx`.

### Programming Assignment-1: Counter Spiral (due 2019-10-03, 23:59 IST)

Given a square matrix, you have to write a program to print it in a counter-clockwise spiral form.

Input Format:
The first line of the input contains an integer number **n** which represents the number of rows and columns in the matrix.
From the second line contains **n** rows with each row having **n** elements separated by a space.

Output Format:
Print the elements in a single line with each element separated by a space

Example:

Input:
4
25 1 29 7
24 20 4 32
16 38 29 1
48 25 21 19

Output:
25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4

Explanation:
In the above example, each row, first all the elements of the first column is printed which are 25 24 16 48 after that, remaining elements of the last row is printed which are 25 21 and 19.
After which the remaining elements of the last column is printed which are 1 32 and 7 and so on...

Author's code (lines 1–41 visible; the rest scrolled out of view; private test cases 1–3: Passed):
```python
a= int(input())
mat=[]
for i in range(0,a):
  l=list(map(int, input().split()))
  mat.append(l)
m=a
n=a
k=0
l=0
count =0
total = a*a

while(k<m and l <n):
  if(count == total):
    break

  for i in range(k,m):
    print(mat[i][l],end= " ")
    count += 1

  l += 1

  if(count == total):
    break

  for i in range(l,n):
    print(mat[m-1][i],end= " ")
    count += 1

  m -= 1

  if(count == total):
    break

  if(k<m):
    for i in range(m-1,k-1,-1):
      print(mat[i][n-1],end= " ")
      count += 1

  n -= 1
  # … (remaining lines not captured)
```
Sample test case 1: `3 / 1 2 3 / 4 5 6 / 7 8 9` → `1 4 7 8 9 6 3 2 5`.

### Programming Assignment-2: Maximum Numeric (due 2019-10-03, 23:59 IST)

Given an alphanumeric string **S**, extract maximum numeric value from that string. All the alphabets are in lower case. Take the maximum consecutive digits as a single number.

**Input Format:**
The first line contains the string S.

**Output Format:**
Print the maximum value

**Example:**

Input:
23dsa43dsa98

Output:
98

Explanation:
There are three integer values present in the string, 23, 43 and 98. Among these, 98 is the maximum.

Author's code:
```python
import re
ip=input()
l=((re.findall('\d+',ip)))
l=list(map(int,l))
print(max(l),end='')
```

### Programming Assignment-3: Email ID (due 2019-10-03, 23:59 IST)

Assuming that we have some email addresses in the **"username@companyname.com"** format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Input Format:
The first line of the input contains an email address.

Output Format:
Print the company name in single line.

Example;

Input:
john@google.com

Output:
google

Author's code (private test cases 1–3: Passed):
```python
ip=input()
x=ip.index("@")
print(ip[x+1:len(ip)-4],end='')
```
Sample test cases: `amit@sccilabs.com` → `sccilabs`; `simran@iitrpr.com` → `iitrpr`; `tushita@classready.com` → `classready`.

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-10-02, 16:17 IST).
- **Accepted answers seen:** Q1 n is the number of nodes and p is the probability of edge creation · Q3 [ ] · Q4 [0,1,2,3] · **Q5 2657.77Km²** · Q6 Yes · Q7 Yes · **Q8 Error**. Q2 and Q9 were not shown.
- **This settles the Q8 and Q5 notes above:** the official answers are "Error" and "2657.77Km²", the ticked options.

### Programming Assignment-1: Counter Spiral

The private test cases are very large matrices (over 50 values) and are not transcribed. The instructor sample solution was not shown in the recording.

### Programming Assignment-2: Maximum Numeric — private tests and instructor solution

| Test case | Input |
|---|---|
| 1 | `amit123aman786` |
| 2 | `ghjldsagjulsda1234hdsjkalgjk8765dsgayhuf3214bjdksa234bhfjksahj9878dsahjk…` (cut off) |
| 3 | `1g2g3g4g5g6g7g8` |

(Expected outputs scrolled out of view; by the statement they are 786, the largest run in TC2, and 8.)

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

import re

def extractMax(input):

    # get a list of all numbers separated by
    # lower case characters
    # \d+ is a regular expression which means
    # one or more digit
    # output will be like ['100','564','365']
    numbers = re.findall('\d+',input)

    # now we need to convert each number into integer
    # int(string) converts string into integer
    # we will map int() function onto all elements
    # of numbers list
    numbers = map(int,numbers)

    print(max(numbers))

S = input()
extractMax(S)
```

### Programming Assignment-3: Email ID — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `amit@dsi.com` | `dsi` |
| 2 | `sumit@amazon.com` | `amazon` |
| 3 | `ajay@manga.com` | `manga` |

Sample solutions (Provided by instructor):
```python
"""

@author: Descentis
"""


import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))
```
