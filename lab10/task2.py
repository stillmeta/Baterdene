def stack_operation_cost(n, k):
    
    if n == 1:
        return 1.0
    
    total_pairs = n // k
    total_non_pairs = n % k
    
    total_cost = (total_pairs * 2) + total_non_pairs
    
    return total_cost / n


import unittest

class TestAmortizedCost(unittest.TestCase):
    
    def test_amortized_cost_example_1(self):
        n = 10
        k = 3
        expected = 0.7
        result = stack_operation_cost(n, k)
        self.assertEqual(result, expected)
    
    def test_amortized_cost_example_2(self):
        n = 5
        k = 2
        expected = 1.0
        result = stack_operation_cost(n, k)
        self.assertEqual(result, expected)
    
    def test_amortized_cost_example_3(self):
        n = 7
        k = 4
        expected = 0.7142857142857143
        result = stack_operation_cost(n, k)
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_amortized_cost_edge_case(self):
        n = 1
        k = 1
        expected = 1.0
        result = stack_operation_cost(n, k)
        self.assertEqual(result, expected)

    def test_amortized_cost_large_values(self):
        n = 100000
        k = 2
        expected = 1.0
        result = stack_operation_cost(n, k)
        self.assertEqual(result, expected)

# Run the tests
if __name__ == '__main__':
    unittest.main()