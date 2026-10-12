# JOC Jul-2019 · Week 8: Cool Ideas (Part 6) · Assignment 8 + Programming Assignments

- Source: <https://www.youtube.com/watch?v=4QscogEYOZ0> · Mayank Patel · published 2019-09-23 (the Ultimate Gamer Week 8 video was not found)
- Portal: `noc19_cs41` (visible in the status-bar URL); "Your last recorded submission was on 2019-09-23, 10:03 IST"; due 2019-09-25, 23:59 IST → **Jul-2019 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown).
- The video also shows the three Week 8 programming assignments with the author's code. All private test cases show "Passed".

**1) Suppose t = (1, 2, 4, 3), which of the following is incorrect?**
- [ ] print(t[3])
- [x] t[3] = 45
- [ ] print(max(t))
- [ ] print(len(t))

**2) What is the output of the following code?**
```
a=(1,2,3,4)
del(a[2])
print(a)
```
- [ ] (1,3,4)
- [ ] (1,2,4)
- [ ] (1,2,3)
- [x] Error

**3) Is the following piece of code valid?**
```
a=(1,2,3,4)
del a
```
- [x] Yes
- [ ] No

**4) What type of data is: a=[(1,1),(2,4),(3,9)]?**
- [ ] Array of tuples
- [x] List of tuples
- [ ] Tuples of lists
- [ ] Invalid type

**5) What is VADER?**
- [ ] It is used to extract data from a Facebook account
- [ ] It is used to convert speech into text
- [x] It is a lexicon and rule-based sentiment analysis tool
- [ ] It is used for special visual effects such as displaying variants of Google map

**6) Which of the following does CLAHE use to enhance the images?**
- [x] Histogram Equalisation
- [ ] Median Filtering
- [ ] Mask Filtering
- [ ] None of the above

**7) What is an Anagram?**
- [ ] A word that has the same meaning as another given word
- [ ] A word that has the same sound as another given word
- [x] A word, phrase, or name formed by rearranging the letters of another
- [ ] Any permutation of another given word

**8) Consider the scenario below: Ram wants to play a lottery game in which he has to choose one ticket out of 10 tickets. If the ticket chosen by the participant is 9, then he wins 500$. The price for playing the lottery game is 100$. Ram decides to play this game 10 times in order to guarantee his win. Would you advise him to play this game?**
- [ ] Yes
- [x] No
- [ ] Can't say

**9) Find out the anagrams present in the following sentences. One day, When I was going through my old stuff, I found my old study table. Though It was damn dusty, but still i could read the stupid stuff that i used to write on it as a kid.**
- [ ] year and ear
- [ ] night and thing
- [x] dusty and study
- [ ] There is no anagram present in the given sentences

---

## Programming Assignment - 1: Duplicate Elements (due 2019-09-25, 23:59 IST)

With a given list **L of integers**, write a program to print this list L after removing all duplicate values with original order preserved.

**Example:**

If the input list is

12 24 35 24 88 120 155 88 120 155

Then the output should be

12 24 35 88 120 155

**Explanation:**
Third, seventh and ninth element of the list **L** has been removed because it was already present.

**Input Format:**
In one line take the elements of the list **L** with each element separated by a space.

**Output Format:**
Print the elements of the modified list in one line with each element separated by a space.

**Example:**

Input:
12 24 35 24

Output:
12 24 35

Author's code (private test cases 1–3: Passed):
```python
A=list(map(int,input().split()))
B=[]
for i in A:
  if i not in B:
    B.append(i)
print(*B,end="")
```
(The public sample test-case values are too small to read reliably in the recording, so they are omitted.)

## Programming Assignment-2: Panagrams (due 2019-09-25, 23:59 IST)

A panagram is a sentence containing every 26 letters in the English alphabet. Given a string **S**, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
The quick brown fox jumps over the lazy dog

Output:
YES

Author's code (private test cases 1–3: Passed):
```python
alphabet=[]
for i in range(97,123):
    alphabet.append(chr(i))
s=input()
s=s.lower()
d=set(s)
d=list(d)
for i in d:
    if i in alphabet:
        alphabet.remove(i)
if len(alphabet)==0:
  print("YES",end="")
else:
  print("NO",end="")
```

## Programming Assignment-3: Vowels (due 2019-09-25, 23:59 IST)

Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.

Input Format:
Sentence S in a single line

Output Format:
Print S after removing consecutive vowels

Example:

Input:
your article is in queue

Output:
yor article is in qu

Explanation:

In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed. In the fifth word, 'u', 'e', 'u' and 'e' are appearing together, hence 'e', 'u', 'e' are removed.

Sample test cases:

| | Input | Output |
|---|---|---|
| Test Case 1 | great part of life | gret part of life |
| Test Case 2 | eel is electricity | el is electricity |
| Test Case 3 | love hate and war | love hate and war |

Author's code (private test cases 1–3: Passed):
```python
def vow(l):

    return ((l == 'a') or (l == 'e') or (l == 'i') or (l == 'o') or (l == 'u'))
def final(ip):
    print(ip[0], end = "");
    for i in range(1,len(ip)):
        if ((vow(ip[i - 1]) != True) or
            (vow(ip[i])!= True)):
            print(ip[i], end = "")
ip=input()
final(ip)
```

---

## ✅ Official accepted answers and instructor solutions (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-09-25, 21:48 IST).
- **Accepted answers:** Q1 t[3] = 45 · Q2 Error · Q3 Yes · Q4 List of tuples (marked correct) · Q5 It is a lexicon and rule-based sentiment analysis tool · Q6 Histogram Equalisation · Q7 A word, phrase, or name formed by rearranging the letters of another · Q8 No · Q9 dusty and study. **All ticks above are correct.**

### Programming Assignment - 1: Duplicate Elements — private tests and instructor solution

The three private test cases are long runs of single digits (for example `4 3 3 2 2 0 7 6 6 3 9 8 3 0 1 9 0 4 8 7 0 7 5 8 9 4 4 7 6 4 7 2 6 9 1 0 5 9 …`). They are too long to transcribe reliably from the frame and are omitted.

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
http://sccilabs.org/amit_verma.html
"""

def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[]
li= list(map(int, input ().split ()))
x = removeDuplicate(li)

for i in x:
    print(i,end=" ")
```

### Programming Assignment-2: Panagrams — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `Ghe quick brown fox jumps ovar the lezy doT` | `YES` |
| 2 | `Ghe quick bxown for jumps ovar the lezy doT` | `YES` |
| 3 | `abc` | `NO` |

Sample solutions (Provided by instructor; the final `else` branch is cut off):
```python
"""

@author: descentis
"""

def checkPangram(s):
    List = []
    # create list of 26 charecters and set false each entry
    for i in range(26):
        List.append(False)

    #converting the sentence to lowercase and iterating
    # over the sentence
    for c in s.lower():
        if not c == " ":
            # make the corresponding entry True
            List[ord(c) -ord('a')]=True

    #check if any charecter is missing then return False
    for ch in List:
        if ch == False:
            return False
    return True

# Driver Program to test above functions
sentence = input()

if (checkPangram(sentence)):
    print("YES")
# … (else: print("NO") presumably)
```

### Programming Assignment-3: Vowels — private test cases and instructor solution

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `neeru neetu and neeraj` | `neru netu and neraj` |
| 2 | `dsabj dsahjlg dfsabdsaeas asdasdasdssaasa ioioeseaeaoi` | `dsabj dsahjlg dfsabdsas asdasdasdssasa ise` |
| 3 | `three four five` | `thre for five` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

def is_vow(c):

    # this compares vowel with
    # character 'c'
    return ((c == 'a') or (c == 'e') or
            (c == 'i') or (c == 'o') or
            (c == 'u'))

# function to print resultant string
def removeVowels(str):

    # print 1st character
    print(str[0], end = "")

    # loop to check for each character
    for i in range(1,len(str)):

        # comparison of consecutive
        # characters
        if ((is_vow(str[i - 1]) != True) or
            (is_vow(str[i]) != True)):

            print(str[i], end = "")

# Driver code
str= input()
removeVowels(str)
```
