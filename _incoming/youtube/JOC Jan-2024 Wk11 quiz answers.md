# JOC Jan-2024 · Week 11: Assignment 11

- Source: <https://www.youtube.com/watch?v=A4tKYxGvs1U> · Study_Ease · published 2024-04-01
- Portal: `noc24_cs57`, due 2024-04-10, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked / value entered by the video author ("Your last recorded submission was on 2024-04-02, 02:08 IST") → unverified, no score shown

**1) Select the correct statement regarding selenium library**
- [ ] Selenium is primarily used for web browser automation
- [ ] The web driver in selenium allows a way to interact with web browsers
- [ ] The Keys Class provides a set of special keys that can be used for keyboard interaction
- [x] All of the above

**2) Which of the following tasks in WhatsApp can be automated using selenium?**
- [x] Sending Media Files
- [x] Reading Messages
- [x] Creating and Managing Groups
- [x] Updating Profile Information

**3) Read the given code and identify the correct statement.**

```python
1  import pytz
2
3  def does_something():
4      variable = [tz for tz in pytz.all_timezones if tz.startswith('Asia')]
5      return variable
6
7  x = does_something()
8  for _ in x:
9      print(_)
10
```
- [ ] does_something returns a list of all time zones in Asia
- [ ] the above code prints all time zones in Asia
- [ ] The output of the code can change depending on the version of pytz used
- [x] All of the above

**4) Read the given code. What is the output of does_something(2022,2,29).(NAT)**

```python
import calendar

def does_something(year, month, day):
    variable = calendar.monthrange(year,month)

    return int(1<= day<= variable[1])
```
Answer entered: `0`

**5) Read the given code.**

```python
def checks_something(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Read years from a text file
file_path = 'years.txt'
with open(file_path, 'r') as file:
    years = [int(line.strip()) for line in file]


count = sum(1 for year in years if checks_something(year))
```
**Assume the file years.txt contains the following data.**

```
2000
2007
2004
2009
2001
```
**What is the output of the code (NAT)**

Answer entered: `2`

**6) Read the given code.**

```python
1  import calendar
2
3  def count_something(year):
4      count = 0
5
6      for month in range(1, 13):
7
8          day_of_week = calendar.weekday(year, month, 13)
9          if day_of_week == calendar.FRIDAY:
10             count += 1
11
12     return count
13
```
**Enter the value of int(count_something(1996)==count_something(2024))**

Answer entered: `1`

**7) Read the given code.**

```python
1  def count_(s, e):
2      count = 0
3
4      for year in range(s, e + 1):
5          if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
6              count += 1
7
8      return count
```
**Enter the value returned by count_(1990,2024)**

Answer entered: `9`

**8) In addition to the first birthday celebration, Koreans often celebrate "MiSeDol," which marks the completion of the 100th day after a baby's birth. This is considered another significant milestone. Given an input birthdate, the following code tries to calculate the date of "MiSeDol", but the code might contain errors. Identify the line number corresponding to the error. In the absence of an error answer -1.**

```python
1  from datetime import datetime,timedelta
2
3  def calculate_(year, month , day):
4
5      input_date = datetime(year, month, day)
6      date= input_date +timedelta(days=99)
7
8      year =date.year
9      month=date.month
10     day=date.day
11
12     return year, month ,day
13
```
Answer entered: `-1`

**9) Read the given code.**
**Find the value returned by finds_something (2000,12)**

```python
import calendar

def finds_something(year, month):
    first_day_of_month = calendar.weekday(year,month,1)

    x=(first_day_of_month+1)%7

    return x
```
Answer entered: `5`

**10) Read the following code. What does count_something(2024,1) return ?**

```python
import calendar
def count_something(year, month):
    x,y=calendar.monthrange(year,month)
    last_day=y
    count=0
    for day in range(1, last_day+1):
        if calendar.weekday(year,month,day)<5 :
            count+=1

    return count
```
Answer entered: `23`
