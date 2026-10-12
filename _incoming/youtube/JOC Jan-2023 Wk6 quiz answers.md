# JOC Jan-2023 · Week 6 : Assignment 1

- Source: <https://www.youtube.com/watch?v=V9Idm5UwI38> · Techies Talk · published 2023-02-27
- Portal: `noc23_cs20`, due 2023-03-08, 23:59 IST → **Jan-2023 session**
- `[x]` = option ticked by the video author → unverified

**1) Which of the following is true about recursion?**
- [ ] Recursion always performs better than non-recursive code.
- [x] Recursive code can be reused.
- [x] The base case is necessary for recursion.
- [x] Recursive code can be shorter than non-recursive code

**2) If PYTHON is encoded by TCXLSR then DIAMOND will be encoded as?**
- [ ] EJBNPOE
- [ ] FKCORPF
- [ ] HMERTSH
- [x] HMEQSRH

**3) Let L be a list containing different names of movies. Which statement is correct to select a random movie name from that list L?**
- [x] random.choices(L)
- [ ] random.select(L)
- [ ] random.movie(L)
- [ ] random.random(L)

**4) In the list L = [4,6,7,4,6,2,1], What is the index of element '7'?**
- [ ] 0
- [ ] 1
- [x] 2
- [ ] 3

**5) What will be the output of the following code?**

```python
import string

def shift(word,value):

    letters = string.ascii_lowercase
    new = ''

    for i in range(len(word)):

        if word[i] in letters:

            index = letters.index(word[i])
            new = new + letters[(index+value)%26]

        else:

            new = new + word[i]

    return new
```
- [x] Shift every letter in a given word by value.
- [ ] Shift every letter in a given word by 1.
- [ ] Shift every letter in a given word by 26.
- [ ] Returns the same word.

**6) Library used to import images?**
- [x] PIL
- [ ] Imageview
- [ ] IMG
- [ ] image

**7) Values of CSV files are separated by?**
- [x] Commas
- [ ] Colons
- [ ] Semi-colons
- [ ] Slash

**8) what will be the output of the following program?**

```python
def recursive(num):

    if(num==1):
        print('*')
        return

    if(num%2 == 0):
        print('*'*num)
        recursive(num-1)
        return
    else:
        recursive(num-1)
        return

recursive(10)
```
- [ ] Option 1
  ```
  **********
  *********
  ********
  *******
  ******
  *****
  ****
  ***
  **
  *
  ```
- [ ] Option 2
  ```
  *********
  *******
  *****
  ***
  *
  ```
- [ ] Runs into infinite loop
- [x] Option 4
  ```
  **********
  ********
  ******
  ****
  **
  *
  ```

**9) What will happen if we don't check for a base case in recursion.**
- [ ] The program will run smoothly
- [ ] The program will return a wrong output.
- [x] The program will enter into an infinite loop.
- [ ] The program will never run.

**10) Which of the following is true about recursion?**
- [ ] Recursion increases the speed of the program.
- [x] Recursion decreases the speed of the program.
- [ ] Speed of the program remains the same.
- [ ] Recursion is easier to understand than non-recursive programs.
