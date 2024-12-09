def count_primes(n):
    if n < 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False   
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n, i):
                is_prime[j] = False
    
    return sum(is_prime)

# Unit testing part
import unittest

class TestPrimeCounter(unittest.TestCase):
    def test_count_primes(self):
        self.assertEqual(count_primes(10), 4)
        self.assertEqual(count_primes(18), 7)
        self.assertEqual(count_primes(100), 25)
        self.assertEqual(count_primes(0), 0)
        self.assertEqual(count_primes(1), 0)

if __name__ == "__main__":
    unittest.main()