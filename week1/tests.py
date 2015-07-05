def is_even(n):
    return n % 2 == 0

def is_credit_card_valid(number):
        number = [int(x) for x in str(number)]
        for i in range(len(number)):
            if not is_even(i):
                number[i] = number[i]*2
        if sum(number) % 10 == 0:
            print(sum(number))
            return "valid"
        

print(is_credit_card_valid(79927398713))