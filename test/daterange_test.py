from unittest import TestCase

from datetime import datetime, timedelta
from cowboy.daterange import DateRange

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


class StepsTests(TestCase):
    def setUp(self):
        self.dr = DateRange(
            start=datetime(1970, 1, 1),
            end=datetime(1970, 2, 1)
        )

    def test_returns_generator(self):
        'returns a generator'
        steps = self.dr.steps(timedelta(days=1))

        self.assertTrue(hasattr(steps, 'next'))

    def test_returns_start(self):
        'always returns start'
        steps = self.dr.steps(timedelta(days=1))

        self.assertEqual(datetime(1970, 1, 1), steps.next())

    def test_may_return_end(self):
        'may return end'
        steps = self.dr.steps(timedelta(days=1))

        self.assertIn(datetime(1970, 2, 1), list(steps))

    def test_has_right_amount_for_month(self):
        'returns 32 for day (since it includes the end)'
        steps = self.dr.steps(timedelta(days=1))

        self.assertEqual(32, len(list(steps)))
