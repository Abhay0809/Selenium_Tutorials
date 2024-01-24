import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("I will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("This is setup method")
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("This is teardown method")
        print("I will run once after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after all tests")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
