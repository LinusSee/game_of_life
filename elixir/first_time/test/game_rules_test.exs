defmodule GameRulesTest do
  use ExUnit.Case
  doctest GameRules

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
