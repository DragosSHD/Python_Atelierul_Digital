from my_math_class import Fraction

my_test_fraction = Fraction(5, 5)
my_other_fraction = Fraction(9, 15)

print('Fraction: ', str(my_test_fraction))
print('Other Fraction: ', str(my_other_fraction))

print('Addition: ', str(my_test_fraction + my_other_fraction))
print('Subtraction: ', str(my_test_fraction - my_other_fraction))

print('Inverse of the first: ', str(my_test_fraction.inverse()))

