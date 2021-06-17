import unittest
from City_function import city_country


class TestCaseCity(unittest.TestCase):
    def test_city_country(self):
        name = city_country('Santiago', 'Chile')
        self.assertEqual(name, 'Santiago, Chile')

    def test_city_pop_country(self):
        name = city_country('Santiago', 'Chile', 5000000)
        self.assertEqual(name, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
