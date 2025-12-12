"""Tests for hello module."""

import unittest
from sample_pipa_package.hello import greet


class TestHello(unittest.TestCase):
    """Test cases for hello module."""

    def test_greet(self):
        """Test greet function."""
        result = greet("Test")
        self.assertEqual(result, "Hello, Test testtttt!")


if __name__ == "__main__":
    unittest.main()