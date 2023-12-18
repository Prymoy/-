import pytest

def recursive_function(x, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return recursive_function(x, k // 2) ** 2
    else:
        return x * recursive_function(x, k - 1)

def non_recursive_function(x, k):
    result = 1
    while k > 0:
        if k % 2 == 0:
            x = x
            k //= 2
        else:
            result *= x
            k -= 1
    return result

@pytest.mark.parametrize("function", [recursive_function, non_recursive_function])
def test_functions(function):
    assert function(2, 3) == 8
    assert function(3, 4) == 81
    assert function(5, 0) == 1
    assert function(0, 5) == 0

if __name__ == '__main__':
    pytest.main()