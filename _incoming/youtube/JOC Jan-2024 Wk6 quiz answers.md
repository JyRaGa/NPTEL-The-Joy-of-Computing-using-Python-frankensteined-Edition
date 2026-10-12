# JOC Jan-2024 · Week 6: Assignment 6

- Source: <https://www.youtube.com/watch?v=xtjt5fpgHLg> · Techies Talk · published 2024-02-27
- Portal: `noc24_cs57`, due 2024-03-06, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked by the video author before submitting → unverified (only "Thank you for taking the Week 6 : Assignment 6." is shown, no score)

**1) What is the output of following code:**

```python
def mystry(n):
    if n < 2:
        return n
    else:
        return mystry(n-1) + mystry(n-2)

n = 25
print(mystry(n))
```
- [ ] 14930352
- [x] 75025
- [ ] 610
- [ ] None of the above

**2) Which method in Python is used to convert lowercase letters in a string to uppercase?**
- [x] `upper()`
- [ ] `capitalize()`
- [ ] `casefold()`
- [ ] `swapcase()`

**3) The "Min Max" strategy, often referred to as the minimax algorithm, is a decision-making algorithm used in game theory and artificial intelligence. It's commonly employed in two-player games with alternate turns and perfect information, such as chess or tic-tac-toe. What is the primary objective of the min max algorithm?**
- [ ] Maximizing the player's score
- [ ] Minimizing the opponent's score
- [x] Minimizing the maximum possible loss
- [ ] Maximizing the number of moves

**4) Typecasting refers to the conversion of one data type to another. Python provides several built-in functions for typecasting, such as `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, and `dict()` among others, to convert between different data types. What would be the output of the following code?**

```python
num_str = "123babumoshai"
num = int(num_str)
print(num)
```
- [ ] 123
- [x] ValueError
- [ ] SyntaxError
- [ ] NameError

**5) What term is used in programming languages when a function calls itself?**
- [ ] Self-referencing
- [ ] Iteration
- [x] Recursion
- [ ] Circular referencing

**6) Consider the following snippet of code.**

```python
def func(L):
    if L == []:
        return 0
    if L[0] % 2 == 0:
        return 1 + func(L[1:])
    else:
        return func(L[1:])
```
**If L is a non-empty list of positive integers, which of the following statements is correct about the recursive function func(L)?**
- [ ] It returns the total number of odd elements in the list L
- [x] It returns the total number of even elements in the list L
- [ ] It returns the sum of the even elements in the list L
- [ ] It returns the sum of the odd elements in the list L

**7) Consider the following snippet of code.**

```python
def func(L):
    if L == []:
        return 0
    if L[-1] % 2 == 1:
        return L[-1] + func(L[:-1])
    else:
        return func(L[:-1])
```
**If L is a non-empty list of positive integers, which of the following statements is correct about the recursive function `func(L)`?**
- [ ] It returns the total number of odd elements in the list L
- [ ] It returns the total number of even elements in the list L
- [ ] It returns the sum of the even elements in the list L
- [x] It returns sum of the odd elements in the list L

**8) What purpose does a base case serve in recursive functions?**
- [ ] To make the function run faster
- [ ] To eliminate the need for additional functions
- [x] To prevent infinite recursion and ensure termination
- [ ] To enable the function to handle complex calculations

---

**Q. 9-10**

**Consider the following function f that accepts an integer as argument `n`.**

```python
def f(n):
    if n > 1:
        if (n ** 0.5) == int(n ** 0.5):
            return 1 + f(int(n ** 0.5))
        elif n % 2 != 0:
            return 1 + f(3 * n + 1)
        else:
            return 1 + f(int(n / 2))
    elif n < 1:
        return 1 + f(n ** 2)
    else:
        return 0
```

**9) What is the value returned by `f(10000)` ?**

Answer entered: `7`

**10) What is the value returned by `f(-8)` ?**

Answer entered: `5`
