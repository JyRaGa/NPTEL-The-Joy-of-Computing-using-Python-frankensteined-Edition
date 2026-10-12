# JOC Jan-2026 · Week 9: Assignment 9

- Source: <https://www.youtube.com/watch?v=Srks81bt7bw> · NPTEL ASSIGNMENTS · published 2026-03-13
- Portal: due 2026-03-25, 23:59 IST; "Your last recorded submission was on 2026-03-13, 19:07 IST" → **Jan-2026 session**
- `[x]` = option shown selected in the author's (already submitted) page → unverified (no score shown). The video is a fast-scrolling phone screen recording; long code lines are cut off at the right edge of the phone screen (marked `…`).

**Stylometric and Sentiment Analysis of the Federalist Papers**

**Background**

A political science research team is examining the **Federalist Papers**, a historically significant collection of essays written to support the ratification of the U.S. Constitution. While many essays are clearly attributed to **Hamilton, Madison,** or **Jay,** a subset of essays has **disputed or shared authorship.**

Instead of relying on historical arguments alone, the team decides to use **computational text analysis** to study writing patterns across different author groups.

**Problem Statement**

The team wants to understand whether **quantitative textual characteristics** , such as word usage patterns and sentiment , can help differentiate between authors and provide insights into disputed essays.

The task is **not to assign authorship directly**, but to compare:
- Writing style indicators
- Distributional properties of words
- Emotional tone across author groups

**Dataset Description**

The dataset is organized by author category:
- **Hamilton**
- **Madison**
- **Jay**
- **Disputed**
- **Shared**

Each category contains a block of text representing essays attributed to that group. These texts are treated as independent corpora.

**Analytical Approach**

The analysis follows four major stages:

**1. Text Preprocessing**

Each author's text is processed to extract meaningful words by:
- Tokenizing text into individual words
- Removing punctuation and non-alphabetic tokens
- Eliminating common English stopwords

This ensures that comparisons focus on **content-bearing words** rather than grammatical fillers.

**2. Stylometric Analysis Using Word Length**

For every author group:
- The length of each word is computed
- A frequency distribution of word lengths is constructed

Word length is treated as a **stylistic signature**, allowing comparison of writing habits without relying on vocabulary meaning.

**3. Sentiment Analysis**

Each author's entire text is analyzed using a sentiment model to compute:
- A **polarity score** ranging from negative to positive

This helps identify whether different authors (or disputed texts) consistently express different emotional tones, even within formal political writing.

**4. Visual Comparison**

Word-length frequency distributions are plotted for all authors on the same figure.
This visual representation allows analysts to:
- Observe overlaps between authors
- Identify stylistic similarities
- Spot anomalies in disputed or shared texts

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from textblob import TextBlob


authors = ["Hamilton", "Madison", "Disputed", "Jay", "Shared"]

federalist_by_author = {
    "Hamilton": "Text data for Hamilton...",
    "Madison": "Text data for Madison...",
    "Disputed": "Text data for Disputed...",
    "Jay": "Text data for Jay...",
    "Shared": "Text data for Shared..."
}


author_tokens = {}
for author, text_data in federalist_by_author.items():
    tokens = [
        word for word in word_tokenize(text_data)
        if word.isalpha() and word.lower() not in stopwords.words("english")
    ]
    author_tokens[author] = tokens


author_word_lengths = {}
for author, tokens in author_tokens.items():
    word_lengths = [len(word) for word in tokens]
    author_word_lengths[author] = word_lengths


sentiment_scores = {}
for author, text_data in federalist_by_author.items():
    blob = TextBlob(text_data)
    sentiment_scores[author] = blob.sentiment.polarity


plt.figure(figsize=(12, 6))
for author in authors:
    fdist = FreqDist(author_word_lengths[author])
    fdist.plot(15, cumulative=False)
plt.legend(authors)
plt.show()


for author, sentiment in sentiment_scores.items():
    print(f"Sentiment analysis for {author}: Sentiment Score = {sentiment}")
```

**1) Assume the text for *Hamilton* contains only the words:**
**"Liberty liberty the Constitution"**

**After preprocessing, what will be stored in author_tokens["Hamilton"]?**
- [x] ["Liberty", "liberty", "Constitution"]
- [ ] ["Liberty", "liberty", "the", "Constitution"]
- [ ] ["liberty", "liberty", "constitution"]
- [ ] ["Liberty", "Constitution"]

**2) If an author's text contains only stopwords, what happens when plotting their word-length distribution?**
- [ ] The program raises a runtime error
- [x] An empty plot is generated without bars
- [ ] All word lengths are plotted as zero
- [ ] The author is skipped automatically

**3) Which author property is directly visualized in the plotted graphs?**
- [ ] Sentiment polarity
- [ ] Token frequency
- [x] Word-length frequency
- [ ] Vocabulary richness

**4) If the *Disputed* corpus contains significantly longer average words than others, how would this most likely appear in the plot?**
- [ ] Higher bars at smaller word lengths
- [x] A wider spread with peaks at larger word lengths
- [ ] A flat distribution across all lengths
- [ ] No visible difference from other authors

**5) Suppose TextBlob returns a sentiment polarity of 0.0 for *Jay*. What does this imply?**
- [x] Jay's text is emotionally neutral overall
- [ ] Jay uses no adjectives
- [ ] Jay's text contains no positive words
- [ ] Jay's text failed sentiment analysis

**6) If the stopword filter were removed from preprocessing, which change would MOST likely occur?**
- [ ] Sentiment scores become negative
- [x] Word-length distributions shift toward shorter lengths
- [ ] Vocabulary size decreases
- [ ] Alphabetic filtering stops working

**7) Why is sentiment analysis performed on the entire text rather than token-level sentiment?**
- [ ] TextBlob does not support token sentiment
- [x] Corpus-level sentiment smooths local noise
- [ ] Token sentiment would always be zero
- [ ] Tokens are removed before sentiment analysis

**8) If the *Shared* corpus was written by multiple authors, what pattern would MOST likely appear?**
- [ ] A sharply peaked word-length distribution
- [ ] Identical sentiment to all authors
- [x] A broader, less consistent distribution
- [ ] No visible plot

---

**Exploring Social Networks Using Shortest Paths**

**Background**

A data analyst is interested in understanding how people are connected within a large online social network. To do this, the analyst works with a real-world dataset representing friendships between users on a social media platform. Each user is modeled as a **node**, and each friendship is modeled as an **edge** in a graph.

The analyst chooses **NetworkX**, a Python library designed for creating, analyzing, and studying complex networks, to perform this analysis.

**Problem Context**

One of the most well-known ideas in social network analysis is the **Six Degrees of Separation** theory, which suggests that any two people in the world are connected by [a] surprisingly small number of intermediate connections. *(first letter of the line cut off)*

The analyst wants to verify whether this idea holds for the given social network dataset by answering the following questions:
- How closely connected are users on average?
- What is the shortest possible connection between any two users?
- What is the longest shortest path observed in the network?
- Does the network show properties that support the idea of six degrees of separation?

**Data Description**
- The dataset is stored in a text file (facebook_combined.txt).
- Each line represents a friendship between two users.
- The graph is **undirected**, meaning friendships work both ways.

**Analytical Approach**

Using the provided code, the analyst performs the following steps:

**1. Network Construction**
   - o The dataset is read and converted into a graph structure.
   - o All users (nodes) are extracted for analysis.

**2. Shortest Path Computation**
   - o For every pair of distinct users, the shortest path length is calculated.
   - o These values represent the minimum number of connections required to move from one user to another.

**3. Statistical Analysis of Paths**
   - o All shortest path lengths are stored.
   - o The minimum, maximum, and average shortest path lengths are computed.

**4. Interpretation of Results**
   - o The **minimum shortest path** shows the closest possible connection between any two users.
   - o The **maximum shortest path** indicates the farthest distance between two users while still remaining connected.
   - o The **average shortest path length** serves as the most important metric for validating the Six Degrees of Separation theory.

**Key Observations**
- If the **average shortest path length** is close to 6 (or lower), it supports the idea that people in the network are closely connected.
- A relatively small **maximum shortest path length** suggests that even the most distant users are not too far apart.
- These findings highlight how social networks enable rapid connectivity through indirect relationships.

**Conceptual Insights**
- **Six Degrees of Separation:** The experiment demonstrates how short paths emerge naturally in large social networks.
- **Exponential Growth of Connections:** As each user has multiple friends, and each friend has their own friends, the number of reachable users grows exponentially with each step.
- **Graph Theory in Practice:** Abstract concepts like nodes, edges, and shortest paths directly translate into real-world social phenomena.

```python
import networkx as nx

G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes)

shortest_path_length_list = []
for u in N:
    for v in N:
        if u != v:
            l = nx.shortest_path_length(G, source=u, target=v)
            print(f"Shortest path between {u} and {v} is of length {l}")
            shortest_path_length_list.append(l)

minimum_shortest_path_length = min(shortest_path_length_list)
maximum_shortest_path_length = max(shortest_path_length_list)
average_shortest_path_length = sum(shortest_path_length_list) / len(shortest_path_length_list)

print("Minimum Shortest Path Length:", minimum_shortest_path_length)
print("Maximum Shortest Path Length:", maximum_shortest_path_length)
print("Average Shortest Path Length:", average_shortest_path_length)
print("Six Degrees of Separation: The idea that you can connect with anyone in the world through a network of acquaintances within an average of six connect…")
print("Exponential Growth in Connections: This concept works because of the exponential growth in the number of friends' friends within a social network.")
print("Encouragement to Explore NetworkX: You can explore the NetworkX library further and make use of its various functionalities for graph analysis.")
```
*Code for Reference* (code is tiny in the recording; the first `print` string runs off the right edge)

**9) What is the primary purpose of using nx.read_edgelist("facebook_combined.txt") in the case study?**
- [x] To create a graph where users are nodes and friendships are edges
- [ ] To calculate shortest paths directly from the file
- [ ] To store shortest path lengths in a list
- [ ] To visualize the social network

**10) Why does the code check if u != v before computing the shortest path?**
- [ ] To prevent duplicate edges in the graph
- [x] To avoid self-loops that always have zero path length
- [ ] To reduce memory usage
- [ ] To ensure the graph remains undirected

**11) What does the list shortest_path_length_list primarily represent?**
- [ ] The degree of each node
- [ ] The number of friends per user
- [x] All shortest path lengths between distinct pairs of nodes
- [ ] Only the longest path in the network

**12) Which metric from the code is most relevant for validating the Six Degrees of Separation concept?**
- [ ] Minimum shortest path length
- [ ] Maximum shortest path length
- [ ] Number of nodes in the graph
- [x] Average shortest path length

**13) If the network is fully connected, what would most likely happen to the maximum shortest path length?**
- [ ] It would increase significantly
- [ ] It would become zero
- [x] It would remain relatively small
- [ ] It would become equal to the number of nodes

**14) Why does the case study mention exponential growth in connections?**
- [ ] Because shortest path lengths grow exponentially
- [ ] Because the number of nodes doubles each iteration
- [x] Because friend-of-friend connections expand rapidly with each step
- [ ] Because NetworkX uses exponential algorithms internally

**15) What is a computational limitation of the approach used in the code?**
- [ ] It cannot handle undirected graphs
- [ ] It only works for weighted graphs
- [ ] It ignores isolated nodes
- [x] It computes shortest paths for every node pair, which is expensive
