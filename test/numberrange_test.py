import sure
from unittest import TestCase

from cowboy.numberrange import NumberRange

class NumberRangeTests(TestCase):
    'tests for NumberRange'
    def test_steps_default(self):
        'NumberRange has a sensible default granularity'
        steps = NumberRange(0, 5).steps()
        self.assertEqual(6, len(list(steps)))
