defmodule ProjectEuler.One do

  @moduledoc """
  Solving problem #1 on
  [Project Euler](https://projecteuler.net/).
  """

  @doc """
  Problem 1: Multiples of 3 and 5

  If we list all the natural numbers below 10 that are multiples
  of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

  Find the sum of all the multiples of 3 or 5 below 1000.

  ## Examples

      iex> ProjectEuler.One.sum_mul_three_five(10)
      23

      iex> ProjectEuler.One.sum_mul_three_five(1000)
      233168

      iex> ProjectEuler.One.sum_mul_three_five(-1)
      :error

  """
  @spec sum_mul_three_five(integer()) :: integer()
  def sum_mul_three_five(n) when n <= 0, do: :error
  def sum_mul_three_five(n) when n > 0 do
    (for i <- 1..n-1, rem(i, 3) == 0 or rem(i, 5) == 0, do: i)
    |> Enum.sum
  end
end
