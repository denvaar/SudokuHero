### Application Description ###

Sudoku Hero solves sudoku puzzles of all
sizes and difficulty. The puzzles may be
loaded and saved via text files (.txt).

While Sudoku Hero is a sudoku solving
application, it has been built as a way
to explore a couple software design patterns
as well as PyQt.

![Sudoku Hero](https://github.com/denvaar/SudokuHero/blob/master/screenShot.png)

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

### Project Structure ###

#### Files ####

    ./README.txt        Application information
    ./mainFile.py       Application entry point (python mainFile.py to run)
    ./screenShot.png    Sample screen shot

#### Directories ####

    ./diagrams/      UML Diagrams
    ./algorithms/    Algorithms for loading, saving, and solving puzzles.
    ./widgets/       Custom GUI widgets
    ./unittests/     Unit tests of core functionalities

### Author ###

Denver Smith
11/15/15


