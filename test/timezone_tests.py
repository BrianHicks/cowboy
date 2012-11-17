'tests for timezone'
from datetime import tzinfo, timedelta, datetime
from unittest import TestCase

from times.timezone import parse_utc_offset


#class MetaTests(TestCase):
    #'test subclasses, special cases in docs for tzinfo'
    #def test_subclass(self):
        #'TimeZone is a subclass of tzinfo'
        #self.assertTrue(issubclass(TimeZone, tzinfo))

    #def test_init_takes_no_arguments(self):
        #'__init__ takes no arguments (so it can be unpickled)'
        ## see http://docs.python.org/2/library/datetime.html#tzinfo-objects
        #try:
            #TimeZone()
        #except Exception as err:
            #self.fail(
                #'TimeZone cannot be instantiated with no arguments. Error: %s' % err
            #)

class ParseUtcOffsetTests(TestCase):
    'parse_utc_offset tests'
    def test_none(self):
        self.assertEqual(
            (None, None, None),
            parse_utc_offset(None)
        )

    def test_positive(self):
        self.assertEqual(
            ('east', 0, 0),
            parse_utc_offset('+0000')
        )

    def test_negative(self):
        self.assertEqual(
            ('west', 0, 0),
            parse_utc_offset('-0000')
        )

    def test_hours(self):
        self.assertEqual(
            ('west', 5, 0),
            parse_utc_offset('-0500')
        )

    def test_minutes(self):
        self.assertEqual(
            ('west', 0, 30),
            parse_utc_offset('-0030')
        )
