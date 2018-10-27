# Sudoku solver and Sudoku generator
Author: Andrea Pollastro

In the last two years I got passionate about Sudoku game, so I decided to write a Sudoku solver and a Sudoku generator that creates sudoku with unique solution (with the difficulty easy, medium, hard).

# Sudoku solver
Solving a Sudoku is known to be a NP-complete problem, for this reason to solve a Sudoku I realized a <i>backpropagation algorithm</i> (needed to find all the possible configuration of the grid) speeded by the <i>constraint propagation</i> technique.
To solve a Sudoku, my algorithm uses mainly two data structures:
- <i>peers</i>: a dictionary that contains the indexes of all the cells contained into the row, col and box per cell
- <i>validValues</i>: a dictionary that contains all the possible values assignable per cell

I really got ispired by <i>Search</i> strategy proposed by Norvig, for this reason my search starts from the cell with the fewer number of choices, decreasing in this way the failure's probability. Then, the algorithm starts assigning one of these values to the chosen cell and the search goes on. If no one of these values leads to a solution (in the other hand, if all of these values leads to contradictions), the algorithm uses backtracking to come to the last valid state of the grid.<br>
The assignment comes giving one value to a cell and applying the main rule of the Sudoku game that is every value must appear once in any column, rows and box.<br>
Thanks to this constraint, propagation is made: once a value is assigned to a cell, it is removed from the choices of all the cell's peers. If one of them remains without choices, we've reached a contradiction, so we come back to the last valid state of the grid. Otherwise, if one of them instead remains with only one choice, that value is assigned to that peer.<br>
In this way, only one assignment can lead us quickly to a contradiction or to a solution.

# Sudoku generator
The basic idea to generate a Sudoku consists to randomly assign values to cell from the available values. To avoid the validity checking for every value before assigning to a cell (specifically, checking if it's not present into the cell's column/row/box), I used three data structures (contained into the <i>supportStructures</i>):
- <i>rows</i>: list of <i>r</i> sets
- <i>cols</i>: list of <i>c</i> sets
- <i>box</i>: list of <i>b</i> sets

Where <i>r, c, b</i> are the number of rows, cols and boxes of the grid.<br>
The idea consists in insert the value assigned to a cell into the row/col/box respective to the cell (this comes in constant time because lists permit positional access in constant time and insert into sets comes in constant time too because python's sets use hashing).<br>
In this way, the number of available elements per cell is equal to the number of missing element into the union of the respective row/col/box. If this number is equal to zero, we've reached a contradiction, so we come back to the last valid state of the grid (restoring the three sets row/col/box).<br>
Once we got the complete grid, we need to make blank some cell to make the grid "playable". The number of cells varies according to the difficulty. It is really important to preserve the uniqueness of the grid's solution and, for this reason, for any new blank the number of solution is counted. If the number of solution is greater then 1, the last blank is restored and another one is choosen. This process is iterated until the number of blanks is equal to the ones requested by the difficulty.

# Solving benchmarks
Firstly, I started to test my solver using Sudoku produced by my generator. In particular, I solved 100 grids at difficulties <a href="https://github.com/andrea-pollastro/Sudoku/blob/master/sudokueasy.txt">easy</a>, <a href="https://github.com/andrea-pollastro/Sudoku/blob/master/sudokumedium.txt">medium</a> and <a href="https://github.com/andrea-pollastro/Sudoku/blob/master/sudokuhard.txt">hard</a>.<br>
I obtained these results (expressed in seconds):
<table>
  <tr>
    <td><b>Difficulty</b></td>
    <td><b>Max value</b></td>
    <td><b>Min value</b></td>
    <td><b>Mean</b></td>
    <td><b>Std. dev.</b></td>
  </tr>
  <tr>
    <td>Easy</td>
    <td>0.00094</td>
    <td>0.00004</td>
    <td>0.00007</td>
    <td>0.00011</td>
  </tr>
  <tr>
    <td>Medium</td>
    <td>0.00279</td>
    <td>0.00004</td>
    <td>0.00051</td>
    <td>0.00056</td>
  </tr>
  <tr>
    <td>Hard</td>
    <td>0.07276</td>
    <td>0.00004</td>
    <td>0.00711</td>
    <td>0.01190</td>
  </tr>
</table>
I also tested these <a href="http://norvig.com/top95.txt">95 hard puzzles</a> and these <a href="http://norvig.com/hardest.txt">eleven puzzles</a> tested by Norvig and I obtained these results:
<table>
  <tr>
    <td><b>Name test</b></td>
    <td><b>Max value</b></td>
    <td><b>Min value</b></td>
    <td><b>Mean</b></td>
    <td><b>Std. dev.</b></td>
  </tr>
  <tr>
    <td>95 hard puzzles</td>
    <td>2.92104</td>
    <td>0.00082</td>
    <td>0.22289</td>
    <td>0.48517</td>
  </tr>
  <tr>
    <td>Eleven puzzles</td>
    <td>0.05647</td>
    <td>0.00050</td>
    <td>0.00914</td>
    <td>0.01579</td>
  </tr>
</table>
All the test were made on an Intel Core i3-2350M CPU @ 2.30 GHz
