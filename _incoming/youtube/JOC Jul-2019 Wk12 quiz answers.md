# JOC Jul-2019 · Week 12 · Assignment 12

- Source: <https://www.youtube.com/watch?v=7VgRqKZQsuY> · ultimate gamer · published 2019-10-15
- Portal: "Your last recorded submission was on 2019-10-15, 17:50 IST" (the due date is cut off at the frame edge) → **Jul-2019 session** (by upload/submission date)
- `[x]` = option selected by the author; the page shows "Thank you for taking the Assignment 12." → submitted, but no score shown, so unverified.

**1) In the point distribution method of page rank algorithm, at each iteration, each node shares its pagerank value by […]** (the rest of the line is cut off at the frame edge)
- [ ] Randomly choosing one of its outgoing links and sharing all its pagerank value to the node connected to that link
- [x] Dividing its pagerank value equally to all the outgoing links
- [ ] Dividing its pagerank value randomly to all the outgoing links
- [ ] Dividing its pagerank value to all the outgoing links with the value given being proportional to their outdegree

**2) In random walk method, what is the next step when a sink node is encountered in the underlying graph?**
- [x] random node is chosen out of all the given node
- [ ] The node with maximum number of incoming links is chosen
- [ ] The node with maximum number of outgoing links is chosen
- [ ] The process stops at this stage

**3) According to Google Page rank algorithm, rank of a page depends on:**
- [ ] Number of pages it is referring to
- [x] Number of pages referring to it
- [ ] Rank of pages it is referring to
- [ ] Rank of pages referring to it

> ⚠ **Official accepted answer: "Rank of pages referring to it"** (see the official section at the end). The tick above is wrong.

**4) Which of the following is not true about Collatz Conjecture?**
- [ ] If the previous term is even, the next term is one half the previous term
- [x] If the previous term is odd, the next term is 3 times the previous term
- [ ] If the previous term is odd, the next term is 3 times the previous term plus 1
- [ ] No matter what value of n, the sequence will always reach 1

**5) State True or False.**
**The sequence based on 3n+1 problem will always reach 1.**
- [x] True
- [ ] False

**6) What is the sequence obtained according 3m+1 algorithm for m=9?**
- [x] 28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1
- [ ] 28,14,7,22,11,34,52,26,13,40,20,10,5,16,8,4,2,1
- [ ] 28,14,7,22,11,17,52,26,13,40,20,10,5,16,8,4,2,1
- [ ] 28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1

> Note: in this Jul-2019 run, options A and D really are identical; the official review page shows the same thing. The accepted answer is that full sequence, and the ticked A is marked "Yes, the answer is correct" with **Score: 0**, so the question was zero-weighted. In the Jan-2019 version (Jan-2019 Week 12 Q4), option A drops "52" instead, and the full sequence is option D.

**7) Consider the following statements:**
**Statement (a): Random Walk method requires lesser number of iterations to calculate accurate PageRank as compare to Points Distribution method**
**Statement (b): Points Distribution method requires lesser number of iterations to calculate accurate PageRank as compare to Random Walk method**
- [ ] Statement a is correct
- [ ] Statement b is correct
- [x] None of the above

**8) In the web graph, nodes are the web pages. What are the edges?**
- [ ] Network Connections
- [x] Links to other web pages
- [ ] URLs
- [ ] None of the above

---

## ✅ Official accepted answers and programming assignments (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-10-23, 14:48 IST).
- **Accepted answers:** Q1 Dividing its pagerank value equally to all the outgoing links · Q2 random node is chosen out of all the given node · **Q3 Rank of pages referring to it** · Q4 If the previous term is odd, the next term is 3 times the previous term · Q5 True · Q6 28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1 (Score 0, zero-weighted) · Q7 None of the above · Q8 Links to other web pages.
- ⚠ **Q3 is confirmed wrong above.** "Number of pages referring to it" is ticked; the accepted answer is "Rank of pages referring to it". Every other tick matches.

### Programming Assignment-1: Holes

Let us assume paper as the plane and a letter as a curve on the plane, then each letter divides [the plane into regions. For] example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters e[ach have one hole. Similarly,] letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. We say that the num[ber of holes in the text is equal] to the total number of holes in the letters of the text. Write a program to determine how many ho[les are in a given text.]

Input Format:
The only line contains a non-empty text composed only of uppercase letters of English alphabet[s.]

Output Format:
output a single line containing the number of holes in the corresponding text.

Example-1

Input:
DRINKEATCODE

Output:
5

Explanation:
D R A O D has one hole hence total number of holes in the text is 5.

Private test inputs: `KHUIOPDSHAUPBIPGYUIHDSJIAPGHUIPBJIP` · `JUHJPHJPBJPDSAGJIPHBJIPHUIVHUOYBJIPUUUUFOYUOGBJIPHUIFGYUO` · `HUIGDUSAIOGBHUOGGIDSA` (expected outputs cut off)

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

list_st = []


zero_hole = ["C","E","F","G","H","I","J","K","L","M","N","S","T","U","V","W","X","Y","Z"]
one_hole = ["A","D","O","P","Q","R"]
two_hole = ["B"]




x = input()


c = 0
for j in x:
    if(j in one_hole):
        c = c+1
    if(j in two_hole):
        c=c+2
print(c)
```
(Lines 17–19 are blank in the frame.)

### Programming Assignment-2: Smallest Palindrome

Given a string **S** having characters from English alphabets ['a' - 'z'] and '.' as the special charact[er …]
Write a program to construct the lexicographically smallest palindrome by filling each of the fade[d '.' characters with a lower] case alphabet.

**Definition:**
The smallest lexicographical order is an order relation where string **s** is smaller than **t**, given the [first character of s (s₁) is] smaller than the first character of **t** (t₁), or in case they
are equivalent, the second character, etc.

For example "aaabbb" is smaller than "aaac" because although the first three characters
are equal, the fourth character b is smaller than the fourth character c.

**Input Format:**
String S

**Output Format:**
Print lexicographically smallest palindrome after filling each '.' character, if it
possible to construct one. Print -1 otherwise.

Example-1

Input:
a.ba

Output:
abba

Example-2:

Input:
a.b

Output:
-1

Explanation:
**In example 1**, you can create a palindrome by filling the '.' character by 'b'.
**In example 2**, it is not possible to make the string **s** a palindrome.

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `dsj.dsa..dsaffds` | `-1` |
| 2 | `axzy...yzxa` | `axzyaaayzxa` |

Sample solutions (Provided by instructor; only the first 16 lines were visible):
```python
"""

@author: descentis
"""


numbers = []


li = []
x = input()
li = list(str(x))
if(len(li)%2 != 0):
    if(li[int(len(li)/2)] == '.'):
        li[int(len(li)/2)] = 'a'
s=0
# … (rest not shown)
```

### Programming Assignment-3: Letters

Write a program that accepts a sentence and calculate the number of upper case letters and lo[wer case letters.]

Input Format:
The first line of the input contains a statement.

Output Format:
Print the number of upper case and lower case respectively separated by a space.

Example:

Input:
Hello world!

Output:
1 9

Private test inputs: `In 10 hours, learn the basics of the world's fastest growing and most popular programming language` · `Say "Hello, World!" With Python` · `Learn Python in simple and easy steps`

Sample solutions (Provided by instructor):
```python
"""

@author: Descentis
"""


s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print(d['UPPER CASE'],d['LOWER CASE'])
```
