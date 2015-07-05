#task 1
def count_words(arr):
    return dict( (i, arr.count(i)) for i in arr)
#task 2 
def unique_words_count(arr):
    return len(dict((i, arr.count(i)) for i in arr)) 
#task 3
def nan_expand(times):
    nan= ""
    if times == 0:
        return " "" "
    else:
        for i in range(times):
            nan = nan[ :len(nan)] + "Not a "
        return nan[ :len(nan)] + "NaN"
#task 4
def iterations_of_nan_expand(expanded):
    if expanded == nan_expand(expanded.count("Not a")):
        return expanded.count("Not a")
    else:
        return False
#task 5
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
#task 6 
def group(lst):
    result = []
    same = []
    for i in range(len(lst)):
        if i == 0:
            same = [lst[i]]
        else:
            if lst[i] == lst[i-1]:
                same.append(lst[i])
            else:
                result.append(same)
                same = [lst[i]]
    result.append(same)
    return result
#task 7
def max_consecutive(items):
    return max(len(i) for i in group(items))

#task 8
def groupby(func, seq):
    result = {}
    keys = { func(element) for element in seq}
    for key in keys:
        result[key] = [element for element in seq if func(element) == key]
    return result

#task 9
def prepare_meal(number):
    result = ""
    count3 = 0
    while number % 3 == 0:
        count3 += 1
        number/ 3 
    result += " ".join(["spam" for i in range(count3)])
    if number % 5 == 0:
         result += " ".join(["eggs" if count3 == 0 else " and eggs"])

    return result
#task 10
def reduce_filpath(path):
    path = [x for x in path.split('/') if x != '' and x != '.' and x != '/']

    for element in path:
        if element == '..':
            del path[ path.index[element] - 1 : ]

    index = 0

    while index <= len(path) - 1:
        path.insert(index, '/')
        index += 2

    path = ''.join(path)

    return path

#task 11
def is_an_bn(word):
    lst = list(word)
    counta = lst.count("a")
    countb = lst.count("b")
    if counta == countb:
        return True
    return False
 #task 12
 def is_credit_card_valid(number):
    pass