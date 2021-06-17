import unittest
from City_function import city_country 


class TestcaseCity(unittest.TestCase):
    def test_city_country(self):
        name =  city_country('Santiago', 'Chile', 5000000)
        self.assertEqual(name, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()