def binary_expression():
    """
    Считает количество единиц в двоичной записи значения выражения.

    Returns:
    int: Количество единиц в двоичной записи значения выражения.
    """
    result = (4 ** 511 + 2) - 511
    binary_result = bin(result)[2:]  # Преобразуем результат в двоичную запись и убираем префикс '0b'
    return binary_result.count('1')

# Пример использования
result = binary_expression()
print(result)