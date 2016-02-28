import unittest
from binsearch import binary_search

class MyTest(unittest.TestCase):
    input = list(range(10))

    def test_basicfunctionality(self):
        self.assertEqual(binary_search(self.input,5),5)
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 4), -1)
        self.assertEqual(binary_search(self.input, 5, 1,3), -1)
        self.assertEqual(binary_search(self.input, 2, 1,3), 2)
        self.assertEqual(binary_search(self.input, 2, 3, 1), -1)
        self.assertEqual(binary_search(self.input, 2, 2, 2), 2)
        self.assertEqual(binary_search(self.input, 5, 2, 2), -1)

    def test_badinput(self):
        import numpy as np
        self.assertEqual(binary_search([1,2,np.inf], 2), 1)
        self.assertEqual(binary_search([1,2,np.inf], np.inf), 2)
        self.assertEqual(binary_search([],1),-1)
        with self.assertRaises(TypeError):
            binary_search(['a',3],1)
        with self.assertRaises(TypeError):
            binary_search(['a',3],'a')

    def test_needles(self):
        self.assertEqual(binary_search(self.input, 4.5), -1)
        self.assertEqual(binary_search(self.input, 10), -1)
        self.assertEqual(binary_search(self.input, 0), 0)
        self.assertEqual(binary_search(self.input, 100), -1)
        
suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)
