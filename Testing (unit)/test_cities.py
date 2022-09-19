import unittest
from city_func import location

class PlaceNameTest(unittest.TestCase):

    def test_full_location(self):

        together_location = location('Kyiv', 'ukraine')
        self.assertEqual(together_location, 'Kyiv, Ukraine')

    def test_full_location_population(self):

        together_location = location('kyiv', 'ukraine', 700000)
        self.assertEqual(together_location, 'Kyiv, Ukraine - 700000')

if __name__ == '__main__':
    unittest.main()