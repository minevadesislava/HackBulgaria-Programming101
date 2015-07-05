def sum_of_divisors(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0 : 
            sum += i
    return sum 
'''
def sum_of_divisors(n):
return sum([x for x in range(1, n + 1) if n % x == 0])
'''

def is_prime(n):
    if n <= 0:
        bool_prime = False
    elif n == 1:
        bool_prime = False
    else:
        for i in range(1,n/2+1):
            if n % i == 0: 
                bool_prime = False
                break
            else:
                bool_prime = True
    return bool_prime
'''
def is_prime(n):
return n + 1 == sum_of_divisors(n)

def count_of_divisors(n):
return sum([1 for x in range(1, n + 1) if n % x == 0])
'''
    
def prime_number_of_divisors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0 : 
            count += 1
    return is_prime(count)
'''

def prime_number_of_divisors(n):
    is_prime(count_of_divisors(n))
'''

def contains_digit(number, digit):
    b = str(number)
    symbol= str(digit)
    if symbol in b:
        return True
    else:
        return False

def contains_digits(number, digits):
    b= str(number)
    c=[]
    for digit in b:
        c.append (int(digit))
    if c in number_str:
        return True
    else:
        return False

def is_number_balanced(n):
    nums = to_digit(n)
    half = len(nums) // 2
    left_nums = nums[0:half]
    if len(nums) % 2 == 0:
        right_nums = nums[half:]
    else:
        right_nums = nums[half + 1]
    return sum(left_nums) == sum(right_nums)
    
def count_substrings(haystack, needle):
    return haystack.count(needle)

def zero_insert(n):
    result = []
    digits = to_digits(n)
    start = 0
    end = len(digits)
    while start < end - 1:
        x = digits[start]
        y = digits[start + 1]
        result.append(x)
        if (x + y) % 10 == 0 or x == y:
            result.append(0)
        start += 1
        result.append(digits[start])
    return to_number(result)

def sum_matrix(m):
    result = 0
    for row in sum_matrix:
        result += sum(row)
    return result
'''
def sum_matrix(m):
    return sum([sum(row) for row in m])
'''

def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_bombing_plan(m)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)

if __name__ == '__main__':
    main()
