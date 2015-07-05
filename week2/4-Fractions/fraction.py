from fractions import gcd

class Fraction:

    def __init__(self, numerator, denominator):
        gd = gcd(numerator, denominator)
        self.numerator = int(numerator/gd)
        self.denominator = int(denominator/gd)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return "{} / {}". format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.numerator/self.denominator == other.numerator/ other.denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)


