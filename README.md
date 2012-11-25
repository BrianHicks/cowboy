# COWBOY

[![Build Status](https://secure.travis-ci.org/BrianHicks/cowboy.png?branch=master)](https://travis-ci.org/BrianHicks/cowboy)

It works on ranges.

## Installation

In the **future** you'll be able to install from PyPI. [Progress on
release.](https://github.com/BrianHicks/cowboy/issues?milestone=1&state=open)
For now, do this to get the non-production-ready code on your machine:

    git clone https://github.com/BrianHicks/cowboy.git
    pip install -r requirements.txt
    nosetests

## How to do stuff with Cowboy

Make a range:

```python
import datetime
from cowboy import DateRange

first_quarter = DateRange(
    start=datetime(2012, 1, 1),
    end=datetime(2012, 3, 31)
)
```

See if an arbitrary value is within the range:

```python
first_quarter.contains(datetime(2012, 2, 1)) # True
```

Step through all the values in the range:

```python
from cowboy import NumberRange

one_through_ten = NumberRange(1, 10)

one_through_ten.steps(granularity=1) # Generator yielding [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Add two ranges:

```python
from cowboy import NumberRange

fst, snd = NumberRange(1, 2), NumberRange(3, 4)

fst + snd # <NumberRange: 1 to 4>
```

Check validity of a range:

```python
from cowboy import NumberRange

NumberRange(1, 2).is_valid # True
NumberRange(2, 1).is_valid # False
```

## Make your own ranges

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
