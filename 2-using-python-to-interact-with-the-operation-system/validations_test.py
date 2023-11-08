#!/usr/bin/env python3

import unittest
from validations import validate_username


class TestValidations(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_username("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_username("inv", 5), False)

    def test_valid(self):
        self.assertEqual(validate_username("invalid_user", 3), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_username, "user", -1)


unittest.main()
