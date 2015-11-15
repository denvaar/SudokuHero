### Application Description ###

Sudoku Hero solves sudoku puzzles of all
sizes and difficulty. The puzzles may be
loaded and saved via text files (.txt).

While Sudoku Hero is a sudoku solving
application, it has been built as a way
to explore a couple software design patterns
as well as PyQt.

### Requirments ###

- Python 3.4
- PyQt5
- NumPy

### Design Decisions ###

- GUI code has been separated from the data
models and underlying algorithms.

- A template method pattern is used to encapsulate
the sudoku solving algorithm. Two variations of the
solving algorithm are implemented in separate classes.
Both classes use the same set of steps to solve a puzzle.
The sequnce of steps for the solving algorithm is defined
and implemented in the base class.

- A factory pattern is used to select an appropriate
algorithm for loading a puzzle file based on whether the
text file contains DOS or UNIX style line endings.

- A simple strategy pattern is also used to allow
the user to switch between two different ways to save
a map.

### File Descriptions ###



### Author ###

Denver Smith
11/15/15


