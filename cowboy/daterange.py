'date range object'
from cowboy.base import Range
from datetime import timedelta

class DateRange(Range):
    'represent a range of dates'
    default_granularity = timedelta(days=1)
