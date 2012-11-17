'tests for timezone'
from datetime import tzinfo
from unittest import TestCase

from times.timezone import TimeZone


class MetaTests(TestCase):
    'test subclasses, special cases in docs for tzinfo'
    def test_subclass(self):
        'TimeZone is a subclass of tzinfo'
        self.assertTrue(issubclass(TimeZone, tzinfo))

    def test_init_takes_no_arguments(self):
        '__init__ takes no arguments (so it can be unpickled)'
        # see http://docs.python.org/2/library/datetime.html#tzinfo-objects
        try:
            TimeZone()
        except Exception as err:
            self.fail(
                'TimeZone cannot be instantiated with no arguments. Error: %s' % err
            )
