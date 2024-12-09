import unittest

def fibonacci_tabulation(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_table = [0] * (n + 1) 
    fib_table[0], fib_table[1] = 0, 1 
    for i in range(2, n + 1): 
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2] 

    return fib_table[n]

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        # Test cases for the Fibonacci function
        self.assertEqual(fibonacci_tabulation(0), 0)
        self.assertEqual(fibonacci_tabulation(1), 1)
        self.assertEqual(fibonacci_tabulation(2), 1)
        self.assertEqual(fibonacci_tabulation(3), 2)
        self.assertEqual(fibonacci_tabulation(4), 3)
        self.assertEqual(fibonacci_tabulation(5), 5)
        self.assertEqual(fibonacci_tabulation(6), 8)
        self.assertEqual(fibonacci_tabulation(7), 13)
        self.assertEqual(fibonacci_tabulation(8), 21)
        self.assertEqual(fibonacci_tabulation(9), 34)
        self.assertEqual(fibonacci_tabulation(10), 55)

if __name__ == '__main__':
    unittest.main()
