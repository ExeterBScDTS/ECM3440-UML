# Class-generator

## Tests

This code used the **pytest** framework.  If you are working in VS Code you should enable this testing framework, for instructions see <https://code.visualstudio.com/docs/python/testing>

### Writing tests

Consider *equivalence partitioning*, e.g. write tests for inputs, and outputs, with common characteristics. This will usually include writing tests that ensure the correct exception is thrown for invalid inputs.

### Exceptions

To catch and examine exceptions in a test use ```import pytest``` and code like this -

```python
with pytest.raises(Exception) as exp:
    # code that raises exception
assert str(exp.value) == 'Invalid arguments to myfunc.'
```

### *Happy path*

Always write tests that check your code is doing as expected. It isn't always necessary to test for exact values, as test data may change in future.  Consider testing
the type of retured values like this -

``` python
assert isinstance(text,str)
```

### TDD and unit tests

When writing code and tests simultaneously it is often necessary to examine the value of variables, rather than use ```print()``` statements consider using ```breakpoint()``` to examine variables in the Python debugger.

Unit tests should be simple, test just one thing, and *cheap*, very quick to run.  This ensures if the test breaks it is easy to fix the code and that the tests can be run frequently during coding.  Where possible run your entire unit test suite for every code change.

### Feature and integration tests

Unit tests ensure individual functions behave as expected, but do not test other important aspects of the code base.

Using fixtures <https://docs.pytest.org/en/6.1.1/fixture.html>

### Mocking

<https://medium.com/javascript-scene/mocking-is-a-code-smell-944a70c90a6a>

Things you might mock

* Web API
* Database connection
* Physcial devices
* Long running processes
