from functools import lru_cache
import pytest

@lru_cache(maxsize=None)
def recursive_function_memoized(x, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return recursive_function_memoized(x, k // 2) ** 2
    else:
        return x * recursive_function_memoized(x, k - 1) 

def test_recursive_function_memoized():
    assert recursive_function_memoized(2, 3) == 8
    assert recursive_function_memoized(3, 4) == 81
    assert recursive_function_memoized(5, 0) == 1
    assert recursive_function_memoized(0, 5) == 0

# Опционально: запустить тесты
if __name__ == '__main__':
    pytest.main()