'''3. Write a Python class named Student with two attributes student_name, marks. Modify the 
attribute values of the said class and print the original and modified values of the said 
attributes. '''
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student1 = Student("Alice", 85)
print(f"Original values: Name = {student1.student_name}, Marks = {student1.marks}")
student1.marks = 95
student1.student_name='malika'
print(f"Modified values: Name = {student1.student_name}, Marks = {student1.marks}")

#output:
# Original values: Name = Alice, Marks = 85
# Modified values: Name = malika, Marks = 95