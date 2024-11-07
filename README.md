# conway_python

### Conway's Game of Life Implementation in Python


Inspired by the following project at realpython.com: [https://realpython.com/conway-game-of-life-python](https://realpython.com/conway-game-of-life-python)


### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/smcgarril/conway_python.git
  $ cd conway_python
  ```

2. Initialize and activate a virtual environment:
  ```
  $ python -m venv venv
  $ source venv/bin/activate
  ```

3. Build project:
  ```
  $ python -m pip install .
  ```

4. Run the program:
  ```
  $ conway_python -p "Glider Gun" -g 100
  ```

NOTE: To execute with a version of Python lower than 3.11 you may need to install an external dependency:
  ```
  $ pip install tomli
  ```


### Options

The program accepts the following options which can be passed as command line arguments:

  ```
  -h, --help                Displays information on possible choices

  --version                 Prints current version and exits

  -p, --pattern             Choose a starting pattern from the list in patterns.toml (default: Blinker)

  -a, --all                 Loop through all patterns in patterns.toml

  -v, --view                Choose a view type from views.py (default: CursesView)

  -g, --gen                 Set number of generations to evolve (default: 10)

  -f, --fps                 Set frames per second (default: 7)
  ```