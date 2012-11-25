from unittest import TestCase
import operator

from datetime import datetime, timedelta
from cowboy.base import Range

class RangeTests(TestCase):
    'tests for Range'
    def test_assigns_start_end(self):
        'assigns start and end'
        r = Range(0, 1)
        self.assertEqual(r.start, 0)
        self.assertEqual(r.end, 1)

    # contains
    def test_within(self):
        self.assertTrue(1 in Range(0, 2))

    def test_before(self):
        self.assertFalse(0 in Range(1 ,2))

    def test_after(self):
        self.assertFalse(3 in range(1, 2))

    # is_valid
    def test_validity_true(self):
        self.assertTrue(Range(1, 2).is_valid)

    def test_validity_false(self):
        self.assertFalse(Range(2, 1).is_valid)

    # adding
    def test_add_start(self):
        'add uses the first start'
        a, b = Range(0, 1), Range(1, 2)
        self.assertEqual(0, (a + b).start)

    def test_add_end(self):
        'add uses the last end'
        a, b = Range(0, 1), Range(1, 2)
        self.assertEqual(2, (a + b).end)

    def test_other_class(self):
        'add raises a TypeError if two unlike classes are passed'
        a = type('a', (Range,), {})(1, 2)
        b = type('b', (Range,), {})(3, 4)
        self.assertRaisesRegexp(
            TypeError, 'Cannot add two unlike types',
            operator.add, a, b
        )

    # equality
    def test_eq_like_ranges(self):
        'like ranges are equal'
        a, b = Range(0, 1), Range(0, 1)
        self.assertTrue(a == b)

    def test_eq_unlike_ranges(self):
        'unlike ranges are not equal'
        a, b = Range(0, 1), Range(2, 3)
        self.assertFalse(a == b)

    def test_eq_unlike_types(self):
        'unlike types are not equal'
        a = type('a', (Range,), {})(1, 2)
        b = type('b', (Range,), {})(1, 2)
        self.assertFalse(a == b)


class RangeStepTests(TestCase):
    'tests for Range.step'
    # steps
    def test_steps_generator(self):
        'steps is a generator'
        steps = Range(0, 10).steps(1)
        self.assertTrue(hasattr(steps, 'next'))

    def test_steps_start(self):
        'steps always returns start'
        steps = list(Range(0, 10).steps(1))
        self.assertTrue(0 in steps)

    def test_steps_end_sometimes(self):
        'steps sometimes returns end'
        no = list(Range(0, 10).steps(3))
        self.assertFalse(10 in no)

        yes = list(Range(0, 10).steps(1))
        self.assertTrue(10 in yes)

    def test_repr(self):
        'repr should be correct'
        self.assertEqual(
            '<Range: 1 to 2>',
            repr(Range(1, 2))
        )
