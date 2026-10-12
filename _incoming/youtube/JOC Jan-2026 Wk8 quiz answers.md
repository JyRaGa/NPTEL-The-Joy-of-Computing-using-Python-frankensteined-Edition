# JOC Jan-2026 · Week 8: Assignment 8

- Source: <https://www.youtube.com/watch?v=dAxq9rWeU1U> · NPTEL Solver · published 2026-03-17
- Portal: due 2026-03-18 (time partly hidden by an overlay) → **Jan-2026 session**
- `[x]` = option ticked by the video author before submitting → unverified (no score shown)

**A Month of Chance—Simulating a Lottery Strategy**

**Background**

Ravi, a college student interested in probability and data analysis, wants to understand whether playing a simple lottery-style game every day can be profitable in the long run. Instead of relying on intuition or anecdotes, he decides to **simulate the experience using Python**.

Ravi chooses a very straightforward strategy:
- Every day, he selects **one fixed number between 1 and 10** as his bet.
- A system randomly draws a number between 1 and 10.
- If his chosen number matches the draw, he earns a large reward.
- If it doesn't, he incurs a small loss.

He repeats this experiment **once per day for 30 days**, representing a month of consistent participation.

---

**Objective of the Study**

The purpose of this case study is to:
- Observe how **randomness** affects outcomes over time
- Track **profit and loss trends** instead of isolated wins
- Visually analyze whether consistency in betting leads to gains or losses

Rather than focusing on a single lucky or unlucky day, Ravi wants to see the **overall trajectory** of his account balance.

---

**Experimental Setup**
- Ravi starts with an account balance of **₹0**
- He plays the game **once per day for 30 days**
- Each day's result updates his account balance
- The balance is recorded daily to study trends over time

To make the results more intuitive, Ravi plots:
- **Days (1–30)** on the x-axis
- **Account balance** on the y-axis

This allows him to clearly see fluctuations, streaks of loss, occasional jumps, and the final outcome.

---

**Given Code for Analysis**

Students are provided with the following Python code and are expected to analyze its behavior, output, and implications based on the case study above:

```python
import random
import matplotlib.pyplot as plt

# User input
bet = int(input("Enter your bet from 1 to 10: "))

# Account initialization
account = 0

# Simulation loop for one month (30 days)
x = []  # Days
y = []  # Account balances

for day in range(30):
    lucky_draw = random.randint(1, 10)

    if bet == lucky_draw:
        account += 900
    else:
        account -= 100

    x.append(day + 1)
    y.append(account)

# Visualization
plt.plot(x, y)
plt.xlabel("Days")
plt.ylabel("Account Balance")
plt.title("Lottery Simulation - Profit or Loss")
plt.show()
```

**1) What does the variable bet represent in the simulation?**
- [ ] The amount of money invested each day
- [ ] The randomly generated lucky number
- [x] The fixed number chosen by the user for the entire month
- [ ] The number of days the simulation runs

**2) How many times is the lottery game simulated in the program?**
- [ ] 10
- [x] 30
- [ ] Until the user wins
- [ ] Depends on the bet value

**3) What happens to the account balance when the bet does NOT match the lucky draw?**
- [ ] It remains unchanged
- [ ] It increases by 100
- [ ] It decreases by 900
- [x] It decreases by 100

**4) Which Python library is responsible for generating randomness in the simulation?**
- [ ] matplotlib
- [x] random
- [ ] pyplot
- [ ] math

**5) What do the lists x and y store respectively?**
- [ ] Account balances and days
- [ ] Bets and lucky numbers
- [x] Days and account balances
- [ ] Wins and losses

**6) If the user never wins even once during the 30 days, what will be the final account balance?**
- [x] −3000
- [ ] −900
- [ ] −100
- [ ] 0

**7) What is the probability of winning on any single day?**
- [ ] 1/30
- [ ] 1/100
- [x] 1/10
- [ ] Depends on previous days

**8) Why does the account balance graph typically show long downward trends with occasional sharp upward jumps?**
- [ ] Because the bet value changes daily
- [x] Because losses are frequent and wins are rare but large
- [ ] Because matplotlib smooths the curve
- [ ] Because account balance is averaged

**9) Which change would make the simulation more statistically reliable without changing the game rules?**
- [ ] Increasing the win amount
- [x] Running the simulation for more days
- [ ] Changing the bet every day
- [ ] Removing the plot

**10) Despite a high winning reward (₹900), why does the simulation still tend to show losses over time?**
- [ ] Because the plotting scale is incorrect
- [x] Because the probability of winning is too low compared to the loss frequency
- [ ] Because Python integers overflow
- [ ] Because the account starts at zero

> Note: with a 1/10 win chance, the expected daily result is 0.1·900 − 0.9·100 = 0, so the "tends to show losses" premise is not strictly true; the tick is reproduced as shown.

---

**Detecting Pattern Consistency Between Two Strings**

**Background**

A software team working on a **text pattern–matching system** needs to verify whether two given strings follow the **same structural pattern**. This requirement arises in areas such as:
- Data normalization
- Search indexing
- Language processing
- Pattern validation in user input

The focus is **not** on object-oriented design, but purely on **string processing and logical consistency**.

---

**Problem Scenario**

Two strings are given:
- String **S** represents an original pattern
- String **T** represents a transformed version

The task is to determine whether:
- Each character in **S** consistently maps to **one unique character** in **T**
- The mapping is **one-to-one and reversible**
- The relative structure of both strings remains identical

For example:
- "egg" and "add" follow the same pattern
- "foo" and "bar" do not

---

**Constraints of the Study**
- Both strings must be of **equal length**
- A character cannot map to **multiple different characters**
- Two different characters cannot map to the **same character**
- The comparison is performed **position by position**

Learners are given the following code to analyze and answer questions based on the case study:

```python
def isomorphicString(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if (char_s in s_map and s_map[char_s] != char_t) or \
           (char_t in t_map and t_map[char_t] != char_s):
            return False

        s_map[char_s] = char_t
        t_map[char_t] = char_s

    return True
```
*(the line-continuation character at the end of the `if` line is partly hidden by the text cursor in the recording)*

**11) What will the function return for s = "egg" and t = "add"?**
- [x] True
- [ ] False
- [ ] Depends on dictionary insertion order
- [ ] Raises an error

**12) What is the first condition that can cause the function to return False?**
- [ ] Duplicate characters in s
- [ ] Conflicting mappings in dictionaries
- [ ] Repeated characters at adjacent positions
- [x] Length mismatch between the two strings

**13) What will the function return for s = "ab" and t = "cc"?**
- [x] False
- [ ] True
- [ ] Only the forward mapping fails
- [ ] Depends on loop iteration

**14) Why is the condition checking both s_map and t_map necessary?**
- [ ] To reduce memory usage
- [ ] To avoid nested loops
- [ ] To speed up execution
- [x] To enforce a one-to-one and reversible character mapping

**15) Which of the following best describes what the algorithm is verifying?**
- [x] Structural equivalence between two strings
- [ ] Lexicographical ordering
- [ ] Equality of character frequencies
- [ ] Whether both strings are permutations
