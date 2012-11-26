'base class - range'
from __future__ import unicode_literals
from cowboy.errors import InvalidRangeError

class Range(object):
    'base class for ranges'
    def __init__(self, start, end):
        if start > end:
            raise InvalidRangeError(
                "start must be less than or equal to end"
            )

        self.start = start
        self.end = end

    def steps(self, granularity):
        '''return a list of steps at the given granularity

        if a subclass wants to provide a default for this, they should override
        the method signature to provide a default granularity.'''
        current = self.start
        while current <= self.end:
            yield current
            current += granularity

    def __contains__(self, other):
        'test if an object is within the range'
        return self.start <= other and self.end >= other

    def __repr__(self):
        'return a nice representation of an instance'
        return '<%s: %s to %s>' % (
            self.__class__.__name__,
            repr(self.start), repr(self.end)
        )

    def __add__(self, other):
        'get the union of two ranges'
        if type(self) != type(other):
            raise TypeError('Cannot add two unlike types')

        return self.__class__(
            min([self.start, other.start]),
            max([self.end, other.end])
        )

    def intersect(self, other):
        'return intersection of self and other (may return an invalid range)'
        return self.__class__(
            max([self.start, other.start]),
            min([self.end, other.end])
        )

    def __eq__(self, other):
        'equality of two ranges'
        return type(self) == type(other) and self.start == other.start and self.end == other.end

    def __hash__(self):
        'return the hash of this object' # TODO: find out if this is the best way to do this
        return id(self)


class MultiRange(object):
    def __init__(self, *ranges):
        self.ranges = set(ranges)

    def __contains__(self, value):
        'see if any member ranges contain the value'
        return any([value in member for member in self.ranges])

    def __eq__(self, other):
        return self.ranges == other.ranges

    def __repr__(self):
        return '<MultiRange: %s>' % self.ranges
