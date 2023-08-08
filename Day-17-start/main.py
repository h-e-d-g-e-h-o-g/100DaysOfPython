# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Student:
    def __init__(self, student_id, roll_no, phone_no):
        self.id = student_id
        self.rollNo = roll_no
        self.phonNo = phone_no


s1 = Student("3", "41221025", "8860317648")
print(s1.id)
print(s1.rollNo)
print(s1.phonNo)
