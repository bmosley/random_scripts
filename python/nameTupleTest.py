from collections import namedtuple

Student = namedtuple("Student", "first last grade")

y = Student("bryan", "josh", "peter")

print(y.first)

print(y.grade)