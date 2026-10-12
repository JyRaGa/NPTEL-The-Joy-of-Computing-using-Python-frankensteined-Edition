# JOC Jul-2023 · Week 9: Assignment 9

- Source: <https://www.youtube.com/watch?v=jYMEaOBxzCc> · MY SWAYAM · published 2023-09-15 (190 s screen recording)
- Portal: `noc23_cs108`, "Your last recorded submission was on 2023-09-16, 10:04 IST" (the due date is cut off at the right edge) → **Jul-2023 session**. Each question is 1 point.
- `[x]` = option the author selected (visible for Q1, Q2, Q3, Q6, Q7 only). No score is shown.
- Q4, Q5 and Q6 are graph images; their options and figures are described in text (edges read from the pictures).

**1) How can we identify which book is written by which author?**
- [ ] By matching handwriting.
- [ ] By analyzing word length with previous books.
- [ ] By analyzing the number of pages in a book.
- [x] By analyzing the book's preface.

**2) How can a list L be transformed into a tuple?**
- [x] tuple(L)
- [ ] tup(L)
- [ ] L(tuple)
- [ ] L(tup)

**3) Will the following piece of code always return True?**
```python
G = nx.gnp_random_graph(10, 0.5)
print(nx.is_connected(G))
```
- [ ] True
- [x] False

**4) What is the output of the following code?**
```python
 1  import networkx as nx
 2  import matplotlib.pyplot as plt
 3
 4
 5  G = nx.Graph()
 6  G.add_nodes_from([1, 2, 3, 4])
 7  G.add_edges_from([(1, 2), (2, 1), (2, 3), (3,4), (4,1), (3,1)])
 8
 9  nx.draw(G,with_labels=True)
10  plt.show()
```
Options (images of drawn graphs, nodes labelled 1–4):
- [ ] A straight diagonal chain: 1 at the top left, then 2, 3 and 4 at the bottom right
- [ ] A crossing ("X") layout: 4 and 1 at the top, 2 and 3 at the bottom, with two lines crossing in the middle
- [ ] A quadrilateral 4 – 3 – 2 – 1 – 4 with an extra diagonal between 1 and 3
- [ ] A fourth drawing with 4 at the top left, 3 at the right and 2 at the bottom right (only partly visible in the video)

**5) How many edges are there in the following graph?**
(Image: nodes 4 and 1 at the top, 2 and 3 at the bottom; edges 4–1, 4–3, 1–2 and 2–3, so the lines cross in an X.)
- [ ] 4
- [ ] 5
- [ ] 3
- [ ] 2

**6) How many neighbors does node 3 have?**
(Image: nodes 2 and 1 at the top, 3 and 4 at the bottom; edges 2–1, 2–3, 1–3, 1–4 and 3–4.)
- [ ] 2
- [ ] 4
- [ ] 1
- [x] 3

**7) In which of the following ways can we create a string in python?**
- [ ] By using single quotes.
- [ ] By using double-quotes.
- [ ] By using triple-quotes.
- [x] All of the above.

**8) Which of the following is not true about Stylometry Analysis?**
- [ ] It is quantitative study of literature style
- [ ] It is based on the observation that the authors tend to write in relatively consistent and recognisable ways
- [ ] any two people may have same vocabulary
- [ ] It is a tool to study variety of questions involving style of writing

**9) A complete graph will have __ degree of separation**
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] Depends on the number of nodes.

**10) Networkx in pythons is used for**
- [ ] Making networks
- [ ] Analyzing networks
- [ ] Visualizing networks
- [ ] All of the above
