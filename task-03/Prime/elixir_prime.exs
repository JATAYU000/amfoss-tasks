defmodule PrimeNumbers do
  def is_prime(n) when n <= 1, do: false
  def is_prime(n) do
    Enum.all?(2..n - 1, fn x -> rem(n, x) != 0 end)
  end

  def find_primes_up_to_n(n) do
    Enum.filter(2..n, &is_prime/1)
  end

  def run do
    IO.puts("Enter a number : ")
    n = String.to_integer(IO.gets("")|> String.replace("\n", ""))
    primes = find_primes_up_to_n(n)
    IO.puts("Prime numbers:")
    Enum.each(primes, &IO.puts/1)
  end
end

PrimeNumbers.run()
