# JOC Jul-2022 · Week 5: Assignment 5

- Source: <https://www.youtube.com/watch?v=jFx3_F4KK8s> · Techies Talk · published 2022-08-22
- Portal: `noc22_cs122`, due 2022-08-31, 23:59 IST → **Jul-2022 session**
- `[x]` = option ticked by the video author before submitting → unverified

**1) What is the correct way to initialize a dictionary?**
- [ ] D = {a-10, b-20, c-30}
- [ ] D = {'a'-10, 'b'-20, 'c'-30}
- [ ] D = {a:10, b:20, c:30}
- [x] D = {'a':10, 'b':20, 'c':30}

**2) What is the correct syntax to get all the keys only from a dictionary d?**
- [ ] d.key()
- [ ] d.item()
- [ ] d.value()
- [x] d.keys()

**3) Which of the following statements are true about dictionaries in python?**
- [x] The keys of a dictionary must be unique values.
- [ ] The keys of a dictionary can or cannot be unique.
- [ ] The values of a dictionary must be unique values.
- [x] The values of a dictionary can or cannot be unique.

**4) State True or False: In the monte hall problem, swapping the choice does not increase the chance of winning.**
- [ ] True
- [x] False

**5) In dictionaries, d.items() will return _**
- [x] Pairs of all (key, value) together.
- [ ] All (keys) and (values) separately.
- [ ] All (values) and (keys) separately.
- [ ] Pairs of all (value, key) together.

**6) What will be the output of the following program?**

```python
import string
import random

a = string.ascii_lowercase
d = {}

for i in range(26):

    index = random.randint(0, 25)
    try:
        d[a[index]]+=1

    except KeyError:
        d[a[index]] = 0

print(d)
```
- [ ] A dictionary with all letters as keys and 0 as values.
- [ ] A dictionary with some letters as keys and 0 as values.
- [ ] A dictionary with all letters as keys and some random numbers as values.
- [x] A dictionary with some letters as keys and some random numbers as values.

**7) Binary search can be applied on ___.**
- [x] Sorted list in ascending order.
- [ ] Unsorted list
- [ ] Both A and B
- [x] Sorted list in descending order

**8) Which error is encountered while accessing a position that is not present in a list?**
- [ ] KeyError
- [x] IndexError
- [ ] RunTimeError
- [ ] ValueError

**9) Which of the following command is correct to delete a key from a dictionary 'd'?**
- [x] d.pop('key')
- [ ] d.del('key')
- [ ] d.remove('key')
- [ ] d.delete('key')

**10) Which of the following is/are correct regarding dictionaries?
1) One can make a dictionary inside a dictionary in python.
2) Keys in the dictionary are mutable.**
- [ ] Option 1 is correct, option 2 is correct. Option 2 is the correct explanation for option 1.
- [x] Option 1 is correct, option 2 is incorrect. Option 2 is not the correct explanation for option 1.
- [ ] Option 1 is correct, option 2 is correct. Option 2 is not the correct explanation for option 1.
- [ ] None of these
