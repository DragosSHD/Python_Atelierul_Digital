
class Fraction:

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Only integers are allowed")
        self.numerator = numerator
        self.__denominator = denominator
        self.__simplify_fraction()

    def __highest_divider(self, first_nr, second_no):
        return first_nr if second_no == 0 else self.__highest_divider(second_no, first_nr % second_no)

    def __simplify_fraction(self):
        hdiv = self.__highest_divider(self.numerator, self.__denominator)
        self.numerator //= hdiv
        self.__denominator //= hdiv


    def __str__(self):
        return str(self.numerator) + '/' + str(self.__denominator)

    def __add__(self, other):
        if self.__denominator == other.__denominator:
            new_numerator = self.numerator + other.numerator
            return Fraction(new_numerator, self.__denominator)
        else:
            new_numerator = self.numerator * other.__denominator + other.numerator * self.__denominator
            new_denominator = self.__denominator * other.__denominator
            return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if self.__denominator == other.__denominator:
            new_numerator = self.numerator - other.numerator
            return Fraction(new_numerator, self.__denominator)
        else:
            new_numerator = self.numerator * other.__denominator - other.numerator * self.__denominator
            new_denominator = self.__denominator * other.__denominator
            return Fraction(new_numerator, new_denominator)

    def inverse(self):
        return Fraction(self.__denominator, self.numerator)
