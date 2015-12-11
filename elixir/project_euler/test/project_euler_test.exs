defmodule ProjectEulerTest do
  use ExUnit.Case
  doctest ProjectEuler

  alias ProjectEuler, as: PE

  # Helper Tests

  # Exercise Tests
  test "problem one example" do
    assert PE.problem_one(10) == 23
  end

  # @tag :pending
  test "problem one question" do
    assert PE.problem_one(1000) == 233168
  end

  # @tag :pending
  test "problem one negative number" do
    assert PE.problem_one(-1) == :error
  end

  # @tag :pending
  test "problem two small number" do
    assert PE.problem_two(100) == 44
  end

  # @tag :pending
  test "problem two question" do
    assert PE.problem_two(4000000) == 4613732
  end

  # @tag :pending
  test "problem two negative number" do
    assert PE.problem_two(-1) == :error
  end

end
