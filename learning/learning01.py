from learning.learning01_student import StudentOne


def student_factory(name):
    student_one = StudentOne(name)
    student_one.say_hello()
