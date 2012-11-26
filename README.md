# COWBOY

[![Build Status](https://secure.travis-ci.org/BrianHicks/cowboy.png?branch=master)](https://travis-ci.org/BrianHicks/cowboy)

It works on ranges.

## Installation

`pip install cowboy`

### Installing for development

    git clone https://github.com/BrianHicks/cowboy.git
    pip install -r requirements.txt
    python setup.py develop
    nosetests

## How to do stuff with Cowboy

Construct a range:

```python
import datetime
from cowboy import DateRange

first_quarter = DateRange(
    start=datetime(2012, 1, 1),
    end=datetime(2012, 3, 31)
)
```

See if an arbitrary value is within the range, matching on start and end.
`O(2)`:

```python
datetime(2012, 2, 1) in first_quarter # True
```

Step through all the values in the range. Generator returns `O(2n+1)` where `n`
is the delta of the start and end:

```python
from cowboy import NumberRange

one_through_ten = NumberRange(1, 10)

one_through_ten.steps(granularity=1) # Generator yielding [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Working with multiple ranges

You can add two ranges in the obvious manner (takes the lesser of the starts
and the greater of the ends):

```python
fst, snd = NumberRange(1, 2), NumberRange(3, 4)

fst + snd # <NumberRange: 1 to 4>
```

In real life, that's not always how you want to combine sets. Take for example,
a circus, where we want to quickly see if the circus is showing any particular
day:

```python
from cowboy import MultiRange

circus_schedule = MultiRange(
    DateRange(datetime(2012, 1, 1), datetime(2012, 1, 3)),
    DateRange(datetime(2012, 1, 8), datetime(2012, 1, 10))
)
datetime(2012, 1, 2) in circus_schedule # True
datetime(2012, 1, 9) in circus_schedule # True
```

You can also get the intersection of two ranges. This works a little bit like
`set.intersection` but might raise a `InvalidRangeError` if the start is
greater than the end. Essentially, this tries to create a new Range with the
greater of the starts and the lesser of the ends:

```python
fst, snd = NumberRange(1, 3), NumberRange(2, 4)
fst.intersection(snd) # <NumberRange: 2 to 3>
```

### Make your own ranges

Say you wanted to make your own Range for chars, so that `CharRange('a', 'c')`
made sense. That class would look something like this:

```python
from cowboy.base import Range

class CharRange(Range):
    'a range of characters'
    def steps(self, granularity=1): # most subclasses will override just granularity
        current = ord(self.start)
        while current <= ord(self.end):
            yield chr(current)
            current += granularity
```

Now you can use all the methods outlined above to operate on ranges of characters.
