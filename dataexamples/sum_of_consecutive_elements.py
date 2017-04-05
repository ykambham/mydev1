# largest sum of consecutive integers in an array
elements = [1, 4, 2, 8, 9]
def largest_sum(elements):
    largest = 0
    for i in range(len(elements) - 1):
        if elements[i] + elements[i+1] > largest:
            largest = elements[i] + elements[i+1]
    return largest
print largest_sum(elements)

import unittest
class TestSum(unittest.TestCase):
    def init(self):
        self.elements = elements
    def test_elemtents(self):
        self.assertIsNotNone(self.elements, "List exists")
        
unittest.main()
        