from unittest import TestCase
import operator
import types

from datetime import datetime, timedelta

from cowboy.base import Range, MultiRange
from cowboy.errors import InvalidRangeError

class RangeTests(TestCase):
    'tests for Range'
    def test_assigns_start_end(self):
        'assigns start and end'
        r = Range(0, 1)
        self.assertEqual(r.start, 0)
        self.assertEqual(r.end, 1)

    def test_eq_good(self):
        'does not raise InvalidRangeError if start == end'
        try:
            Range(0, 0)
        except InvalidRangeError:
            self.fail('raised InvalidRangeError with zero-length range')

    def test_raises_invalid_range(self):
        'raises InvalidRangeError if start > end'
        self.assertRaisesRegexp(
            InvalidRangeError, 'start must be less than or equal to end',
            Range, 1, 0
        )

    # contains
    def test_within(self):
        self.assertTrue(1 in Range(0, 2))

    def test_before(self):
        self.assertFalse(0 in Range(1 ,2))

    def test_after(self):
        self.assertFalse(3 in range(1, 2))

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
        self.assertRaises(
            TypeError,
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

    # intersection
    def test_intersection_overlap(self):
        a, b = Range(1, 3), Range(2, 4)
        self.assertEqual(
            a.intersect(b),
            Range(2, 3)
        )

    def test_intersection_inner_set(self):
        a, b = Range(1, 4), Range(2, 3)
        self.assertEqual(
            a.intersect(b),
            Range(2, 3)
        )

    def test_intersection_none(self):
        a, b = Range(1, 2), Range(3, 4)
        self.assertRaises(
            InvalidRangeError,
            a.intersect, b
        )


class RangeStepTests(TestCase):
    'tests for Range.step'
    # steps
    def test_steps_generator(self):
        'steps is a generator'
        steps = Range(0, 10).steps(1)
        self.assertTrue(isinstance(steps, types.GeneratorType))

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

    # hash
    def test_hash(self):
        'hash of Range object'
        r = Range(1, 2)
        self.assertEqual(id(r), hash(r))


class MultiRangeTests(TestCase):
    'tests for MultiRange'
    def test_contains(self):
        'test contains'
        mr = MultiRange(
            Range(1, 3),
            Range(5, 7)
        )
        self.assertTrue(2 in mr)
        self.assertFalse(4 in mr)
        self.assertTrue(6 in mr)

    def test_equal(self):
        'two multiranges equal each other'
        r = Range(1, 2)
        a, b = MultiRange(r), MultiRange(r)
        self.assertEqual(a, b)

    def test_repr(self):
        'repr returns an informative string'
        self.assertEqual(
            '<MultiRange: {<Range: 1 to 2>}>',
            repr(MultiRange(Range(1, 2)))
        )
