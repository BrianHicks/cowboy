'tests for convenient imports'
from unittest import TestCase

class ImportTests(TestCase):
    def test_import_range(self):
        'Range can be imported from a variety of places'
        try:
            from cowboy import Range
        except ImportError:
            self.fail('Range is not in cowboy')

        try:
            from cowboy.base import Range
        except ImportError:
            self.fail('Range is not in cowboy.base')

    def test_import_daterange(self):
        'DateRange can be imported from a variety of places'
        try:
            from cowboy import DateRange
        except ImportError:
            self.fail('DateRange is not in cowboy')

        try:
            from cowboy.daterange import DateRange
        except ImportError:
            self.fail('DateRange is not in cowboy.daterange')
