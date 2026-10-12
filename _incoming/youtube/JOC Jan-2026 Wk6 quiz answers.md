# JOC Jan-2026 · Week 6: Assignment 6

- Source: <https://www.youtube.com/watch?v=Z1IjmCFp2Ww> · NPTEL Solver · published 2026-02-21
- Portal: due 2026-03-04 (time hidden by an overlay) → **Jan-2026 session**
- `[x]` = option ticked by the video author before submitting → unverified (no score shown). **Q2 and Q6 were left unticked** in every frame.

**In-Place Data Reversal in a Memory-Constrained System**

**Context**

A learning analytics platform maintains a list of numerical records representing **student interaction order** during an online examination.The records are stored in the sequence in which events occurred.

For audit, debugging, and review purposes, the system occasionally needs to **reverse the order of these records** so that the **most recent interactions appear first**.

However, the platform operates under **strict memory constraints** because it runs simultaneously for thousands of students.

**System Constraints**

The development team has imposed the following conditions:

1. The reversal must happen **within the same list** (no new list allowed).

2. The solution must be **function-based**, not written inline.

3. The team wants to explore **non-iterative approaches** as part of internal training.

4. The system should work correctly for:

   o Empty lists

   o Lists with odd number of elements

   o Lists with even number of elements

**Operational Requirement**

When a list such as:

[10, 20, 30, 40, 50]

is processed by the system, the **same list object** must be transformed into:

[50, 40, 30, 20, 10]

No additional list should be returned or constructed.

**Implementation Provided to the Team**

The following implementation was submitted by a developer for review and analysis:

```python
def reverseArray(nums):
    start = 0
    end = len(nums) - 1
    swap = 0
    return helper_reverse(start, end, nums, swap)

def helper_reverse(start, end, nums, swap):
    if start > end:
        return nums

    swap = nums[start]
    nums[start] = nums[end]
    nums[end] = swap

    return helper_reverse(start + 1, end - 1, nums, swap)
```

**1) If the function reverseArray is called with the input:**

nums = [1, 2, 3, 4]

**What will be the final value of nums?**
- [ ] [1, 2, 3, 4]
- [x] [4, 3, 2, 1]
- [ ] [2, 1, 4, 3]
- [ ] [4, 2, 3, 1]

**2) For which condition does the recursive process stop?**
- [ ] When start == end
- [ ] When start > end
- [ ] When end == 0
- [ ] When swap becomes zero

**3) What does the function reverseArray(nums) return?**
- [x] The modified list nums
- [ ] None
- [ ] A new reversed list
- [ ] Only the last swapped value

**4) What happens when the input list has an odd number of elements?**
- [ ] The middle element is removed
- [ ] The program crashes
- [x] The middle element remains unchanged
- [ ] The middle element is swapped with itself twice

**5) What is the output when reverseArray([]) is executed?**
- [ ] Runtime error
- [ ] None
- [ ] [0]
- [x] []

**6) What is the extra space complexity of this approach (excluding input list)?**
- [ ] O(n) due to recursion stack
- [ ] O(1) because no variables are used
- [ ] O(log n)
- [ ] O(n²)

**7) What is the actual role of the variable swap?**
- [ ] It stores recursion depth
- [x] It temporarily holds a value during exchange
- [ ] It controls termination
- [ ] It accumulates reversed values

**8) For a list of length 6, how many recursive calls perform swaps?**
- [ ] 6
- [ ] 4
- [x] 3
- [ ] 5

**9) Which statement best describes the behavior of this function?**
- [ ] It creates and returns a new list
- [ ] It modifies the list but returns nothing
- [ ] It uses iteration internally
- [x] It mutates the original list and returns it

**10) If the final return helper_reverse(...) line is removed from helper_reverse, what happens?**
- [x] The list still gets reversed but None is returned
- [ ] The list is not reversed
- [ ] The program throws a syntax error
- [ ] Only the first swap happens

---

**Terminal-Based Tic Tac Toe Game**

**Background**

During a programming lab session, two students decide to recreate the classic **Tic Tac Toe** game using Python. Instead of using a graphical interface or mobile application, they choose a **terminal-based approach**, relying entirely on text input and output.

The objective is to allow two players to play the game interactively while the system manages the board, validates moves, and determines the final result.

**Game Environment**

The game is executed in a Python environment where:
- The board consists of **nine positions arranged in three rows** [and three columns] *(end of line hidden by the SUBSCRIBE overlay)*
- Each position on the board can display:
  - o An "X"
  - o An "O"
  - o Or remain empty
- The board is shown to players after every move

Players interact with the system by entering their choices through the keyboard.

**Player Interaction**
- The game involves **two players**
- One player uses the symbol **X**, the other uses **O**
- Players enter their moves using **row and column numbers**
- Input is provided in a fixed format during every turn
- If an invalid entry is made, the system requests a new input without progressing the game

**Game Flow**
- The game begins with a predefined starting player
- Players alternate turns throughout the match
- Each turn updates the visible board
- The game continues until a decisive outcome is reached
- No player is allowed to overwrite an existing move

**Game Completion**

The game ends in one of two ways:

1. **A winner is declared**
   - o One player successfully completes a valid winning pattern
   - o The game stops immediately once a winner is identified

2. **A draw is declared**
   - o All board positions are filled
   - o No player achieves a winning pattern

In both cases, the final board state is displayed before the result is announced.

The source code is presented in **three sequential parts** and must be read **in the order provided** as a single continuous program.

```python
board = [[" " for _ in range(3)] for _ in range(3)]

def display_board():
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("---------")

def check_won(symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True

    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False
```
*Tic Tac Toe Game Code – Part 1*

```python
current_player = "X"
turns = 0

while turns < 9:
    display_board()
    move = input(f"Player {current_player}, enter your move (row and column): ").split(',')

    if len(move) != 2:
        print("Invalid input.")
        continue

    row, col = map(int, move)

    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid position.")
        continue

    if board[row - 1][col - 1] != " ":
        print("Cell already occupied.")
        continue

    board[row - 1][col - 1] = current_player
    turns += 1
```
*Tic Tac Toe Game – Part 2*

```python
    if check_won(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break

    current_player = "X" if current_player == "O" else "O"
else:
    display_board()
    print("It's a draw!")
```
*Tic Tac Toe Game – Part 3*

**11) When the program starts executing and no input has been entered yet, which of the following is true?**
- [ ] The board is displayed with all cells filled with "X"
- [x] The board is displayed with all cells empty
- [ ] The game immediately asks Player O for input
- [ ] The game prints "It's a draw!"

**12) A player enters the following input when prompted:**
```
2
```
**What happens next?**
- [ ] The move is accepted and placed in column 2
- [ ] The program crashes with an error
- [x] The program asks the player to re-enter input
- [ ] The turn switches to the next player

**13) Which situation causes the variable turns to increase by 1?**
- [ ] When the board is displayed
- [ ] When a player enters invalid input
- [ ] When a player overwrites an occupied cell
- [x] When a valid move is successfully placed on the board

**14) The game stops immediately when which of the following occurs?**
- [ ] Nine turns have been completed
- [x] A winning condition is detected
- [ ] An invalid move is entered
- [ ] The board is fully displayed

**15) Under which condition does the program print "It's a draw!"?**
- [ ] When Player O makes the last move
- [ ] When no diagonal matches are found
- [x] When the loop ends without detecting a winner
- [ ] When all rows contain mixed symbols
