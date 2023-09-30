First my usual finding prime factor code was slow .
Then I found out that Prime factors of a number will be less than root of the number.
Similarly primes below a number will be less than half of the number.
Using this idea and iterating only odd numbers finding out if n is divisible by f .
Divide if yes else f+=2, finally after the loop n will be the largest prime factor.
