from op import *

def test_add():
    # Test case 1: Adding positive numbers
    assert add(2, 3) == 5

    # Test case 2: Adding negative numbers
    assert add(-2, -3) == -5

    # Test case 3: Adding zero to a number
    assert add(5, 0) == 5

    # Test case 4: Adding floating-point numbers
    assert add(2.5, 3.7) == 6.2

    # Test case 5: Adding large numbers
    assert add(1000000, 2000000) == 3000000

def test_subtract():
    # Test case 1: Subtracting positive numbers
    assert subtract(5, 3) == 2

    # Test case 2: Subtracting negative numbers
    assert subtract(-5, -3) == -2

    # Test case 3: Subtracting zero from a number
    assert subtract(5, 0) == 5

    # Test case 4: Subtracting floating-point numbers
    assert subtract(2.5, 1.7) == 0.8

    # Test case 5: Subtracting large numbers
    assert subtract(1000000, 200000) == 800000

def test_divide():
    # Test case 1: Dividing positive numbers
    assert divide(10, 2) == 5

    # Test case 2: Dividing negative numbers
    assert divide(-10, -2) == 5

    # Test case 3: Dividing zero by a number
    assert divide(0, 5) == 0

    # Test case 4: Dividing floating-point numbers
    assert divide(2.5, 0.5) == 5

    # Test case 5: Dividing by zero (expecting a ZeroDivisionError)
    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError"

def test_mul():
    # Test case 1: Multiplying positive numbers
    assert mul(2, 3) == 6

    # Test case 2: Multiplying negative numbers
    assert mul(-2, -3) == 6

    # Test case 3: Multiplying zero with a number
    assert mul(5, 0) == 0

    # Test case 4: Multiplying floating-point numbers
    assert mul(2.5, 1.5) == 3.75

    # Test case 5: Multiplying large numbers
    assert mul(1000000, 2000000) == 2000000000000

