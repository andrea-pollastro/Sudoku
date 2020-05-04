# Sudoku Solver and Sudoku Generator
Author: Andrea Pollastro

In the last two years I got passionate about the Sudoku puzzle, so I decided to write a Sudoku Solver and a Sudoku Generator that creates Sudoku with a unique solution (with the difficulties easy, medium, hard).<br>
Since solving a Sudoku is known to be a NP-complete problem, I realized an algorithm based on <i>backpropagation</i> speeded by the <i>constraint propagation</i> technique and the <i>Search</i> strategy proposed by <a href="https://norvig.com/sudoku.html">Peter Norvig</a>.<br>
The generator I've implemented creates a solved Sudoku and then it adds <i>n</i> blank cells to make it "playable" (where <i>n</i> is related to the desired difficulty) while preserving the uniqueness of the grid's solution.

# Solving benchmarks
I've firstly tested the solver on 100 grids created by the generator for each difficulty (<a href="https://github.com/andrea-pollastro/Sudoku/blob/master/sudokueasy.txt">easy</a>, <a href="https://github.com/andrea-pollastro/Sudoku/blob/master/sudokumedium.txt">medium</a> and <a href="https://github.com/andrea-pollastro/Sudoku/blob/master/sudokuhard.txt">hard</a>) obtaining these results (in seconds):
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

Then I tested the <a href="http://norvig.com/top95.txt">95 hard puzzles</a> and the <a href="http://norvig.com/hardest.txt">eleven puzzles</a> tested by Peter Norvig obtaining these results (in seconds):
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
