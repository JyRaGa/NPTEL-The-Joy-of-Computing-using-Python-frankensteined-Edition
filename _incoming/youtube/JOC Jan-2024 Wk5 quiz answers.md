# JOC Jan-2024 · Week 5: Assignment 5

- Source: <https://www.youtube.com/watch?v=FXFVUqhDpgg> · Study_Ease · published 2024-02-18
- Portal: `noc24_cs57`, due 2024-02-28, 23:59 IST → **Jan-2024 session**
- `[x]` = option ticked by the video author before submitting → unverified (video ends at "Submit Answers", no score)

**1) Imagine the Monty Hall problem had four doors instead of three, and Monty opened one door to reveal a goat after your initial choice, what would be the probability of winning the car by switching?**
- [ ] 1/2
- [ ] 1/3
- [ ] 1/4
- [x] 3/4

**2) What happens if you try to add a new key-value pair to a dictionary using a key that already exists in the dictionary?**
- [x] The new value overwrites the existing value
- [ ] An error is raised
- [ ] The dictionary becomes immutable
- [ ] The new value is appended to the existing value

**3) The extended version of "Rock, Paper, Scissors" with "Lizard" and "Spock" was popularized by the TV show "The Big Bang Theory." Here are the rules for "Rock, Paper, Scissors, Lizard, Spock":**

**- Rock wins against Scissors.**
**- Scissors wins against Paper.**
**- Paper wins against Rock.**
**- Rock wins against Lizard.**
**- Lizard wins against Spock.**
**- Spock wins against Scissors.**
**- Scissors wins against Lizard**
**- Lizard wins against Paper**
**- Paper wins against Spock.**
**- Spock wins against Rock.**

**Each option can defeat two other options, lose to two other options, and draw with one other option.**

**Now, the major steps involved in the algorithm for coding a rock-paper-scissors game as discussed in the lecture include:**
**1) Assigning values to the choices: The algorithm involves assigning numerical values to the rock, paper, and scissors choices, such as 1 for rock, 2 for paper, and 3 for scissors.**
**2) Inputting user choices: The algorithm prompts the users to input their choices for the game, such as rock, paper, or scissors.**
**3) Secret bit positions: The algorithm uses secret bit positions to determine the winner of the game, which involves bitwise operations to compare the choices and determine the outcome.**
**4) Coding the rules: The algorithm includes coding the rules for determining the winner based on the choices made by the players, such as using if-else conditions to compare the choices and declare the winner.**
**5) Running the program: The algorithm allows for running the program to test the rock- paper-scissors game with different user inputs and provides examples of the game outcomes.**

**What would be the possible change in steps for running "Rock, Paper, Scissors, Lizard, Spock"?**
- [ ] Step 1 would involve assigning 5 values to choices instead of 3
- [ ] The bitwise operations involved in Step 3 would involve modulo operation with 5 instead of 3
- [ ] None of the above
- [x] All the above

**4) How does Bubble Sort compare elements in an array?**
- [x] Compares adjacent elements and swaps if they are in the wrong order
- [ ] Compares random elements in the array
- [ ] Compares all elements with the first element
- [ ] Compares elements in reverse order

**5) To sort a list in ascending order when does Bubble Sort exhibit poor performance?**
- [ ] When the list is sorted in ascending order
- [x] When the list is sorted in descending order
- [ ] When the list contains unique elements
- [ ] Bubble Sort always exhibits poor performance

**6) How many passes does Bubble Sort make through the array in the worst-case scenario for sorting n elements?**
- [ ] n
- [x] n-1
- [ ] 2n
- [ ] n²

**7) How many pairs of adjacent elements are compared in a single pass of the bubble sort algorithm?**
- [ ] n
- [x] n-1
- [ ] n/2
- [ ] 2n

**8) The following steps are required to implement the binary search for an array sorted in ascending order.1)**

**1)Initialize Pointers:**
**- Set two pointers, \`low\` and \`high\`, initially pointing to the start and end of the array, respectively.**

**2) Calculate Midpoint:**
**- Calculate the midpoint index using the formula \`mid = (low + high) // 2\`.**

**3) Compare Midpoint Element:**
**- Compare the element at the midpoint with the target element you are searching for:**
**- If the midpoint element is equal to the target, the search is successful, and you can return the index.**
**- If the midpoint element is less than the target, update \`low\` to \`mid + 1\` and continue the search in the right half.**
**- If the midpoint element is greater than the target, update \`high\` to \`mid - 1\` and continue the search in the left half.**

**4) Repeat:**
**- Repeat steps 3-4 until the \`low\` pointer is greater than the \`high\` pointer. This means the search range has become empty.**

**5) Return Result:**
**- If the target element is found, return its index. If the target is not found, return a sentinel value (e.g.,-1) to indicate that the element is not in the array.**

**Which steps would require modification if the array were sorted in descending order?**
- [ ] Step 2
- [x] Step 4
- [ ] Steps 2 and 4
- [ ] No modification in steps

**9) Select the correct statements among the following**
- [ ] In the presence of duplicate elements in a list, binary search always finds the first occurrence of the element in the list
- [x] In the presence of duplicate elements in a list, binary search may or may not find the first occurrence of the element in the list
- [x] In the presence of duplicate elements in a list, the existing binary search algorithm with minor modifications can be used to find the first occurrence of the target element in the list
- [ ] In the presence of duplicate elements in a list , the existing binary search can be used to find any kth(k can be any number from 1 to number of times the element has been repeated) of target element in the list

**10) Swapping of two numbers is an intermediate step in any sorting algorithm, In the lecture we use a temporary variable to swap two elements in the list.**
**Can swapping of two numbers be done without using a temporary variable?**
- [x] Yes
- [ ] No
- [ ] Depends on size of list
- [ ] Depends on nature of elements in the list
