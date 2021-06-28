# What we've done during the fourth python course.

# Memory Savers
# - lambda functions: used inline so we won't occupy memory with a function that we have to use only once

my_sum = (lambda param1, param2: param1 + param2)(5, 7)
print('my_sum', my_sum)

# use case example:

students = [{
    'name': 'Student 1',
    'grade': 7.85,
}, {
    'name': 'Student 2',
    'grade': 6.75,
}, {
    'name': 'Student 3',
    'grade': 10,
}, {
    'name': 'Student 4',
    'grade': 8.44,
}]

students.sort(key=kambda student_item: student_item['grade'] if