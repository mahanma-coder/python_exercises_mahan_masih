employees = {
    'E01': {
        'name': 'Ali',
        'age': 28,
        'salary': 3000
    },
    'E02': {
        'name': 'Sara',
        'age': 32,
        'salary': 4500
    },
    'E03': {
        'name': 'Reza',
        'age': 25,
        'salary': 2800
    }
}
highest_employee = 'E01'
lowest_employee = 'E01'
highest_salary = employees['E01']['salary']
lowest_salary = employees['E01']['salary']
total_salary = 0
for code in employees:
    employee = employees[code]
    salary = employee['salary']
    if salary > highest_salary:
        highest_salary = salary
        highest_employee = code
    if salary < lowest_salary:
        lowest_salary = salary
        lowest_employee = code
    total_salary = total_salary + salary
average_salary = total_salary / len(employees)
print('Highest salary:')
print(employees[highest_employee]['name'])
print(highest_salary)
print('Average salary:')
print(average_salary)
print('Employees with salary more than 3000:')
for code in employees:
    employee = employees[code]
    if employee['salary'] > 3000:
        print(employee['name'], employee['salary'])
print('Lowest salary employee:')
print(employees[lowest_employee]['name'])