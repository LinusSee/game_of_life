defmodule GameRulesTest do
  use ExUnit.Case
  doctest GameRules

  describe "Underpopulation: cell with < 2 neighbours dies or remains dead" do
    test "alive cell with 0 neighbours dies" do
      assert GameRules.dies?(:alive, 0) == true
    end

    test "alive cell with 1 neighbour dies" do
      assert GameRules.dies?(:alive, 1) == true
    end

    test "dead cell with 0 neighbours remains dead" do
      assert GameRules.dies?(:dead, 0)
    end

    test "dead cell with 1 neighbour remains dead" do
      assert GameRules.dies?(:dead, 1)
    end
  end

  describe "Survival: alive cell with 2 or 3 neighbours stays alive" do
    test "alive cell with 2 neighbours stays alive" do
      refute GameRules.dies?(:alive, 2)
    end

    test "alive cell with 3 neighbours stays alive" do
      refute GameRules.dies?(:alive, 3)
    end
  end

  describe "Revival: dead cell with exactely 3 neighbours comes alive" do
    test "dead cell with exactely 3 neighbours comes alive" do
      refute GameRules.dies?(:dead, 3)
    end
  end

  describe "Overpopulation: a cell with > 3 neighbours will be dead" do
    test "alive cell with 4 neighbours dies" do
      assert GameRules.dies?(:alive, 4)
    end

    test "alive cell with 6 neighbours dies" do
      assert GameRules.dies?(:alive, 6)
    end

    test "alive cell with 8 neighbours dies" do
      assert GameRules.dies?(:alive, 8)
    end
  end
end
