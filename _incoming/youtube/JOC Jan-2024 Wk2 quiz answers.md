# JOC Jan-2024 · Week 2: Assignment

- Source: <https://www.youtube.com/watch?v=-7U-XDjb7ek> · Techies Talk · published 2024-01-27
- Portal: `noc24_cs57`, due 2024-02-07, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked by the video author before submitting → unverified (only "Thank you for taking the Week 2 : Assignment." is shown, no score)

**1) At any given point during a program's execution, what value is held within a variable?**
- [ ] The value it was initially assigned when it was created.
- [ ] The sum of all values that have ever been assigned to it.
- [x] The most recent value that was assigned to it.
- [ ] The average of all values that have ever been assigned to it.

**2) What will be the output of the following Python code snippet?**

```python
a = 'The value is: '
b = input('Enter a value: ')
c = a + b
print(c)
```
**Which of the following represents the correct output if the user inputs "25"?**
- [x] The value is: 25
- [ ] 25
- [ ] The value is:
- [ ] None of the above

**3) What are the possible loop values that can be specified in the range argument of a for loop in Python, and why are these values used?**
- [x] Integers, representing the starting and ending points of the loop, allowing iteration through a specified range of numbers.
- [ ] Floating-point numbers, enabling iteration through decimal ranges with precise steps.
- [ ] Strings, facilitating iteration through characters in a specified string
- [ ] Tuples, allowing iteration through multiple sequences simultaneously.

**4) What values can be used in the argument of a while loop in Python, and why are these values used?**
- [ ] Integers, representing the starting and ending points of the loop, allowing iteration through a specified range of numbers
- [x] Boolean expressions or conditions, enabling the loop to execute until the condition becomes False.
- [ ] Floating-point numbers, allowing iteration through decimal ranges with precise steps.
- [ ] Strings, facilitating iteration through characters in a specified string.

**5) What types of conditional entries can be used in a Python if statement, and why are these entries used?**
- [ ] Integers, representing specific numeric values to check against a variable, ensuring a match for equality
- [x] Boolean expressions or conditions, evaluating to True or False and determining the path of execution in the code.
- [ ] Strings, enabling comparison of text values for exact matches in the condition
- [ ] Floating-point numbers, allow range-based conditions to check if a variable falls within a specific numerical range.

**6) Consider the following code snippet:**

```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)
```
**What does the code do?**
- [x] Takes an input **n**, computes the multiplication table of **n** from **1** to **10**, and prints each multiplication.
- [ ] Takes an input **n**, computes the multiplication table of **n** from **1** to **11**, and prints the final product.
- [ ] Takes an input **n**, computes the multiplication table of **n** from **1** to **10**, and prints the final product.
- [ ] Takes an input **n**, initializes **i** to **1**, and prints the multiplication of **n** and **i** without any loop.

**7) Consider the following code snippet:**

```python
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, 'x', i, '=', number * i)
        i += 1
```
(as displayed on the portal, `i += 1` is indented deeper than `print`)

**What does the code do?**
- [x] Takes an input number, computes the multiplication table of numbers from 1 to 10, and prints each multiplication
- [ ] Takes an input number, computes the multiplication table of numbers from 1 to 11, and prints the final product.
- [ ] Takes an input number, computes the multiplication table of numbers from 1 to 10, and prints the final product.
- [ ] Takes an input number, initializes **i** to 1, and prints the multiplication of number and **i** without any loop.

**8) Consider the following code snippet:**

```python
num = int(input("Enter a number: "))
result = 1
counter = 1

while counter <= num:
    result *= counter
    counter += 1

print("Factorial of", num, "is:", result)
```
**What does the code do?**
- [x] Takes an input **num,** computes the factorial of **num**, and prints the factorial value.
- [x] Takes an input **num,** computes the product of numbers from **1** to **num**, and prints the final product.
- [ ] Takes an input **num,** computes the sum of numbers from **1** to **num**, and prints the final sum.
- [ ] Takes an input **num,** initializes the result to **1**, and prints the value of the result without any factorial computation.

**9) An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. Which of the following are IDEs?**
- [x] PyCharm
- [x] Spyder
- [x] Visual Studio Code (VS Code)
- [ ] C# (pronounced "C sharp")

**10) A Python distribution is a software bundle, which contains a Python interpreter and the Python standard library. What is Anaconda being discussed in lectures?**
- [ ] A species of snake
- [ ] A type of programming language
- [ ] An integrated development environment (IDE)
- [x] A Python distribution for scientific computing and data science
