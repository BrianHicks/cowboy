'date range object'

class DateRange(object):
    'represent a range of dates'
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, date):
        'test if this range contains a date'
        return self.start <= date and self.end >= date

    def steps(self, delta):
        'returns the steps between start and end at delta resolution'
        current = self.start
        while current <= self.end:
            yield current
            current += delta
