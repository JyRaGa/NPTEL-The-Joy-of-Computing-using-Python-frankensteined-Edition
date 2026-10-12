# JOC Jul-2022 · Week 8: Assignment 8

- Source: <https://www.youtube.com/watch?v=Hd21O2JTwKo> · Techies Talk · published 2022-09-12
- Portal: `noc22_cs122`, due 2022-09-21, 23:59 IST → **Jul-2022 session**
- `[x]` = option ticked by the video author before submitting → unverified

**1) Which of the following q43 the correct representation of tuples?** *(sic — "q43" as printed on the portal)*
- [ ] [1,2,3,4]
- [x] (1,2,3,4)
- [x] ((1), (2), (3), (4))
- [ ] [[1], [2], [3], [4]]

**2) Why gambling is not recommended?**
- [ ] Because you lose every time.
- [ ] Because you win every time.
- [x] Because the loss amount is greater than the winning amount over time.
- [ ] Because the winning amount is greater than the loss amount over time.

**3) Which of the following programs will print the exact same word?**

- [x] Option 1
  ```python
  word = 'nptel'
  new = ''

  for i in word:
      j = ord(i)
      k = (((j+26) - 97) % 26) + 97

      new = new+chr(k)

  print(new)
  ```
- [ ] Option 2
  ```python
  word = 'nptel'
  new = ''

  for i in word:
      j = ord(i)
      k = (((j+26)) % 26)

      new = new+chr(k)

  print(new)
  ```
- [x] Option 3
  ```python
  word = 'nptel'
  new = ''

  for i in word:
      j = ord(i)
      k = (((j) - 97) % 26) + 97

      new = new+chr(k)

  print(new)
  ```
- [ ] Option 4
  ```python
  word = 'nptel'
  new = ''

  for i in word:
      j = (i)
      k = (((j+26) - 97) % 26) + 97

      new = new+(k)

  print(new)
  ```

**4) Using which of the following methods a person can store over a million images in small digital storage?**
- [ ] Decompression
- [x] Compression
- [ ] Enhancement
- [ ] Unzip

**5) State True or False, A lot of information can be revealed from images by using the right kind of enhancement.**
- [x] True
- [ ] False

**6) type(10) will return?**
- [x] int
- [ ] str
- [ ] float
- [ ] list

**7) Which of the following pair of words are anagrams?**
- [x] A gentleman, Elegant man
- [ ] Cat, Arc
- [x] Looted, Toledo
- [ ] Monasteries, Aman stories

**8) Using PIL how an image 'img' can be flipped?**
- [x] img.flip()
- [ ] img.rotate()
- [ ] img.transpose()
- [ ] img.turn()

**9) What is the purpose of NLTK?**
- [ ] To process binary language.
- [ ] To process foreign language.
- [x] To process human language.
- [ ] To process only Hindi language

**10) How does Vader help in sentiment analysis?**
- [ ] It calculates whether the statement is negative, positive, or neutral.
- [ ] It takes care of the intensity of a statement.
- [x] Both A and B
- [ ] None of the above
