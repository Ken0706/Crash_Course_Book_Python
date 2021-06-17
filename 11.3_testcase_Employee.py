import unittest
from Employee import Employee


class TestcaseEmploy(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('Ken', 'Nguyen', 55000)

    def test_money_default(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.annual, 60000)

    def test_money_custom(self):
        self.emp.give_raise(1000)
        self.assertEqual(self.emp.annual, 56000)


if __name__ == '__main__':
    unittest.main()
