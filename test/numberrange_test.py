import sure
from unittest import TestCase

from cowboy.numberrange import NumberRange

class NumberRangeTests(TestCase):
    'tests for NumberRange'
    def test_default(self):
        'NumberRange has a sensible default granularity'
        NumberRange.default_granularity.should.equal(1)
