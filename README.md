# COWBOY

[![Build Status](https://secure.travis-ci.org/BrianHicks/cowboy.png?branch=master)](https://travis-ci.org/BrianHicks/cowboy)

It works on ranges.

## Do it!

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

one_through_ten.steps(resolution=1) # Generator yielding [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Things that are done

Range (and DateRange, specifically) object, supporting `contains` and `steps`

### Things I'd like to do

adding and subtracting, length, special before and after
