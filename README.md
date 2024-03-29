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
  - Case1: A dead cell with 2 neighbours remains dead
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
  - Case5: The board extends upwards if a cell is brought to life on its top (infinitely large board)
  - Case6: The board extends to the left if a cell is brought to life on its left (infinitely large board)
  - Case7: The board extends to the right if a cell is brought to life on its right (infinitely large board)
  - Case8: The board extends downwards if a cell is brought to life on its bot (infinitely large board)
  - Case9: The board extends top and right if a cell is brought to life on both sides
  - Case10: The board extends bot and right if a cell is brought to life on both sides
  - Case11: The board extends bot and top if a cell is brought to life on both sides
  - Case 12: The board extends left and right if a cell is brought to life on both sides
  - Case 13: The board extends left and top if a cell is brought to life on both sides
  - Case 14: The board extends left and bot if a cell is brought to life on both sides
  - Case 15: The board extends left, right and top if a cell is brought to life on those sides
  - Case 16: The board extends left, right and bot if a cell is brought to life on those sides
  - Case 17: The board extends left, bot and top if a cell is brought to life on those sides
  - Case 18: The board extends right, bot and top if a cell is brought to life on those sides
  - Case 19: The board extends on all sides if a cell is brought to life on all sides

- GameOfLife:
  - Case1: The game returns the correct board, i.e. the state, after creation
  - Case2: The game returns the correct board after running an iteration
  - Case3: The game returns the correct board after running 10 iterations
  - Case4: The game returns the correct board after running 100 iterations
  - Case5: The game returns the correct board after running 1000 iterations
