defmodule ProjectEulerTest do
  use ExUnit.Case
  doctest ProjectEuler

  alias ProjectEuler, as: PE

  test "problem one example" do
    assert PE.problem_one(10) == 23
  end

  # @tag :pending
  test "problem one question" do
    assert PE.problem_one(1000) == 233168
  end

end
