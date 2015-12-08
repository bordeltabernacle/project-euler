defmodule ProjectEuler do
  alias ProjectEulerHelper, as: PEH

  @moduledoc """
  Solving the problems on Project Euler.
  """

  @doc """
  Multiples of 3 and 5
  Problem 1
  If we list all the natural numbers below 10 that are multiples
  of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

  Find the sum of all the multiples of 3 or 5 below 1000.
  """
  @spec problem_one(integer()) :: integer()
  def problem_one(n) do
    (for i <- 1..n-1, rem(i, 3) == 0 or rem(i, 5) == 0, do: i)
    |> Enum.sum
  end

end
