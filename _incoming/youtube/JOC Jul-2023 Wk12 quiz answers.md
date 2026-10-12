# JOC Jul-2023 · Week 12: Assignment 12

- Source: <https://www.youtube.com/watch?v=Jn3vOnQZ-7U> · Yamini Richhariya · published 2023-10-07 · "The Joy of Computing using Python | NPTEL | Week 12 | assignment solution 12 | 2023" (76 s screen recording)
- Portal: `noc23_cs108`, "Due date: 2023-10-18, 23:59 IST."; "Your last recorded submission was on 2023-10-07, 22:54 IST" → **Jul-2023 session**. Each question is 1 point.
- `[x]` = option the author selected. No score is shown. Q5 and Q7 are graph images, described in text.

**1) What is a sink?**
- [ ] A node with no incoming edges.
- [ ] A node with maximum incoming edges.
- [ ] A node with maximum outgoing edges.
- [x] A node with no outgoing edges.

**2) What should we do when encountering a sink in the case of page rank algorithm?**
- [ ] Stop the algorithm.
- [ ] Start with the last node.
- [x] Randomly choose a node from all nodes.
- [ ] Randomly choose a node from neighbor nodes.

**3) In the page rank algorithm**
- [ ] We randomly travel from node to node without any relationship.
- [ ] We randomly travel from node to neighbor node.
- [ ] The maximum visited node will be the leader.
- [x] B and C
- [ ] A and C

**4) If we perform the page rank algorithm on the web as a graph, which of the following is true?**
- [x] Websites are nodes and hyperlinks in websites are edges.
- [ ] Hyperlinks in websites are nodes and websites are edges.
- [ ] Websites will work as nodes and edges.
- [ ] Hyperlinks will work as nodes and edges.

**5) Identify the type of graph:**
(Image: two end nodes each joined by a long edge to a chain of nodes that sags in the middle, with a short branch at each end, like a "barbell" outline.)
- [ ] Triangle Graph
- [ ] Directed Graph
- [x] Barbell Graph
- [ ] Wheel graph

**6) Which of the following python function will return random floating point number between 0 and 1?**
- [ ] random.float()
- [ ] random.randomfloat()
- [ ] random.frandom()
- [x] random.random()

**7) What will be the G.out_degree(3) for the following graph(G) ?**
(Image: a directed graph of 8 labelled nodes with arrowheads on the edges; node 3 is the busy node near the centre.)
- [ ] 4
- [x] 5
- [ ] 3
- [ ] 6

**8) In the page rank algorithm the leader is decided by?**
- [ ] A node(person) with maximum number of outgoing edges.
- [ ] A node(person) with maximum number of incoming edges.
- [x] A node(person) which is visited maximum times.
- [ ] Can not decide.

**9) Which of the following is true about directed graphs?**
- [ ] One can come back and forth from one node to another using a single edge.
- [x] One can only go forward from one node to another using a single edge.
- [ ] One can go to any node from one node using one edge.
- [ ] None of the above.

**10) What will be the output of the following code?**
```python
1  word = 'Hey there!'
2  print(list(word))
```
- [ ] ['Hey', 'there', '!']
- [ ] ['Hey', 'there', ' ', '!']
- [x] ['H', 'e', 'y', ' ', 't', 'h', 'e', 'r', 'e', '!']
- [ ] ['H', 'e', 'y', 't', 'h', 'e', 'r', 'e', '!']
