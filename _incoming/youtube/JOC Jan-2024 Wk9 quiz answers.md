# JOC Jan-2024 · Week 9: Assignment

- Source: <https://www.youtube.com/watch?v=NPMo-6uvU60> · Study_Ease · published 2024-03-22
- Portal: `noc24_cs57`, due 2024-03-27, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked / value entered by the video author before submitting → unverified (video ends at "Submit Answers", no score)
- Note: this assignment has 11 questions.

**1) What is stylometry?**
- [ ] The study of language evolution
- [x] The study of linguistic style in written texts
- [ ] The study of speech patterns in public speaking
- [ ] The study of language acquisition in children

**2) What are the different attributes that can be checked in addition to average word length to identify the style of a particular author? (MSQ)**
- [x] Punctuation usage
- [x] Word Frequency
- [x] Usage of Stylistic Devices like Metaphors, Similes, etc
- [x] Average Sentence Length

**3) The following code tries to perform natural language analysis for a small piece of text without using the nltk (Natural Language Toolkit) library.**

```python
1  text = " Natural Language Processing Using Python "
2  words = text.split()
3  x= [len(word) for word in words]
4  y =sum(x)
5  z = y/ len(x)
6
7  print(y,z)
8
```
**Select all the correct statements (MSQ)**
- [x] y represents the sum of length of words in text
- [x] z represents the average word length of text
- [x] x represents a list where each index of the list corresponds to the length of the corresponding word in text
- [x] The output of the code is: 36 7.2

**4) The following code tries to calculate average sentence length of a given block of text in the form of a file, assuming that the sentences always end with full stops and that there are no ellipsis(...) in the block of text. But the code might contain errors. Identify the line number corresponding to the error. In the absence of an error input your answer as -1(NAT)**

```python
1  file_name =input()
2  with open(file_name, 'r') as file :
3      text = file.read()
4  no_of_words = [len(sentence.strip().split()) for sentence in text.split('.') if sentence.strip()]
5  average_length =sum(no_of_words)/len(text)
6  print('Average Sentence Length', average_length)
7
```
Answer entered: `5`

**5) What does the following code do?**

```python
1  import networkx as nx
2  import random
3
4  G = nx.Graph()
5
6  for node in range(1,6):
7      G.add_node(node)
8
9  while(len(G.edges())!=10):
10     node1, node2 = random.sample(range(1,6),2)
11     G.add_edge(node1, node2)
12
13 print(G.nodes())
14 print(G.edges())
15
```
- [x] A graph having 5 nodes which are integers from 1 to 5 and 10 edges in total is created and the edges and nodes of the graph are printed
- [ ] A graph having 6 nodes which are integers from 1 to 6 and 10 edges in total is created and the edges and nodes of the graph are printed
- [ ] A graph having 5 nodes which are integers from 1 to 5 and 9 edges in total is created and the edges and nodes of the graph are printed
- [ ] A graph having 6 nodes which are integers from 1 to 6 and 9 edges in total is created and the edges and nodes of the graph are printed

**6) You are analysing a social network where individuals are represented as nodes, and friendships are represented as edges. What would be the most appropriate graph property to study to identify influential individuals in the network?**
- [x] Node degree
- [ ] Graph density
- [ ] Graph diameter
- [ ] Edge weight

**7) In the "small world experiment" conducted by Stanley Milgram, participants were asked to send a letter to a target person through acquaintances. What was the average number of intermediaries required for the letters to reach the target?**
- [ ] 1 degree
- [ ] 3 degrees
- [x] 6 degrees
- [ ] 10 degrees

**8) Given a file with edges of the graph, and each line representing an edge in the format "node 1 node 2", the following code attempts to plot a graph based on the data given. But the code might contain errors. Identify the line number corresponding to the error. In the absence of an error type your answer as -1.**

```python
1  import networkx as nx
2  import matplotlib.pyplot as plt
3
4  def load_graph_from_file(file):
5      G = nx.Graph()
6      with open(file, 'r') as file:
7          for line in file:
8              nodes = line.strip().split()
9              node1 = int(nodes[0])
10             node2 = int(nodes[1])
11             G.add_edge(node1, node2)
12     return G
13
14 nx.draw(graph, with_labels=True, font_weight='bold')
15 plt.show()
```
Answer entered: `14`

**9) Using the ideas from Area Calculation discussed in the lecture, we are trying to estimate the area of a quarter circle embedded in a square. Identify the line number corresponding to the error(if any) in the absence of error type your answer as -1**

(Image: a square with a blue quarter circle centred at the bottom-left corner, green area outside the arc)

```python
1  import random
2  # Parameters
3  num_points = 10000
4  radius = 1.0
5  # Function to check if a point is inside the quarter circle
6  def is_inside_quarter_circle(x, y, radius):
7      return x**2 + y**2 <= radius**2 and x >= 0 and y >= 0
8  # Monte Carlo simulation for area estimation of a quarter …   ← end of comment hidden by a watermark
9  def estimate_area_quarter_circle(num_points, radius):
10     inside_points = 0
11     for _ in range(num_points):
12         x = random.uniform(0, radius)
13         y = random.uniform(0, radius)
14         if is_inside_quarter_circle(x, y, radius):
15             inside_points += 1
16     area_ratio = inside_points / num_points
17     estimated_area = area_ratio * (radius)**2
18     return estimated_area
```
Answer entered: `-1`

**10) Select the correct statements regarding area calculation using the method discussed in the lecture (MSQ)**
- [x] The main advantage of the method is that it can handle area calculation even for irregular shapes
- [ ] The main advantage of the method is that it is computationally efficient for all scenarios
- [x] Increasing the number of random points reduces the impact of random variations and provides a more stable and accurate estimate of area
- [x] Increasing the number of random points improves accuracy of estimation as it converges the average value to the true value according to law of large numbers

**11) Select the correct statement regarding the PIL library**
- [ ] PIL stands for Python Image Library
- [ ] Pillow is the active successor of PIL
- [ ] Image.open() is used to open images in PIL
- [x] All of the above
