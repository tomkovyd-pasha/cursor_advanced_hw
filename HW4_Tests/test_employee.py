import employee as Emp
import unittest
from unittest.mock import patch


class MockTestTrue:
    ok = True
    text = f'Inner function mocked - {ok}, request correct'

    def __init__(self, *args, **kwargs):
        pass


class MockTestFalse:
    ok = False
    text = f'Inner function mocked - {ok}, request incorrect'

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.test_employee_instance = Emp.Employee("Pasha", "Pasha2", 100000)

    def test_email(self):
        self.assertEqual(self.test_employee_instance.email, "Pasha.Pasha2@email.com")

    def test_fullname(self):
        self.assertEqual(self.test_employee_instance.fullname, "Pasha Pasha2")

    def test_apply_raise(self):
        self.test_employee_instance.apply_raise()
        self.assertEqual(self.test_employee_instance.pay, 105000)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mockRequestGet):
        mockRequestGet.side_effect = MockTestTrue
        print(self.test_employee_instance.monthly_schedule('1'))
        mockRequestGet.side_effect = MockTestFalse
        print(self.test_employee_instance.monthly_schedule('1'))
        self.assertEqual(self.test_employee_instance.monthly_schedule('1'), 'Bad Response!')

