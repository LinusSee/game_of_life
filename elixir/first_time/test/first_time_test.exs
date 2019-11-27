defmodule FirstTimeTest do
  use ExUnit.Case
  doctest FirstTime

  test "greets the world" do
    assert FirstTime.hello() == :world
  end
end
