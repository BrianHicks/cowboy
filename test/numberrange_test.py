from unittest import TestCase

from cowboy.base import Range
from cowboy.numberrange import NumberRange

def test_lineage():
    assert issubclass(NumberRange, Range)

class NumberRangeTests(TestCase):
    'tests for NumberRange'
    def test_steps_default(self):
        'NumberRange has a sensible default granularity'
        steps = NumberRange(0, 5).steps()
        self.assertEqual(6, len(list(steps)))

    def test_repr(self):
        'repr should be correct'
        self.assertEqual(
            '<NumberRange: 0 to 5>',
            repr(NumberRange(0, 5))
        )
