defmodule GameBoardTest do
  use ExUnit.Case
  doctest GameBoard

  describe "Simple cases without the board extending in size" do
    test "board correctly counts the alive neighbours around the upper left cell" do
      board = [
        [ true, true, false, false ],
        [ false, true, false, true ],
        [ true, true, true, true ],
        [ true, false, false, false ]
      ]
      x_pos = 0
      y_pos = 0

      actual = GameBoard.alive_neighbours(board, x_pos, y_pos)
      expected = 2

      assert actual == expected
    end
  end
end
