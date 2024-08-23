from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

# TEST : id should not be initializable and must return an error.
try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print(f"{e}")
