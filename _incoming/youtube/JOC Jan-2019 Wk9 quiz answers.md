# JOC Jan-2019 · Week 9: Cool Ideas(Part 7) · Assignment 9

- Source: <https://www.youtube.com/watch?v=0znreo31xlc> · Ultimate Gamer · published 2019-03-30
- Portal: "Due date for this assignment: 2019-04-03, 23:59 IST."; "Your last recorded submission was on 2019-03-30, 15:09 IST" → **Jan-2019 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown). Video ends with "…can not guarantee that these solutions are 100% correct." Alternate video for this week (not transcribed): Study Fun `DLlcJY6CYns`.

**1) What should be the output of the following program?**
```
import network as nx
G=nx.Graph()
for i in range(3):
        G.add_node(i)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
nx.draw()
```
- [ ] A triangle graph
- [ ] A graph with 3 edges and an isolated node
- [ ] A graph with 3 edges and no isolated node
- [x] Error

> Note: as written (`import network`, and `nx.draw()` without G) it raises an Error. If the intended code is `networkx` with `nx.draw(G)`, the graph has nodes 0–3, a 1-2-3 triangle and node 0 isolated → "A graph with 3 edges and an isolated node".

**2) In network, in order to draw Erdos Renyi graph there is a function 'gnp_random_graph(n,p)'. What are n and p here?**
- [ ] n is the number of edges and p is the probability of edge creation.
- [x] n is the number of nodes and p is the probability of edge creation.
- [ ] n is the number of edges and p is the probability of node creation.
- [ ] n is the number of nodes and p is the probability of node creation.

**3) What does the function G.nodes() in networkx return?**
- [ ] It returns the number of nodes present in the graph G.
- [x] It returns the list of nodes present in the graph G.
- [ ] It returns the tuple of nodes present in the graph G.
- [ ] It returns the number of edges present in the graph G.

**4) What does the function scipy.misc.read() return?**
- [ ] Image in the form of pixels
- [ ] A matrix of RGB values
- [x] Image as Numpy array
- [ ] All of the above.

**5) What is Stylometry?**
- [ ] Stylometry is qualitative study of literary style.
- [x] Stylometry is quantitative study of literary style.
- [ ] Both
- [ ] None of the above

**6) Which of the following statements is correct about tokenisation in Python?**
- [ ] Tokenisation involves splitting words from the text.
- [ ] Tokenisation involves splitting sentences from the text.
- [x] Both
- [ ] None of the above

**7) What is Project Gutenberg?**
- [ ] It is a repository comprising of free images.
- [ ] It is a repository comprising of free music.
- [x] It is a repository comprising of free ebooks.
- [ ] None of the above

**8) Which of the following is a Graph visualisation software?**
- [x] Gephi
- [ ] Visual Graph
- [ ] Graph Plot
- [ ] None of the above

**9) Is the Graph constructed by the following networkx program connected?**
```
import networkx
G = networkx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(7)
G.add_node(9)
G.add_edge(1,2)
G.add_edge(3,1)
G.add_edge(2,4)
G.add_edge(4,1)
G.add_edge(9,1)
G.add_edge(1,7)
G.add_edge(2,9)
networkx.draw(G)
```
- [x] Yes
- [ ] No
