# JOC Jul-2023 · Week 11: Assignment 11

- Source: <https://www.youtube.com/watch?v=aAfR3NX0ihU> · Yamini Richhariya · published 2023-10-07 · "The Joy of Computing using Python | NPTEL | Week 11 | assignment solution 11 | 2023" (120 s screen recording)
- Portal: `noc23_cs108`, "Due date: 2023-10-11, 23:59 IST." → **Jul-2023 session**. Each question is 1 point.
- `[x]` = option the author selected. No score is shown. Small text in the video: code line numbers for Q6 and Q7 are partly cut off, marked below.

**Note: use the following convention for the rest of the assignment.**
dd - date
mm - month
yy - year
hh - hour
MM - minutes
ss - seconds
ms - milli-seconds

**1) Which library is used for browser automation?**
- [ ] nltk
- [ ] numpy
- [x] selenium
- [ ] PIL

**2) What the given statement will return?**
```python
time.time()
```
- [x] Time in seconds.
- [ ] Current date and time.
- [ ] Time in minutes
- [ ] The current date, time and year

**3) Identify the library that can be used to get all timezones:**
- [ ] selenium
- [ ] calender
- [ ] nltk
- [x] pytz

**4) The output of the following code will be?**
```python
1  from datetime import datetime as dt
2
3  print(dt.now())
```
- [ ] Date and time in dd- mm-yy hh:MM:ss:ms respectively.
- [ ] Time and date in hh:MM:ss:ms dd- mm-yy respectively.
- [ ] Date and time in mm-dd-yy hh:MM:ss:ms respectively.
- [x] Date and time in yy- mm-dd hh:MM:ss:ms respectively.

**5) We can use the selenium web driver for different browsers.**
- [ ] True
- [x] False

**6) What will be the output of the following code?**
```python
1  import pytz
2  from datetime import datetime as dt
3
4  zone = pytz.all_timezones
5
6  for i in range(len(zone)):
7      print(dt.now(pytz.timezone(zone[i])))
```
- [x] Print the current date and time of all time zones
- [ ] Print the current date and time of specific time zones.
- [ ] Print the current date of all time zones.
- [ ] Print the current date of some specific time zones.

**7) What will be the output if the system date is 10 December 2021(Friday)?**
```python
2  from datetime import datetime as dt
3
4  day = dt.today()
5
6  print(day.weekday())
```
(Line 1 is hidden in the recording.)
- [ ] 5
- [ ] 3
- [x] 4
- [ ] error

**8) Which statement will return the calendar for a whole year?**
- [ ] calendar.month(year)
- [ ] calendar(year)
- [x] calendar.prcal(year)
- [ ] calendar.year(year)

**9) By which statement can we come out of the loop?**
- [ ] continue
- [ ] leave
- [ ] catch
- [x] break

**10) How to check for the leap year?**
- [ ] calendar.leap(year)
- [ ] calendar.is_leap(year)
- [x] calendar.isleap(year)
- [ ] calendar.checkleap(year)
