import System.IO

isPrime :: Integer -> Bool
isPrime n
    | n <= 1    = False
    | otherwise = not $ any (\x -> n `mod` x == 0) [2..n - 1]

findPrimesUpToN :: Integer -> [Integer]
findPrimesUpToN n = filter isPrime [2..n]

main :: IO ()
main = do
    putStr "Enter a number: "
    hFlush stdout
    input <- getLine
    let n = read input :: Integer
    let primes = findPrimesUpToN n
    putStrLn $ "Prime numbers:"
    mapM_ print primes