defmodule GameRules do
  @moduledoc """
  Documentation for GameRules.
  """

  def dies?(:alive, 0), do: true
  def dies?(:alive, 1), do: true



  # def dies?(:alive, 0) do
  #   true
  # end
end
