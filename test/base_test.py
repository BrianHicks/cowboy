import sure
from unittest import TestCase

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
        r = Range(0, 2)
        r.contains.when.called_with(1).should.return_value(True)

    def test_before(self):
        r = Range(1, 2)
        r.contains.when.called_with(0).should.return_value(False)

    def test_after(self):
        r = Range(0, 1)
        r.contains.when.called_with(2).should.return_value(False)

    def test_stubs_steps(self):
        'stubs steps'
        r = Range(0, 1)
        r.steps.should.be.callable
        r.steps.when.called_with().should.throw(NotImplementedError)

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
