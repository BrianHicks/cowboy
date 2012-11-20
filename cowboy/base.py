'base class - range'
class Range(object):
    'base class for ranges'
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def within(self, other):
        'test if an object is within the range'
        raise NotImplementedError

    def steps(self, resolution):
        'return a list of steps at the given resolution'
        raise NotImplementedError
