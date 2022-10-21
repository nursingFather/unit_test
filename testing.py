import unittest
from main import Employee


class SalaryRaiseTestCase(unittest.TestCase):
    def SetUp(self):
        self.employee = Employee("olusegun", "oni", 130000)

    def test_give_default_raise(self):

        #"""does it increase 130000?"""
        trial = self.employee.give_raise()
        self.assertEqual(trial, 135000)


if __name__ == "__main__":
    unittest.main()