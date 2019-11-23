# game_of_life

This is a spare time project I wanted to do after joining the global day of code retreat 2019.
<br>
The goal is to write a sample solution of Conway's Game of Life the way I would write it right now. I will do it using test driven developement starting with a Python version and maybe adding solutions in other languages later on.
<br>
With this I want to improve my testing skills, Python unittest knowledge and develop a small project using TDD since I have never done a project with this method.
<br>
Also I try to implement this problem as object oriented as possible, which might not be the most efficient way, but definitely a fun exercise.


## Test list
- Underpopulation: An cell with < 2 neighbours will be dead
  - Case1: An alive cell with 0 neighbours dies
  - Case2: An alive cell with 1 neighbour dies
  - Case3: A dead cell with 0 neighbours remains dead
  - Case4: A dead cell with 1 neighbour remains dead
- Survival: An alive cell with 2 or 3 neighbours stays alive
  - Case1: An alive cell with 2 neighbours stays alive
  - Case2: An alive cell with 3 neighbours stays alive
- Revival: A dead cell with exactely 3 neighbours will become alive
  - Case1: A dead cell with exactely 3 neighbours will become alive
- Overpopulation: An cell with > 3 alive neighbours will be dead
  - Case1: An alive cell with 4 neighbours dies
  - Case2: An alive cell with 6 neighbours dies
  - Case3: An alive cell with 8 neighbours dies
  - Case4: A dead cell with 4 neighbours remains dead
  - Case5: A dead cell with 8 neighbours remains dead
  
- Board: 
  - Case1: The board correctly counts the alive neighbours around the upper left cell
  - Case2: The board correctly counts the alive neighbours around the bottom right cell
  - Case3: The board correctly counts the alive neighbours around a cell that is not at an edge
  - Case4: The board correctly applies all rules to transition between states (Create several test cases)
  - Case5: The board extends if a cell outside of it's bounds is brought to life (infinitely large board)
