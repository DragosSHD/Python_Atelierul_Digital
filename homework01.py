# Exercise 1
# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

my_first_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("\n\nThe list from the first exercise is: ", my_first_list)

# Exercise 2
# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

my_asc_list = my_first_list[:]
my_asc_list.sort()
print("\nThe list from the second exercise is: ", my_asc_list)

# Exercise 3
# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

my_desc_list = my_first_list[:]
my_desc_list.sort(reverse=True)
print("\nThe list from the third exercise is: ", my_asc_list)

# Exercise 4
# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

my_even_list = my_first_list[1::2]
print("\nThe list from the fourth exercise is: ", my_even_list)

# Exercise 5
# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

my_odd_list = my_first_list[::2]
print("\nThe list from the fifth exercise is: ", my_odd_list)

# Exercise 6
# afișarea elementelor multipli ai lui 3.

my_three_list = [my_first_list[2], my_first_list[4], my_first_list[9]]
print("\nThe list from the fifth exercise is: ", my_three_list)

# Exercise 7
# a se păstra acuratețea indexilor - aceștia trebuie să fie cât mai specifici.

# ???