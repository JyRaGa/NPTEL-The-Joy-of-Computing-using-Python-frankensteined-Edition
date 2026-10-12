# JOC Jan-2024 · Week 3: Assignment 3

- Source: <https://www.youtube.com/watch?v=MSdYi4Kh63k> · Techies Talk · published 2024-02-05
- Portal: `noc24_cs57`, due 2024-02-14, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked by the video author before submitting → unverified (only "Thank you for taking the Week 3 : Assignment 3." is shown, no score)

**1) Consider the following code snippet:**

```python
elements = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    item = input("Enter element " + str(i + 1) + ": ")
    elements.append(item)
print("The entered elements are:", elements)
```
**What does the code do?**
- [ ] Takes a list of numbers as input, appends each number to a list, and prints the list of numbers
- [ ] Takes a list of elements as input, appends each element to a list, and prints the list of elements
- [x] Takes the count of elements followed by the same number of elements as input, appends each element to a list, and prints the list of elements
- [ ] Takes the count of elements, appends each element to a list, and prints the count of elements entered.

**2) Data Structure is a way by which you can organize/arrange your data. Which of the following statements are true about List Data Structure: [MSQ]**
- [x] It is a flexible Data Structure
- [x] Elements could be added to a list.
- [x] Elements could be subtracted from a list.
- [x] **This_is_not_List = [ ]** is an empty list

**3) Consider the following code snippet:**

```python
L = ['Amar', 'Akbar', 'Anthony']
print(L[2], 'is brother of', L[1], 'and', L[0])
```
**What does the above code print?**
- [ ] Amar, Akbar, Anthony
- [ ] amar is brother of anthony and akbar
- [ ] Amar is brother of Anthony and Akbar
- [x] Anthony is brother of Akbar and Amar

**4) Consider the following code snippet:**

```python
numbers = [2, 4, 6, 8, 10]
for i in range(len(numbers)):
    numbers[i] *= 2
print("Updated list:", numbers)
```
**What does the code do?**
- [x] Takes a list of numbers, multiplies each number by 2, and prints the updated list
- [ ] Takes a list of numbers, appends each number to the list twice, and prints the updated list
- [ ] Takes a list of numbers, removes even numbers from the list, and prints the updated list
- [ ] Takes a list of numbers, divides each number by 2, and prints the updated list

**5) What will be the output of the following Python code?**

```python
import random
def genetic_evolution(binary_string):
    mutation_probability = 0.1  # Adjust this probability as needed
    evolved_string = ""
    for bit in binary_string:
        if random.random() < mutation_probability:
            evolved_string += "1" if bit == "0" else "0"
        else:
            evolved_string += bit
    return evolved_string
initial_string = "0000000000"
result = genetic_evolution(initial_string)
print(result)
```
- [ ] "1111111111"
- [ ] "0000000000"
- [x] A string with some 1s and some 0s
- [ ] The function will raise an error

**6) Consider the following code snippet:**

```python
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)
result = sum(numbers)
average = result / n
print("Sum of the numbers:", result)
print("Average of the numbers:", average)
```
**What does the code do?**
- [x] Takes a list of numbers as input, computes the sum of the numbers, and prints the sum along with the average
- [ ] Takes the count of elements, computes the sum of the elements, and prints the sum along with the average
- [ ] Takes a list of numbers as input, computes the average of the numbers, and prints the average along with the sum
- [ ] None of the above

**7) What will be the output of the following Python code?**

```python
import random
def permutation_example(word):
    word_list = list(word)
    random.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    return shuffled_word
input_word = "python"
result = permutation_example(input_word)
print(result)
```
- [ ] "Python"
- [x] A random permutation of the letters in "python"
- [ ] "random"
- [ ] The function will raise an error

**8) Consider the following code snippet:**

```python
numbers = [1, 2, 3, 4, 5]
new_numbers = []
for num in numbers:
    new_numbers.insert(0, num)  #insert() is a function that inserts a value at a given index
print("Updated list:", new_numbers)
```
**What does the code do? [MSQ]**
- [ ] Reverses the numbers list and stores it in new_numbers.
- [x] Creates an empty list named new_numbers and appends elements from numbers to it in reverse order.
- [ ] Produces an error due to an invalid function used for list manipulation.
- [ ] Generates a new list new_numbers with elements from numbers in the same order as numbers.

**9) Which of the following are the examples of Social Computing/Crowd Computing: [MSQ]**
- [x] Wikipedia
- [x] Stack Exchange
- [x] Quora
- [x] Facebook

**10) Consider the following code snippet:**

```python
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
**What does the code do?**
- [ ] Prints numbers from 1 to 20, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".
- [x] Prints numbers from 1 to 20, replacing multiples of 3 and 5 with "FizzBuzz", multiples of 3 with "Fizz", and multiples of 5 with "Buzz".
- [ ] Prints numbers from 1 to 20, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and numbers divisible by both 3 and 5 with their product.
- [ ] Prints numbers from 1 to 20, replacing multiples of 3 with "Buzz", multiples of 5 with "Fizz", and numbers divisible by both 3 and 5 with "FizzBuzz".
