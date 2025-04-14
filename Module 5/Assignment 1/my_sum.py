def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"


def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total