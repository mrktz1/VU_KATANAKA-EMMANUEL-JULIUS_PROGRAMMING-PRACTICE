
# 1. CONTROL FLOW AND FUNCTIONS

# CONDITIONAL STATEMENTS: if, elif, else
print("\n1.1 CONDITIONAL STATEMENTS")

mark = 72

if mark >= 80:
    grade = "A"
elif mark >= 70:
    grade = "B"
elif mark >= 60:
    grade = "C"
elif mark >= 50:
    grade = "D"
else:
    grade = "F"

print("Mark:", mark)
print("Grade:", grade)

# Nested condition
attendance = 85

if mark >= 50:
    if attendance >= 75:
        print("Student passes and has acceptable attendance.")
    else:
        print("Student passes, but attendance needs attention.")
else:
    print("Student needs academic support.")


#  LOOPS: for, while and iteration
print("\n1.2 LOOPS")

marks = [65, 72, 81, 58, 90]

for m in marks:
    print("Mark:", m)

count = 1
while count <= 5:
    print("While iteration:", count)
    count += 1

for number in range(1, 10):
    if number == 5:
        break
    print("break example:", number)

for number in range(1, 6):
    if number == 3:
        continue
    print("continue example:", number)


#  FUNCTIONS AND MODULAR PROGRAMMING
print("\n1.3 FUNCTIONS AND MODULAR PROGRAMMING")


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def classify_mark(mark):
    if mark >= 70:
        return "Distinction"
    elif mark >= 50:
        return "Pass"
    return "Fail"


student_marks = [65, 72, 81, 58, 90]
average = calculate_average(student_marks)

print("Average:", average)
print("Classification:", classify_mark(average))


# RECURSION
print("\n1.4 RECURSION")


def factorial(n):
    if n == 0:              # base case
        return 1
    return n * factorial(n - 1)


print("5! =", factorial(5))


#  LAMBDA FUNCTIONS
print("\n1.5 LAMBDA FUNCTIONS")


def square(x): return x * x


print("Square of 6:", square(6))

students = [("Amina", 65), ("Brian", 85), ("John", 72)]
students_sorted = sorted(
    students, key=lambda student: student[1], reverse=True
)
print("Students sorted by mark:", students_sorted)


# 2. DATA STRUCTURES AND FILE HANDLING

#  LISTS, TUPLES, SETS AND DICTIONARIES
print("\n2.1 DATA STRUCTURES")

# List: ordered and changeable
marks = [65, 72, 81, 58]
marks.append(90)
print("List:", marks)
print("First mark:", marks[0])

# Tuple: ordered collection that is normally not changed
student = ("Emmanuel", "Data Science and AI", 1)
print("Tuple:", student)

# Set: unique values
course_units = {"Python", "Statistics", "Python", "Mathematics"}
print("Set:", course_units)

# Dictionary: key-value pairs
student_record = {
    "name": "Emmanuel",
    "programme": "Data Science and AI",
    "year": 1,
    "average": 72
}
print("Dictionary:", student_record)
print("Student name:", student_record["name"])


# FILE INPUT AND OUTPUT
print("\n2.2 FILE INPUT AND OUTPUT")

file_name = "student_marks.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python: 72\n")
    file.write("Statistics: 68\n")
    file.write("Mathematics: 75\n")

with open(file_name, "r", encoding="utf-8") as file:
    data = file.read()

print("Contents of file:")
print(data)

# Common modes:
# r = read
# w = write
# a = append
# x = create a new file


# EXCEPTION HANDLING
print("\n2.3 EXCEPTION HANDLING")

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("This block runs whether an exception occurs or not.")

try:
    age = int("twenty")
except ValueError:
    print("Error: the value is not a valid integer.")


# 3. OBJECT-ORIENTED PROGRAMMING

# CLASSES AND OBJECTS
print("\n3.1 CLASSES AND OBJECTS")


class Student:
    def __init__(self, name, programme, mark):
        self.name = name
        self.programme = programme
        self.mark = mark

    def result(self):
        if self.mark >= 50:
            return "Pass"
        return "Fail"


student1 = Student("Amina", "Data Science and AI", 78)

print("Name:", student1.name)
print("Programme:", student1.programme)
print("Mark:", student1.mark)
print("Result:", student1.result())


# INHERITANCE
print("\n3.2 INHERITANCE")


class DataScienceStudent(Student):
    def data_project(self):
        return "Build a small data analysis project."


student2 = DataScienceStudent("Brian", "Data Science and AI", 82)

print(student2.name)
print(student2.result())
print(student2.data_project())


#  ENCAPSULATION
print("\n3.3 ENCAPSULATION")


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance


account = BankAccount(100000)
account.deposit(25000)

print("Balance:", account.get_balance())


# POLYMORPHISM
print("\n3.4 POLYMORPHISM")


class Model:
    def predict(self):
        return "General prediction"


class ClassificationModel(Model):
    def predict(self):
        return "Predicting a class label"


class RegressionModel(Model):
    def predict(self):
        return "Predicting a numerical value"


models = [ClassificationModel(), RegressionModel()]

for model in models:
    print(model.predict())

# MINI INTEGRATED DATA SCIENCE EXAMPLE

print("\nMINI INTEGRATED DATA SCIENCE EXAMPLE")

records = [
    {"name": "Amina", "python": 78, "statistics": 72},
    {"name": "Brian", "python": 64, "statistics": 69},
    {"name": "John", "python": 45, "statistics": 51},
]


def average_record(record):
    return (record["python"] + record["statistics"]) / 2


for record in records:
    average = average_record(record)

    if average >= 70:
        category = "Excellent"
    elif average >= 50:
        category = "Pass"
    else:
        category = "Needs support"

    print(record["name"], "Average:", average, "Category:", category)
