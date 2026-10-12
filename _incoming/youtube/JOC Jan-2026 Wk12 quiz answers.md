# JOC Jan-2026 · Week 12: Assignment 12

- Source: <https://www.youtube.com/watch?v=bCpk0Ur-EoA> · NPTEL ASSIGNMENTS · published 2026-04-03
- Portal: due 2026-04-15, 23:59 IST; "Your last recorded submission was on 2026-04-04, 06:56 IST" → **Jan-2026 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown). Fast-scrolling phone recording; this assignment page contains no code block.

**Understanding PageRank Through Code-Based Simulation**

In the lectures, we discussed a Python program that simulates a simplified version of the PageRank algorithm using **point distribution**. The program creates a directed graph, assigns points to nodes, redistributes those points according to outgoing edges, and compares the results with NetworkX's built-in PageRank function.

**1. Graph Creation**

A directed graph (DiGraph) with 10 nodes (numbered 0 to 9) is created using NetworkX.

**2. Random Edge Generation**

The function responsible for adding edges loops over all pairs of distinct nodes (s, t) and adds a directed edge from s to t with a **50% probability**. Self-loops are avoided by checking that s != t.

**3. Initial Point Assignment**

Every node starts with **100 points**. These points are stored in a list where the index corresponds to the node number.

**4. Point Distribution Logic**

During redistribution:
- If a node has **no outgoing edges**, it keeps all its points.
- If a node has outgoing edges, its points are **split equally** among them.

**5. Iterative Redistribution**

The program repeatedly redistributes points over multiple rounds. After each round, the new distribution is printed. The user can stop the process by typing #.

**6. Graph Visualization**

The graph structure, including nodes and edges, is displayed using matplotlib.

**7. Ranking Nodes by Points**

At the end, a ranking function stores final points in a dictionary {node: points} and sorts them in ascending order to find which nodes have the lowest and highest scores.

**8. Comparison with PageRank**

The program also calls NetworkX's built-in pagerank() function to compute the official PageRank values for the same graph and prints them for comparison with the manual simulation.

This simulation helps visualize how **importance flows through a network** and how PageRank emerges as a stable distribution of scores when point redistribution is repeated many times.

**1) Why is a directed graph mandatory for implementing PageRank in the given code?**
- [x] Because PageRank depends on the direction of influence between nodes
- [ ] Because undirected graphs cannot be read from files
- [ ] Because NetworkX only supports directed graphs
- [ ] Because visualization requires arrows

**2) Why are all nodes initially assigned equal points before distribution begins?**
- [ ] To speed up execution
- [x] To remove any initial bias in importance
- [ ] To match NetworkX's internal implementation
- [ ] To simplify graph drawing

**3) If a node has many outgoing edges, how does it affect its contribution?**
- [ ] It gains more points
- [ ] It distributes more total points
- [x] Its influence is divided among its neighbors
- [ ] It stops participating after one iteration

**4) Why does the case study include a manual Excel-style simulation?**
- [ ] To replace Python computation
- [ ] To compute final PageRank values
- [ ] To reduce graph complexity
- [x] To help visualize a single iteration clearly

**5) Why is the PageRank process iterative?**
- [ ] Because sorting requires multiple passes
- [x] Because convergence happens gradually
- [ ] Because graph size keeps changing
- [ ] Because visualization depends on iteration count

**6) What is the main purpose of converting the points list into a dictionary?**
- [ ] To improve numerical accuracy
- [ ] To reduce memory usage
- [ ] To speed up sorting
- [x] To preserve node–score association

**7) Which type of node can create issues in PageRank distribution?**
- [ ] Nodes with self-loops
- [ ] Nodes with no incoming edges
- [x] Nodes with no outgoing edges
- [ ] Nodes with high degree

**8) Why is sorting performed after computing final point values?**
- [ ] To normalize the graph
- [x] To rank nodes by importance
- [ ] To check convergence
- [ ] To reduce floating-point error

**9) What happens if the user stops the iteration process too early?**
- [ ] Results remain accurate
- [ ] Values become random
- [ ] Convergence still occurs
- [x] Rankings may be misleading

**10) Why is nx.pagerank() used at the end of the case study?**
- [ ] To replace the manual approach
- [ ] To speed up execution
- [ ] To visualize the graph
- [x] To validate the conceptual simulation

**11) What property of PageRank guarantees reliable results?**
- [ ] Use of sorting
- [ ] Deterministic initialization
- [x] Mathematical convergence
- [ ] Absence of cycles

**12) Which factor most strongly increases a node's PageRank score?**
- [ ] Number of outgoing edges
- [ ] Random initialization
- [x] Links from already important nodes
- [ ] Graph visualization

**13) Why is a random graph generated in the later part of the code?**
- [ ] To replace real datasets
- [x] To test scalability and behavior
- [ ] To guarantee convergence
- [ ] To reduce computation time

**14) Why does PageRank still work even if initial points are changed?**
- [ ] Because initial values are ignored
- [ ] Because points are normalized instantly
- [ ] Because sorting removes bias
- [x] Because the algorithm converges to the same distribution

**15) Which statement best summarizes the PageRank idea demonstrated in the case study?**
- [ ] Popular nodes are those with many outgoing edges
- [ ] Importance is random but stabilizes
- [ ] Every node eventually gets equal rank
- [x] A node is important if important nodes point to it
