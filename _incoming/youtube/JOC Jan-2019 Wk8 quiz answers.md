# JOC Jan-2019 · Week 8: Cool Ideas(Part 6) · Assignment 8

- Source: <https://www.youtube.com/watch?v=XcdzKQBoX_E> · Ultimate Gamer · published 2019-03-26 (titled "#CORRECTED", a re-upload)
- Portal: "Due date for this assignment: 2019-03-27, 23:59 IST."; "Your last recorded submission was on 2019-03-27, 00:00 IST" → **Jan-2019 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown). Video ends with "…not guarantee that these solutions are 100%…". Alternate videos for this week (not transcribed): Study Fun `9zzZPlAfn58`, Amanpal Singh `LKKgq9LIm60`.

**1) Which of the following statements is correct about NLTK?**
- [ ] NLTK stands for Natural Language Tooling Kit.
- [x] NLTK is used for language processing.
- [ ] NLTK can be used to process images.
- [ ] All of the above

**2) Which of the following does CLAHE use to enhance the images?**
- [x] Histogram Equalisation
- [ ] Median Filtering
- [ ] Mask Filtering
- [ ] None of the above.

**3) Predict the sentiment of the statement below.**
**SCCI labs of IIT Ropar deals with research areas related to Social Computing.**
- [ ] Positive
- [ ] Negative
- [x] Neutral

**4) State True or False.**
**Sum of ascii values of two anagrams is always same.**
- [x] True
- [ ] False

**5) State True or False.**
**If the sum of ASCII values of two strings is same, then these two strings are anagrams.**
- [ ] True
- [x] False

**6) Which of the following matrices has transpose same as the matrix itself?**
- [x] Identity Matrix
- [ ] Zero Matrix
- [ ] Either A or B
- [ ] Both Aand B

> ⚠ Doubtful: a square zero matrix is also symmetric (its transpose equals itself), so **Both A and B** looks more correct.

**7) Which of the following statements is true in case of tuple t=(10,20,30,90)?**
- [ ] t[4]=40
- [ ] t[3]=40
- [ ] t[len(t)-1]=40
- [x] None of the above

**8) What is the output of the following statement if tuple t=(1,2,3,4)?**
```
t[1:]
```
- [x] (2,3,4)
- [ ] (1,2,3,4)
- [ ] (3,4,1)
- [ ] (1,2,3)

**9) Consider the scenario below:**
**Ram wants to play a lottery game in which he has to choose one ticket out of 10 tickets. If the ticket chosen by the participant is 9, then he wins 500$. The price for playing the lottery game is 100$. Ram decides to play this game 10 times in order to guarantee his win. Would you advise him to play this game?**
- [ ] Yes
- [x] No
- [ ] Can't say

**10) Find out the anagrams present in the following sentences.**
**One day, When I was going through my old stuff, I found my old study table. Though It was damn dusty, but still i could read the stupid stuff that i used to write on it as a kid.**
- [ ] year and ear
- [ ] night and thing
- [x] dusty and study
- [ ] There is no anagram present in the given sentences.

---

## Second source and programming assignments: Amanpal Singh

- Source: <https://www.youtube.com/watch?v=LKKgq9LIm60> · Amanpal Singh · published 2019-03-24 ("Joy of computing using Python nptel assignment 8 [all soutions] March 2019") · `noc19_cs09`; "Your last recorded submission was on 2019-03-24, 21:31 IST"; quiz due 2019-03-27, 23:59 IST.
- **Quiz:** same ticks as Ultimate Gamer **except Q6: Amanpal ticked "Both A and B"**, which supports the note above (a zero matrix is also symmetric). No score was shown.
- All three programming assignments show **"3 out of 3 tests passed. You scored 100.0/100."** The statements are the same as Jul-2019 Week 8 (Vowels, Panagrams, Duplicate Elements); see that file for the full text.

### Programming Assignment-3: Vowels — author's code (100/100)
```python
#Checking for the vowels
def is_vow(c):
    return ((c=='a') or (c=='e') or (c=='i') or (c=='o') or (c=='u'))

#Finding consecutive two non vowels/ concenent
def uniq(s):
  print(s[0],end="") #printing first element
  l=int(len(s))
  for i in range(1,l):
    if ((is_vow(s[i-1]) != True) or  ((is_vow(s[i])) != True)):
        print(s[i],end="")

s=input()
uniq(s)
```

### Programming Assignment-2: Panagrams — author's code (100/100)
```python
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
    print ("YES",end="")
else:
    print ("NO", end="")
```

### Programming Assignment-1: Duplicate Elements — author's code (100/100)
```python
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

l=[int (j) for j in input().split()]
l=uniq(l)
for i in l:
    print(i,end=" ")
```
