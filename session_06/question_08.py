users = [
    ('Ali', 25, 'Python'),
    ('Sara', 30, 'Java'),
    ('Reza', 22, 'Python'),
    ('Mina', 28, 'C++'),
    ('John', 35, 'Python'),
    ('David', 30, 'Java')
]
groups = {}
for user in users:
    name = user[0]
    age = user[1]
    language = user[2]
    if language in groups:
        groups[language].append((name, age))
    else:
        groups[language] = [(name, age)]
print('Groups:')
print(groups)
print()
for language in groups:
    people = groups[language]
    total_age = 0
    for person in people:
        total_age = total_age + person[1]
    average_age = total_age / len(people)
    oldest_name = people[0][0]
    oldest_age = people[0][1]
    for person in people:
        name = person[0]
        age = person[1]
        if age > oldest_age:
            oldest_age = age
            oldest_name = name
    print(language)
    print('Average age:', average_age)
    print('Oldest user:', oldest_name)
    print('Oldest age:', oldest_age)
    print()
most_users_language = ''
most_users = 0
for language in groups:
    people = groups[language]
    if len(people) > most_users:
        most_users = len(people)
        most_users_language = language
print('Language with most users:', most_users_language)
languages = set()
for user in users:
    language = user[2]
    languages.add(language)
print('All languages:', languages)