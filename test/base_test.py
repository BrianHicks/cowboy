import sure
from unittest import TestCase

from datetime import datetime, timedelta
from cowboy.base import Range

class RangeTests(TestCase):
    def setUp(self):
        self.r = Range(0, 1)

    def test_assigns_start_end(self):
        'assigns start and end'
        self.r.start.should.equal(0)
        self.r.end.should.equal(1)

    def test_stubs_within(self):
        'stubs within'
        self.r.within.should.be.callable
        self.r.within.when.called_with().should.throw(NotImplementedError)

    def test_stubs_steps(self):
        'stubs steps'
        self.r.within.should.be.callable
        self.r.within.when.called_with().should.throw(NotImplementedError)
