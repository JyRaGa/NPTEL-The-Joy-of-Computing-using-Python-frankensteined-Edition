# JOC Jan-2023 · Week 11 quiz

- Source: <https://www.youtube.com/watch?v=7UHhXIQ43uk> · Techies Talk · published 2023-04-02
- Portal: `noc23_cs20` → **Jan-2023 session**
- `[x]` = option ticked by the video author → unverified

**1) Which statement will return the calendar for a whole year?**
- [ ] calendar.month(year)
- [ ] calendar(year)
- [x] calendar.prcal(year)
- [ ] calendar.year(year)

**2) By which statement can we come out of the loop?**
- [ ] continue
- [ ] leave
- [ ] catch
- [x] break

**3) What time.time() will return?**
- [x] Time in seconds.
- [ ] Current date and time.
- [ ] Time in minutes
- [ ] The current date, time and year.

**4) Which library used to get all timezones?**
- [ ] selenium
- [ ] calender
- [ ] nltk
- [x] pytz

**5) What is the output of the following code:**

```python
import pytz
from datetime import datetime as dt

zone = pytz.all_timezones

for i in range(len(zone)):
    print(dt.now(pytz.timezone(zone[i])))
```
- [x] Print the current date and time of all time zones.
- [ ] Print the current date and time of specific time zones.
- [ ] Print the current date of all time zones.
- [ ] Print the current date of some specific time zones.

**6) In the page rank algorithm,**
- [ ] We randomly travel from node to node without any relationship.
- [ ] We randomly travel from node to neighbor node.
- [ ] The maximum visited node will be the leader.
- [x] 2 and 3
- [ ] 1 and 3

**7) If we perform the page rank algorithm on the web as a graph, which of the following is true?**
- [x] Websites are nodes, and hyperlinks in websites are edges.
- [ ] Hyperlinks in websites are nodes, and websites are edges.
- [ ] Websites will work as nodes and edges.
- [ ] Hyperlinks will work as nodes and edges.

**8) In the page rank algorithm, the leader is decided by?**
- [ ] A node(person) with a maximum number of outgoing edges.
- [ ] A node(person) with a maximum number of incoming edges.
- [x] A node(person) that is visited maximum times.
- [ ] Can not decide.

**9) Which statement is correct about the following program?**

```python
import random
import matplotlib.pyplot as plt

l = []
count = 0

for i in range(10):
    guess = random.randint(1, 10)
    pick = random.randint(1, 10)

    if(guess!=pick):
        count+=1
        l.append(count)
    else:
        count-=1
        l.append(count)

plt.plot(l)
plt.show()
```
- [ ] The graph will go up when guess and pick are the same.
- [ ] The graph will go down when guess and pick are the same.
- [ ] The graph will go up when guess and pick are not the same.
- [x] Both B and C

**10) Which of the following is not used as conditional statement in Python?**
- [x] switch
- [ ] if...else
- [ ] elif
- [ ] None of the mentioned above
