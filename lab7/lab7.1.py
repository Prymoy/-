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

if __name__ == '__main__':
    # Example usage:
    x_value = 2
    k_value = 5

    recursive_result = recursive_function(x_value, k_value)
    print(f"Recursive Result: {recursive_result}")

    non_recursive_result = non_recursive_function(x_value, k_value)
    print(f"Non-Recursive Result: {non_recursive_result}")