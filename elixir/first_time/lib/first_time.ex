defmodule GameRules do
  @moduledoc """
  Documentation for GameRules.
  """
  def dies?(_, alive_neighbours) when alive_neighbours < 2 do
    true
  end

  def dies?(_, _), do: false



  # def dies?(:alive, 0) do
  #   true
  # end
end
