import unittest
import hello_world_python

class TestHelloWorldPython(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world_python.hello_world(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
