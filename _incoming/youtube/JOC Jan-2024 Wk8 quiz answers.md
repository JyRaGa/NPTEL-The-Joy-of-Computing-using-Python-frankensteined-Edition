# JOC Jan-2024 · Week 8: Assignment 8

- Source: <https://www.youtube.com/watch?v=3_AXZxtRR_s> · Techies Talk · published 2024-03-16
- Portal: `noc24_cs57`, due 2024-03-20, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked by the video author before submitting → unverified (only "Thank you for taking the Week 8 : Assignment 8." is shown, no score)

**1) Which of the following statements about tuples in Python is correct?**
- [ ] Tuples are mutable, allowing modification of individual elements after creation.
- [ ] Tuples are enclosed in square brackets [ ], similar to lists.
- [x] Tuples are immutable, meaning their elements cannot be changed after creation
- [ ] Tuples can only contain elements of the same data type.

**2) Tuples share a close resemblance to lists. They can be indexed and sliced just like lists. The main point of difference between lists and tuples is that tuples cannot be updated in-place. Elements in a tuple cannot be deleted. Which of the following statements are true about Tuples:**
- [x] A tuple can hold mutable objects.
- [x] Tuples can be nested.
- [x] A list can be converted into a tuple and vice versa.
- [x] A tuple can hold a non-homogeneous sequence of items, viz. **a_tuple = (1, 'cool', True).**

**3) Which of the following best describes the role of  matplotlib.pyplot  in Python's matplotlib library for data visualization?**
- [x] It is used for creating figures, plots, adding labels, and other visual elements to create visualizations.
- [ ] It primarily handles numerical computations and statistical analyses for data visualization.
- [ ] It manages data structures and handles data manipulation before visualization.
- [ ] It is responsible for creating interactive visualizations and animations.

**4) The following paragraph is an excerpt from a talk given by Guido:**

**In reality, programming languages are how programmers express and communicate ideas — and the audience for those ideas is other programmers, not computers. The reason: the computer can take care of itself, but programmers are always working with other programmers, and poorly communicated ideas can cause expensive flops. In fact, ideas expressed in a programming language also often reach the end users of the program — people who will never read or even know about the program, but who nevertheless are affected by it.**
**Text processing plays an important role in analysing text data. Given a piece of text, which of the following piece of code determines if how many words are there in the text?**

**Note: 1. Choose the nearest best option. 2. Special Characters are not counted as words.**

```python
text = "In reality, programming languages are how programmers express and communicate ideas — and the audience for those ideas is other programmers, not computers. The reason: the computer can take care of itself, but programmers are always working with other programmers, and poorly communicated ideas can cause expensive flops. In fact, ideas expressed in a programming language also often reach the end users of the program — people who will never read or even know about the program, but who nevertheless are affected by it."
sentences = text.split('.')
while '' in sentences:
    sentences.remove('')
print(len(sentences))
words = [ ]
for sentence in sentences:
    words_ = sentence.split(' ')
    words.extend(words_)
print(len(words))
proc_words = [ ]
for word in words:
    if not(word == '' or word == '—'):
        proc_words.append(word)
print(len(proc_words))
u_words = dict()
for word in proc_words:
    if word not in u_words:
        u_words[word] = 0
    u_words[word] += 1
print(len(u_words))
```
- [ ] Option 1
  ```python
  while '' in sentences:
      sentences.remove('')
  print(len(sentences))
  ```
- [x] Option 2
  ```python
  words = [ ]
  for sentence in sentences:
      words_ = sentence.split(' ')
      words.extend(words_)
  print(len(words))
  ```
- [ ] Option 3
  ```python
  proc_words = [ ]
  for word in words:
      if not(word == '' or word == '—'):
          proc_words.append(word)
  print(len(proc_words))
  ```
- [ ] Option 4
  ```python
  u_words = dict()
  for word in proc_words:
      if word not in u_words:
          u_words[word] = 0
      u_words[word] += 1
  print(len(u_words))
  ```

---

**Code for question 5 & 6:**

```python
def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for i in word1:
        if word1.count(i) != word2.count(i):
            return False
    return True
```

**5) How does the given code check if two strings are anagrams?[MSQ]**
- [x] Compares the lengths of the two input strings. If they are equal, it proceeds to check the character counts in each string.
- [ ] Using a loop to count the occurrence of character present at even places in both strings.
- [x] Iterates through each character in word1 and compares the count of that character in both word1 and word2. If the counts match for all characters, the strings are considered anagrams
- [ ] Compares the lengths of the two input strings. If they are not equal, it proceeds to check the character counts in each string

**6) If two strings are anagrams, what would be the output of the above code? [MSQ]**
- [x] The output in case of **anagram("listen", "silent")** is **True**
- [x] A Boolean Value
- [ ] The output in case of **anagram(""hello", "world")** is **True**
- [x] The output in case of **anagram("race", "care")** is **True**

**7) Consider the tuple colors = ('red', 'green', 'blue'). What is the result of colors + ('purple')?**
- [ ] **('red', 'green', 'blue', 'purple')**
- [x] **TypeError:** can only concatenate tuple (not "str") to tuple ('red', 'green', 'blue')
- [ ] **('red', 'green', 'blue', 'red', 'green', 'blue', 'purple')**
- [ ] **('red', 'green', 'blue')**

**8) Which statement accurately describes the use of VADER and DataFrames in sentiment analysis?**
- [ ] VADER is a machine learning-based tool used with DataFrames to analyze sentiment in images.
- [x] VADER is a lexicon and rule-based sentiment analysis tool often used with Pandas DataFrames to assess sentiment in text data.
- [ ] DataFrames are used to visualize sentiment analysis results, while VADER is a Python visualization library.
- [ ] VADER and DataFrames are used in data preprocessing, not specifically in sentiment analysis tasks.

**9) Statement 1: The method used for flipping the image in the PIL library is transpose(parameter)?**
**Statement 2: CLAHE (Contrast Limited Adaptive Histogram Equalization) is favoured over AHE (Adaptive Histogram Equalization) for its advantage in handling noise**
- [ ] Only one of the above two statements are correct
- [ ] Both statements are correct
- [x] Both statements are incorrect
- [ ] Insufficient information to determine the correctness of both statements.

**10) Consider the following snippet of code.**

```python
word_string = 'abcd'
word_list = ['a', 'b', 'c', 'd']
word_tupple = ('a', 'b', 'c', 'd')
```
**Which of the following snippets of code will throw an error?**
- [ ] Option 1
  ```python
  word_list[0] = 'z'
  print(word_list)
  ```
- [x] Option 2
  ```python
  word_string[0] = 'z'
   print()
  ```
- [x] Option 3
  ```python
  word_tupple[0] = 'z'
  ```
- [ ] All are correct
