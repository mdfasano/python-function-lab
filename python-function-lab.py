# accepts a single integer
# returns the sum of the integers from 1 to n
def sum_to (n):
    if not isinstance(n, int):
        raise TypeError('value must be an integer')
    accumulator = 0
    if n > 0:
        for iter in range(1, n+1):
            accumulator += iter
    elif n <= 0:
        for iter in range(n, 0):
            accumulator += iter
    return accumulator

# takes a list of numbers
# returns the largest number in that list
def largest (num_list):
    current_largest = num_list[0]
    for number in num_list:
        if number > current_largest:
            current_largest = number
    return current_largest

# takes two string arguments
# counts the number of occurrences of str2 in str1
def occurrences (str1, str2):
    end_int = len(str1) - len(str2) + 1
    if end_int < 0:
        return 0
    counter = 0
    for iter in range(0, end_int):
        if str1.find(str2, iter, iter + len(str2)) != -1:
            counter += 1
    return counter

# takes an arbitrary number of numbers
# returns result of multiplying all together
def product (*args):
    result = 0
    for idx, num in enumerate(args):
        if idx == 0:
            result = num
        else:
            result *= num
    return result

# accepts a non-negative integer
# returns the number of steps it took
# to reduce the integer to zero
# If the current number is even, you have to divide it by 2
# otherwise, you have to subtract 1 from it
def steps_to_zero (num):
    if not isinstance(num, int):
        raise TypeError('value must be an integer')
    if num < 0:
        raise ValueError('value cannot be negative')
    counter = 0
    while (num != 0):
        if num %2 == 0:
            num /= 2
        else:
            num -= 1
        counter += 1
    return counter