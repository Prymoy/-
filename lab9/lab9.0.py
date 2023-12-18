import pytest
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

def combine_sequences(seq1, seq2, strategy='sequential'):
    if strategy == 'sequential':
        return [item for sublist in zip(seq1, seq2) for item in sublist]
    elif strategy == 'parallel':
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(lambda x, y: [x, y], x, y) for x, y in zip(seq1, seq2)]
            wait(futures, return_when=FIRST_COMPLETED)
            return [future.result() for future in futures]
    else:
        raise ValueError("Invalid strategy. Use 'sequential' or 'parallel'.")

def test_combine_sequences_sequential():
    result = combine_sequences([1, 2, 3], ['a', 'b', 'c'], strategy='sequential')
    assert result == [1, 'a', 2, 'b', 3, 'c']

def test_combine_sequences_parallel():
    result = combine_sequences([1, 2, 3], ['a', 'b', 'c'], strategy='parallel')
    assert result == [[1, 'a'], [2, 'b'], [3, 'c']]

def test_combine_sequences_invalid_strategy():
    with pytest.raises(ValueError):
        combine_sequences([1, 2, 3], ['a', 'b', 'c'], strategy='invalid')

def benchmark_sequential():
    seq1 = list(range(1, 1001))
    seq2 = list(range(1001, 2001))
    combine_sequences(seq1, seq2, strategy='sequential')

def benchmark_parallel():
    seq1 = list(range(1, 1001))
    seq2 = list(range(1001, 2001))
    combine_sequences(seq1, seq2, strategy='parallel')

if __name__ == "__main__":
    # Запуск бенчмарков
    benchmark_sequential()
    benchmark_parallel()