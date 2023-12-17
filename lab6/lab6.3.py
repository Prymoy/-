from itertools import count, islice
from math import prod

def get_smallest_divisors(n):
    """
    Возвращает список из 5 наименьших делителей числа n.
    """
    divisors = []
    divisor_candidate = 2

    while len(divisors) < 5 and divisor_candidate <= n:
        if n % divisor_candidate == 0:
            divisors.append(divisor_candidate)
        divisor_candidate += 1

    return divisors

def find_numbers():
    numbers = []
    
    for n in islice(count(200000001), None):
        divisors = get_smallest_divisors(n)
        product = prod(divisors)

        if 0 < product < n:
            numbers.append((n, product))

        if len(numbers) == 5:
            break

    return sorted(numbers, key=lambda x: x[0])

result = find_numbers()
for n, m in result:
    print(f"M({n}) = {m}")