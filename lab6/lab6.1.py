def count_valid_codes():
    """
    Считает количество различных кодовых слов, которые может использовать Иван.

    Returns:
    int: Количество различных кодовых слов.
    """
    # Создаем алфавит
    alphabet = ['A', 'B', 'C', 'D', 'E']

    # Генерируем все пятибуквенные слова
    words = [a + b + c + d + e for a in alphabet for b in alphabet
             for c in alphabet for d in alphabet for e in alphabet]

    # Фильтруем слова по условиям
    valid_words = [word for word in words if word[0] != 'E' and word[-1] != 'A']

    # Возвращаем количество слов
    return len(valid_words)

# Пример использования
result = count_valid_codes()
print(result)