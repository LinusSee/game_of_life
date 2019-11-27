defmodule GameRulesTest do
  use ExUnit.Case
  doctest GameRules

  test "alive cell with 0 neighbours dies" do
    assert GameRules.dies?(:alive, 0) == true
  end
end
