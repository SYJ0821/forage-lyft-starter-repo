import unittest

from tire.octoprime_tire import OctoprimeTire


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tireweararray = [0.7, 0.7, 0.8, 0.8]
        tire = OctoprimeTire(tireweararray)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tireweararray = [0.7, 0.6, 0.7, 0.85]
        tire = OctoprimeTire(tireweararray)
        self.assertFalse(tire.needs_service())