import sure
from unittest import TestCase
import operator

from datetime import datetime, timedelta
from cowboy.base import Range

class RangeTests(TestCase):
    'tests for Range'
    def test_assigns_start_end(self):
        'assigns start and end'
        r = Range(0, 1)
        r.start.should.equal(0)
        r.end.should.equal(1)

    # contains
    def test_within(self):
        self.assertIn(1, Range(0, 2))

    def test_before(self):
        self.assertNotIn(0, Range(1, 2))

    def test_after(self):
        self.assertNotIn(2, Range(0, 1))


class RangeStepTests(TestCase):
    'tests for Range.step'
    # steps
    def test_steps_generator(self):
        'steps is a generator'
        steps = Range(0, 10).steps(1)
        steps.should.have.property('next')

    def test_steps_start(self):
        'steps always returns start'
        steps = list(Range(0, 10).steps(1))
        (0).should.be.within(steps)

    def test_steps_end_sometimes(self):
        'steps sometimes returns end'
        no = list(Range(0, 10).steps(3))
        (10).should_not.be.within(no)

        yes = list(Range(0, 10).steps(1))
        (10).should.be.within(yes)

    def test_repr(self):
        'repr should be correct'
        self.assertEqual(
            '<Range: 1 to 2>',
            repr(Range(1, 2))
        )


class RangeAddTests(TestCase):
    'tests for adding ranges'
    def test_add_start(self):
        'add uses the first start'
        a, b = Range(0, 1), Range(1, 2)
        (a + b).start.should.equal(0)

    def test_add_end(self):
        'add uses the last end'
        a, b = Range(0, 1), Range(1, 2)
        (a + b).end.should.equal(2)

    def test_other_class(self):
        'add raises a TypeError if two unlike classes are passed'
        a = type('a', (Range,), {})(1, 2)
        b = type('b', (Range,), {})(3, 4)
        operator.add.when.called_with(a, b).should.throw(
            TypeError, 'Cannot add two unlike types'
        )
