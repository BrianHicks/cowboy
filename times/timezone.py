'timezone class'
from datetime import tzinfo, timedelta

def parse_utc_offset(offset=None):
    if offset is None:
        return (None, None, None)

    return (
        {'+': 'east', '-': 'west'}[offset[0]],
        int(offset[1:3]),
        int(offset[3:5])
    )
