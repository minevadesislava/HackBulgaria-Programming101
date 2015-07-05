
class Bill:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError

        if not isinstance(amount, int):
            raise TypeError
        
        self.__amount = amount

    def __int__(self):
        return self.__amount

    def __str__(self):
        return "A {}$ bill.".format(self.__amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return int(self) == int(other)

    def __hash__(self):
        return hash(self.__str__())


class BillBatch():
    def __init__(self, bills):
        self.__bills = bills

    def __len__(self):
        return len(self.__bills)

    def __getitem__(self, index):
        return self.__bills[index]

    def total(self):
        total_sum = 0
        for bill in self.bills:
            total_sum +=  int(bill)
        return total_sum


class CashDesk():
    def __init__(self):
        self.money_holder = {}

    def __store_money(self, bill):
        if bill not in self.money_holder:
            self.money_holder[bill] = 1
        else:
            self.money_holder[bill] +=1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.__store_money(money)
        elif isinstance(money, BillBatch):
            for bill in money:
                self.__store_money(bill)

    def total(self):
        result = 0
        for bill in self.money_holder:
            result += int(bill) * self.money_holder[bill]
        return "We have a total amount of "  + str(result) + "$ in the desk."

    def inspect(self):
        sorted_bills = sorted(self.money_holder)
        print("We have the following count of bills,\
 sorted in ascending order:")
        for bill in sorted_bills:
            print("{} - {}".format(repr(bill), self.money_holder[bill]))