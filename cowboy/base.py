'base class - range'
class Range(object):
    'base class for ranges'
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, other):
        'test if an object is within the range'
        return self.start <= other and self.end >= other

    def steps(self, resolution):
        'return a list of steps at the given resolution'
        current = self.start
        while current <= self.end:
            yield current
            current += resolution
