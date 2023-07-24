import unittest

from tire.carrigan_tire import CarriganTire


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tireweararray = [0, 0.9, 0.5, 0.8]
        tire = CarriganTire(tireweararray)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tireweararray = [0.8, 0.89, 0.1, 0.85]
        tire = CarriganTire(tireweararray)
        self.assertFalse(tire.needs_service())