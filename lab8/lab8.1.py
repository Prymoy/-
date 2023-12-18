import sys
import os

def limit_hp(min_hp, max_hp):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Получаем текущее количество HP героя
            hp = func(*args, **kwargs)

            # Проверяем, чтобы HP не превышало максимальное значение
            if hp > max_hp:
                hp = max_hp

            # Проверяем, чтобы HP не было меньше минимального значения
            if hp < min_hp:
                hp = min_hp

            # Возвращаем скорректированное количество HP
            return hp
        return wrapper
    return decorator

def suppress_output(func):
    def wrapper(*args, **kwargs):
        # Сохраняем текущее значение sys.stdout
        original_stdout = sys.stdout

        # Переопределяем sys.stdout для подавления вывода на консоль
        sys.stdout = open(os.devnull, 'w')

        # Вызываем функцию, но ее вывод не будет виден на консоли
        result = func(*args, **kwargs)

        # Восстанавливаем оригинальное значение sys.stdout
        sys.stdout = original_stdout

        # Возвращаем результат выполнения функции
        return result
    return wrapper

# Пример использования замыкания для отслеживания HP героя
@limit_hp(0, 100)
def hero_hp(hp_change):
    # Увеличиваем или уменьшаем количество HP героя на заданную величину
    global hero_hp_value
    hero_hp_value += hp_change
    return hero_hp_value

# Пример использования декоратора для подавления вывода функции на консоль
@suppress_output
def example_function():
    print("This text will not be shown on the console.")

# Инициализация переменной hero_hp_value
hero_hp_value = 50

# Пример вызова функции с использованием замыкания
print(hero_hp(20))  # Выведет: 70
print(hero_hp(-30))  # Выведет: 40
print(hero_hp(-100))  # Выведет: 0
print(hero_hp(200))  # Выведет: 100

# Пример вызова функции с использованием декоратора
example_function()  # На консоли ничего не будет выведено