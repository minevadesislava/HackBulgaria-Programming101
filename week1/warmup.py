def factorial(n):
    ''' result=1
     if (n==0 or n==1):
        return result
     else:
        for i in range(n):
            result= result*(i+1)
        return result'''
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result

def fibonacci(n):
    '''list1=[]
    if n==1:
        list1=[1]
    elif n==2:
        list1=[1,1]
    else:
        list1=[1,1]
        for i in range(2,n):
            new_number= list1[i-1] + list1[i-2]
            list1.append(new_number)
    return list1 '''
    result = []
    a = 1
    b = 1
     while len(result) < n:
        result.append(a)
        next_fib = a + b
        a = b
        b = next_fib
     return result

def sum(n):
   ''' if n >= 0:
        num = n
    else:
        num = abs(n)
    results = 0
    while num > 0:
        remainder = num % 10
        results += remainder
        num = (num-remainder)/10
    return results '''
    return sum(to_digits(n))
    
def fact_digits(n):
    '''results=0
    while n > 0:
        remainder = n % 10
        results += factorial(remainder)
        n = (n- remainder)/10
    return results'''
    return sum([factorial(x) for x in to_digits(n)])

def palindrome(obj):
    #word= str(obj)
    #word.lower()
    #for i,char in enumerate(word):
        #if char != word[-i-1]:
        #   return False
        #return True
        return obj== obj[::-1]

def to_digits(n):
    '''b= str(n)
    c=[]
    for digit in b:
        c.append (int(digit))
    return c'''
    return [int(x) for x in str(n)]

def to_number(digits):
    s = map(str, digits)
    s = ''.join(s)
    s = int(s)
    return s

def fib_number(n):
    return to_number(fibonacci(n))

def count_vowels(str4):
    vowel=("aeiouyAEIOUY")
    count=0
    for i in str4:
        if i in vowel:
            count +=1
    return count

def count_consonants(str5):
    consonants=("bcdfghjklmnpqrstvwxzBCDFGHJKLMNOPQRSTVWXZ")
    count=0
    for i in str5:
        if i in consonants:
            count +=1
    return count

def char_histogram(string):
    list_str=list(string)
    dict={}
    for i in list_str:
        dict[i]=list_str.count(i)
    return dict


def p_score(n):
    if palindrome(n)== True:
        return 1
    else:
        return (1+p_score( n + int(str(n)[::-1])) )


def is_increasing(seq):
    for i in range(0,len(seq)-1):
        if seq[i] > seq[i+1]:
            return False
    return True

def is_decreasing(seq):
    for i in range(0,len(seq)-1):
        if seq[i] < seq[i+1]:
            return False
    return True

def even(n):
    return n % 2 == 0

def odd(n):
    return not even(n)

def is_hack(n):
    binary_n = bin(n)[2:]
    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))
    return is_palindrome and has_odd_ones

def next_hack(n):
    n += 1
    while not is_hack(n):
        n += 1
    return n
