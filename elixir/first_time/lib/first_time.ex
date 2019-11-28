defmodule GameRules do
  @moduledoc """
  Documentation for GameRules.
  """

  def dies?(:alive, alive_neighbours) when alive_neighbours < 2 do
    true
  end

  def dies?(:dead, 0) do
    true
  end



  # def dies?(:alive, 0) do
  #   true
  # end
end
