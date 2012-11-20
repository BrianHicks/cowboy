from unittest import TestCase

from datetime import datetime, timedelta
from cowboy.base import Range
from cowboy.daterange import DateRange

def test_lineage():
    assert issubclass(DateRange, Range)

class StepsTests(TestCase):
    def setUp(self):
        self.dr = DateRange(
            start=datetime(1970, 1, 1),
            end=datetime(1970, 2, 1)
        )

    def test_has_right_amount_for_month(self):
        'returns 32 for day (since it includes the end)'
        steps = self.dr.steps(timedelta(days=1))

        self.assertEqual(32, len(list(steps)))
