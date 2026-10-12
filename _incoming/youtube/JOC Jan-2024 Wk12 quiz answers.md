# JOC Jan-2024 · Week 12: Assignment 12

- Source: <https://www.youtube.com/watch?v=olMpNzeQrus> · Study_Ease · published 2024-04-07
- Portal: `noc24_cs57`, due 2024-04-17, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked / value entered by the video author before submitting → unverified (video ends at "Submit Answers", no score)

**1) Which of the following is NOT a factor considered in Google's current search algorithms?**
- [ ] PageRank
- [ ] Content relevance
- [ ] User experience
- [x] None of the above

**2) In a weighted social network graph, what might the edge weights represent?**
- [ ] The time of interaction between users
- [ ] The strength of a relationship
- [ ] The number of shared interests
- [x] All of the above

**3) What is the purpose of a random walk in graph analysis?**
- [ ] To find the shortest path between two nodes
- [x] To explore the entire graph and discover its properties
- [ ] To prioritize nodes based on their degree
- [ ] To determine the central node in the graph

**4) Which of the following are real-world applications of directed graphs? (MSQ)**
- [ ] Social Media Friendship Graph
- [ ] Family Tree
- [x] Linking of Websites
- [x] Airline Route Representation
- [ ] Königsberg bridge problem

**5) Read the given code. Enter the number of elements in incoming_edges_D(NAT)**

```python
import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted directed graph
G = nx.DiGraph()

# Add edges with weights
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=1)
G.add_edge('D', 'E', weight=4)

                                    ← (a blank dark bar appears here in the portal's code image)

# Display incoming edges for node 'D'
incoming_edges_D = G.in_edges('D')
print("Incoming Edges to Node 'D':", incoming_edges_D)
```
Answer entered: `2`

**6) Which of the following statements about PageRank is true?**
- [ ] It only considers the number of links, not their weights
- [x] All web pages start with the same initial PageRank score
- [ ] PageRank is the only factor that determines search engine rankings
- [ ] None of the above

**7) In the Collatz sequence, if a starting value is a power of 2, how many iterations are needed to reach the cycle (4, 2, 1)?**
- [ ] One iteration
- [x] Number of Iterations would be logarithmic in the size of the starting value
- [ ] Number of Iterations would be linear in the size of the starting value
- [ ] None of the above

**8) For how many positive integers below 200 does the Collatz sequence not reach 1?**
- [x] 0
- [ ] 25
- [ ] 10
- [ ] 20

**9) Which of the following statements is true about the Collatz conjecture?**
- [ ] It has been proven to be true for all positive integers.
- [ ] It is known to be false for certain classes of numbers.
- [x] It remains an open problem, and its status is unknown.
- [ ] It only applies to prime numbers.

**10) Find the number of sequences required for Collatz Conjecture when applied to 5 to reach 1 (NAT)**

Answer entered: `6`
