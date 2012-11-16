from unittest import TestCase

from datetime import datetime
from times.daterange import DateRange

class ContainsTests(TestCase):
    'test DateRange.contains'
    def test_within(self):
        'contains returns true for a date within the range'
        dr = DateRange(
            start=datetime(1970, 1, 1),
            end=datetime(1970, 1, 3)
        )
        self.assertTrue(dr.contains(datetime(1970, 1, 2)))

    def test_before(self):
        'contains returns false for a date before the range'
        dr = DateRange(
            start=datetime(1970, 1, 2),
            end=datetime(1970, 1, 3)
        )
        self.assertFalse(dr.contains(datetime(1970, 1, 1)))

    def test_after(self):
        'contains returns false for a date before the range'
        dr = DateRange(
            start=datetime(1970, 1, 1),
            end=datetime(1970, 1, 2)
        )
        self.assertFalse(dr.contains(datetime(1970, 1, 3)))
