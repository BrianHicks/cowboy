'timezone class'
from datetime import tzinfo

class TimeZone(tzinfo):
    'timezone object'
    def __init__(self, offset=0):
        self.offset = 0
