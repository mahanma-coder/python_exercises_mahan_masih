students = {
    'Ali': [18, 17, 20],
    'Sara': [15, 19, 18],
    'Reza': [12, 14, 10],
    'Mina': [20, 20, 19]
}
averages = {}
for name in students:
    grades = students[name]
    total = 0
    for grade in grades:
        total = total + grade
    average = total / len(grades)
    highest_grade = grades[0]
    for grade in grades:
        if grade > highest_grade:
            highest_grade = grade
    if average >= 15:
        status = 'Passed'
    else:
        status = 'Failed'
    averages[name] = average
    print(name)
    print('Average:', average)
    print('Status:', status)
    print('Highest:', highest_grade)
    print()
best_student = ''
highest_average = 0
for name in averages:
    average = averages[name]
    if average > highest_average:
        highest_average = average
        best_student = name
print('Best student:', best_student)
print('Highest average:', highest_average)