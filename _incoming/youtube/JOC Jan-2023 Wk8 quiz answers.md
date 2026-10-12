# JOC Jan-2023 · Week 8 : Assignment 1

- Source: <https://www.youtube.com/watch?v=VWfLWG7dX-Q> · Techies Talk · published 2023-03-12
- Portal: `noc23_cs20`, due 2023-03-22, 23:59 IST → **Jan-2023 session**
- `[x]` = option ticked by the video author → unverified

**1) Which of the following is not true about Stylometry Analysis?**
- [ ] It is the quantitative study of literature style
- [ ] It is based on the observation that the authors tend to write in relatively consistent and recognizable ways
- [x] any two people may have the same vocabulary
- [ ] It is a tool to study a variety of questions involving style of writing

**2) Which of the following is not true about tuples in python?**
- [ ] Tuple consumes less memory
- [ ] Tuples are immutable
- [x] Tuple supports item deletion
- [ ] Tuples does not support modification

**3) What is the output of the following code snippet in python?**
name =('kiran','bhushan','madan')
print (name[-1])
- [ ] invalid syntax
- [ ] tuple index out of range
- [ ] prints nothing
- [x] madan

**4) Strings in python can be created using**
- [ ] single quotes
- [ ] double quotes
- [ ] triple quotes
- [ ] only A and B
- [x] A, B and C

**5) Networkx in python is used for which of the following operation(s)?**
- [ ] Visualizing social network
- [ ] Analyzing social networks
- [ ] Generate social network
- [x] All of the above
- [ ] None of the above

**6) Which of the following will generate a complete graph in python using the networkx package?**
- [ ] Graph = nx.gnp random graph(25,0.5)
- [x] Graph = nx.gnp random graph(25,1.0)
- [ ] Graph = nx.gnp random graph(25,0.25)
- [ ] Graph = nx.gnp random graph(25,0.75)

**7) Which of the following method will return the RBG value of a pixel in python?**
- [x] getpixel()
- [ ] RBGvalue()
- [ ] pixelValue()
- [ ] none of the above

**8) The degree of separation of a complete graph with n nodes is always**
- [ ] n
- [ ] n-1
- [x] 1
- [ ] 6

**9) Which of the following is true about six degrees of separation?**
- [ ] the minimum degree of separation of any node in the network is 6
- [ ] the maximum degree of separation of any node in the network is 6
- [x] the average degree of separation of the nodes in the network is 6
- [ ] the degree of separation of every node in the network is 6

**10) What is the output of the following code?**

```python
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

mytext = "Have nice day, my friend !!! Programming in Python is fun"
print(sent_tokenize(mytext))
```
- [ ] ['Have nice day, my friend!!! Programming in Python is fun']
- [x] ['Have nice day, my friend!!!', 'Programming in Python is fun']
- [ ] 'Have nice day, my friend!!!'
      'Programming in Python is fun'
- [ ] Error
