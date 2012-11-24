'base class - range'
class Range(object):
    'base class for ranges'
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, other):
        'test if an object is within the range'
        return self.start <= other and self.end >= other

    def steps(self, granularity):
        '''return a list of steps at the given granularity

        if a subclass wants to provide a default for this, they should override
        the method signature to provide a default granularity.'''
        current = self.start
        while current <= self.end:
            yield current
            current += granularity
