# JOC Jul-2019 · Week 11 · Assignment 11

- Source: <https://www.youtube.com/watch?v=2JomiVxHvQM> · Ultimate Gamer · published 2019-10-10
- Portal: "Your last recorded submission was on 2019-10-10, 20:16 IST" (the due date is cut off at the frame edge) → **Jul-2019 session** (by upload/submission date)
- `[x]` = option selected by the author; the page shows "Thank you for taking the Assignment 11." → submitted, but no score shown, so unverified.

**1) The function isleap() in the calendar module in Python returns**
- [ ] integer value
- [x] boolean value
- [ ] float value
- [ ] None of the above

**2) What is the output of the following program?**
```
import calendar
yy = 2017
mm = 11
print(calendar.month(yy, mm))
```
- [ ] displays the calendar of the month November
- [ ] displays the calendar of the year 2017
- [ ] displays the calendar of the month November, 2019
- [x] displays the calendar of the month November, 2017

**3) In the question above, if the user wants to display the calendar of the year 2017, then which of the following functions should he use?**
- [ ] calendar.year()
- [ ] calendar.month(2017)
- [x] calendar.calendar(2017)
- [ ] calendar.year(2017)

**4) What is the output of the code shown below if the system date is 18th June, 2017(Thursday)?**
```
tday=datetime.date.today()
print(tday)
```
- [ ] 18
- [ ] 2017-06
- [ ] 3
- [x] 2017-06-18

**5) State True or False.**
**Selenium is an open source tool which is used for automating the test cases carried out on web browsers.**
- [x] True
- [ ] False

**6) State True or False**
**Selenium is required if you want to use remote WebDriver.**
- [x] True
- [ ] False

**7) Which of the following methods is used to locate an element in a webpage?**
- [ ] find_element_by_id()
- [ ] find_element_by_link_text()
- [ ] find_element_by_class_name()
- [x] All of the above

**8) What is the use of xpath in selenium?**
- [x] xpath is used to find the web element in webpage
- [ ] xpath is used to get link text of the web element in webpage
- [ ] xpath is used to find the webpage
- [ ] xpath is used as an address to a webpage

**9) Which of the following is not a valid webdriver class?**
- [ ] webdriver.ActionChains
- [ ] webdriver.Firefox
- [x] webdriver.HtmlUnit
- [ ] webdriver.Chrome

**10) Which of the following platforms does Selenium support?**
- [ ] Linux
- [ ] Mac OS X
- [ ] IOS
- [x] All of the above

---

## ✅ Official accepted answers and programming assignments (portal review page)

- Source: <https://www.youtube.com/watch?v=rL5-U3DybJk> · Dr Thulasi Bikku · published 2024-03-29 (`noc19_cs41` portal after the deadline; that account submitted on 2019-10-12, 12:56 IST).
- **Accepted answers seen:** Q1 boolean value · Q2 displays the calendar of the month November, 2017 (selected) · Q3 calendar.calendar(2017) · Q4 2017-06-18 · Q5 True · Q6 True · Q7 All of the above · Q8 xpath is used to find the web element in webpage. **All match the ticks above.** Q9 and Q10 were not shown.

### Programming Assignment-1: Marks distribution

Given a list **A** of **n** elements, representing the marks. There are **m** students and you have to dis[tribute the marks from the] list **A** to **m** students such that:

1) Each student gets marks.
2) The difference between the maximum marks and minimum marks given to the students is mi[nimised].

**Input Format:**
The first line contains the value **n** and **m** respectively separated by a space.
The second line contains the elements of list **A** separated by a space

**Output Format:**
Print the minimum difference

Example:

Input:
7 3
7 3 2 4 8 12 56

Output:
2

Explanation:
We need to pick 3 marks for three students (m=3). If we pick 2, 3 and 4, the difference is minim[um …]

(The private test cases are huge lists of six-digit numbers, so they are not transcribed. The instructor solution was not visible behind them.)

### Programming Assignment-2: String Sort

Write a program that accepts a comma-separated sequence of words as input and prints the wo[rds in a comma-separated] sequence after sorting them alphabetically.

**Input Format:**
The first line of input contains words separated by the comma.

**Output Format:**
Print the sorted words separated by the comma.

Example:

Input:
without,hello,bag,world

Output:
bag,hello,without,world

Private test inputs: `cheerfully,send,you,the,twenty,dollars` · `singular,that,the,plaintiff,should,have,let,you,forget,it,so,long` · `still,you,do,not,work,much,merely,because,it,does,not,seem,to,you`

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

items=[x for x in input().split(',')]
items.sort()
print (','.join(items))
```

### Programming Assignment-3: Push the zero

Write a Python program to push all zeros to the end of a given list **a**. The order of the elem[ents …]

Input Format:
Elements of the list **a** with each element separated by a space.

Output Format:
Elements of the modified list with each element separated by a space. After the last eleme[nt there should be no] space.

Example:

Input:
0 2 3 4 6 7 10

Output:
2 3 4 6 7 10 0

Explanation:
There is one zero in the list. After pushing it at the end the elements of the list becomes 2 [3 4 6 7 10 0 …]

| Test case | Input | Expected Output |
|---|---|---|
| 1 | `2 1 0 9 1 8` | `2 1 9 1 8 0` |
| 2 | `19 12 0 61 2 8 0 7 12 8 3 0 6 2 1 0 2` | `19 12 61 2 8 7 12 8 3 6 2 1 2 0 0 0 0` |
| 3 | `12 98 0 43 0 23 0 76 0 12 0 76 0 3 0 4 3 5 6 0 1 0 4 6 2 9` | `12 98 43 23 76 12 76 3 4 3 5 6 1 4 6 2 9 0 0 0 0 0 0 0 0 0` |

Sample solutions (Provided by instructor):
```python
"""

@author: descentis
"""

def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)

num_list = list(map(int, input ().split ()))

res = move_zero(num_list)

for i in range(len(res)):
    if(i==len(res)-1):
        print(res[i],end="")
    else:
        print(res[i],end=" ")
```
