def transform_potential(phi, D0):
    # Define new potential function Φ′
    def phi_prime(Di):
        return phi(Di) - phi(D0)
    return phi_prime

import unittest

class trasnformP(unittest.TestCase):
    def test_transform_potential(self):
            # Test case 1: Square function
            def square(x): return x**2
            transformed_square = transform_potential(square, 0)
            
            self.assertEqual(transformed_square(0), 0)  # Φ′(D0) should be 0
            self.assertEqual(transformed_square(2), 4)  # Φ′(2) should be 4
            self.assertEqual(transformed_square(3), 9)  # Φ′(3) should be 9
            
            # Test case 2: Different initial state
            transformed_square_d2 = transform_potential(square, 2)
            self.assertEqual(transformed_square_d2(0), -4)  # Φ′(0) = 0² - 2²
            self.assertEqual(transformed_square_d2(2), 0)   # Φ′(2) = 2² - 2²
            self.assertEqual(transformed_square_d2(3), 5)   # Φ′(3) = 3² - 2²
            
            # Test case 3: Exponential function
            def exp(x): return 2**x
            transformed_exp = transform_potential(exp, 1)
            
            self.assertEqual(transformed_exp(1), 0)    # Φ′(1) = 2¹ - 2¹
            self.assertEqual(transformed_exp(2), 2)    # Φ′(2) = 2² - 2¹
            self.assertEqual(transformed_exp(3), 6)    # Φ′(3) = 2³ - 2¹
            
            # Test case 4: Linear function
            def linear(x): return 3*x + 1
            transformed_linear = transform_potential(linear, 0)
            
            self.assertEqual(transformed_linear(0), 0)  # Φ′(0) = 1 - 1
            self.assertEqual(transformed_linear(1), 3)  # Φ′(1) = 4 - 1
            self.assertEqual(transformed_linear(2), 6)  # Φ′(2) = 7 - 1

if __name__ == '__main__':
    unittest.main()