from concurrent.futures import ThreadPoolExecutor

def parallel_sequence_combiner(sequence1, sequence2, strategy):
    """
    Многопоточная версия генератора для объединения двух последовательностей.

    Parameters:
    - sequence1: Первая последовательность.
    - sequence2: Вторая последовательность.
    - strategy: Функция, определяющая стратегию объединения элементов.

    Yields:
    - Элемент, полученный в результате объединения двух элементов по стратегии.

    Examples:
    >>> seq1 = [1, 2, 3, 4]
    >>> seq2 = [5, 6, 7, 8]
    >>> strategy_add = lambda x, y: x + y
    >>> list(parallel_sequence_combiner(seq1, seq2, strategy_add))
    [6, 8, 10, 12]
    """
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(strategy, item1, item2) for item1, item2 in zip(sequence1, sequence2)]
        for future in futures:
            yield future.result()

# Тесты для многопоточной версии
def test_parallel_combine_sequences():
    seq1 = [1, 2, 3, 4]
    seq2 = [5, 6, 7, 8]

    result = list(parallel_sequence_combiner(seq1, seq2, lambda x, y: x + y))
    assert result == [6, 8, 10, 12]

    result = list(parallel_sequence_combiner(seq1, seq2, lambda x, y: x * y))
    assert result == [5, 12, 21, 32]