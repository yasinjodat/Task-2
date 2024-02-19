from main import StudentsInMLOPs
import unittest

class TestMyClass(unittest.TestCase):
    def test_say_hello(self):
        obj = StudentsInMLOPs()
        obj.enrollstudents(1,2)
        self.assertEqual(obj.getTotalStrength(),1 )

    def test_class_variable(self):
        obj = StudentsInMLOPs()
        obj.enrollstudents(2,3)
        self.assertEqual(obj.getClassName(), [3])

if __name__ == "__main__":
    unittest.main()