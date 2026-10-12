# JOC Jul-2023 · Week 7: Assignment 7

- Source: <https://www.youtube.com/watch?v=Rv3wui8FeuY> · S Kumar Edu · published 2023-09-03 (518 s screen recording)
- Portal: `noc23_cs108`, "Due date: 2023-09-13, 23:59 IST." → **Jul-2023 session**. Each question is 1 point.
- `[x]` = option the author selected while scrolling; only partly visible for some questions, so unticked ≠ wrong. No score is shown.
- Q4 and Q6 options are images; they are described in text.

**1) Values of CSV files are separated by?**
- [ ] Commas
- [ ] Colons
- [ ] Semi-colons
- [ ] Slash

**2) What is the output of the following code?**
```python
def spiral(row, column, arr) :
    rowStart = 0; columnStart = 0

    while (rowStart < row and columnStart < column) :

        for i in range(rowStart, row) :
            print(arr[i][columnStart], end = " ")

        columnStart = columnStart + 1

        for i in range (columnStart, column) :
            print( arr[row - 1][i], end = " ")

        row = row - 1

        if (rowStart < row) :
            for i in range(row - 1, rowStart - 1, -1) :
                print(arr[i][column - 1], end = " ")
            column = column - 1

        if (columnStart < column) :
            for i in range(column - 1, columnStart - 1, -1) :
                print( arr[rowStart][i], end = " ")

            rowStart = rowStart + 1

matrix = [ [ 1, 2, 3 ],
           [ 5, 6, 7 ],
           [ 9, 10, 11 ] ]

row = 3
column= 3

spiral(row, column, matrix)
```
- [ ] 1, 2, 3, 7, 11, 10, 9, 5, 6
- [ ] 1, 2, 3, 5, 6, 7, 9, 10, 11
- [x] 1, 5, 9, 10, 11, 7, 3, 2, 6
- [ ] 1, 5, 9, 2, 6, 10, 3, 7, 11

**3) What will be the output of the following code?**
```python
import turtle

pen = turtle.Turtle()

for i in range(3):

    pen.forward(60)
    pen.right(120)

turtle.done()
```
- [ ] Scalar triangle
- [ ] Right angle triangle
- [ ] Equilateral triangle
- [ ] Isosceles triangle

**4) Which of the following program will draw a hexagon?**

Option A
```python
 1  import turtle
 2
 3  pen = turtle.Turtle()
 4
 5  for i in range(3):
 6
 7      pen.right(60)
 8      pen.forward(60)
 9
10  turtle.done()
```
- [ ] (Option A)

Option B
```python
 1  import turtle
 2
 3  pen = turtle.Turtle()
 4
 5  for i in range(3):
 6
 7      pen.right(60)
 8      pen.forward(60)
 9      pen.right(60)
10      pen.forward(60)
11
12  turtle.done()
```
- [x] (Option B)

Option C
```python
 1  import turtle
 2
 3  pen = turtle.Turtle()
 4
 5  for i in range(6):
 6
 7      pen.right(30)
 8      pen.forward(30)
 9
10  turtle.done()
```
- [ ] (Option C)

(Only three code blocks are shown for this question in the recording.)

**5) Which of the following library is used to render data on google maps?**
- [ ] gplot
- [ ] googlemaps
- [x] gmplot
- [ ] gmeplot

**6) What is the output of the following code?**
```python
 1  import turtle
 2
 3  pen = turtle.Turtle()
 4
 5  for i in range(3):
 6
 7      pen.right(60)
 8      pen.forward(60)
 9      pen.penup()
10      pen.right(60)
11      pen.forward(60)
12      pen.pendown()
13
14
15  turtle.done()
```
Options (images):
- [ ] A hexagon drawn with an arrow on its top edge
- [ ] A 12-sided, nearly circular polygon with an arrow at the top
- [ ] An arrow at the top (pointing right) with two separate slanted lines below it, left and right
- [ ] An arrow at the top right, two slanted lines (left and right) and a horizontal line at the bottom

**7) Which turtle command is equivalent to lifting up a pen.**
- [ ] penlift()
- [x] penup()
- [ ] uppen()
- [ ] penremove()

**8) Why do we use functions?**
- [ ] To improve readability.
- [ ] To reuse code blocks.
- [ ] For the ease of code debugging.
- [x] All of the above

**9) Library used to import images?**
- [ ] PIL
- [ ] Imageview
- [ ] IMG
- [ ] image

**10) In snakes and ladder what can be the ways to track ladders and snakes?**
- [ ] Maintain a dictionary with snakes or ladder number blocks as keys.
- [ ] Using the if condition to check on every number.
- [ ] Both A and B.
- [ ] None of the above
