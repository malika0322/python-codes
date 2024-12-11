'''4. Write a Python class named Student with two attributes student_id, student_name. Add a 
new attribute student_class and display the entire attribute and the values of the class. Now 
remove the student_name attribute and display the entire attribute with values.'''
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student = Student(1, "malika")
student.student_class = "10th Grade"
print("Attributes with values:", vars(student))

del student.student_name
print("Attributes after removal:", vars(student))

#output
# Attributes with values: {'student_id': 1, 'student_name': 'malika', 'student_class': '10th Grade'}
# Attributes after removal: {'student_id': 1, 'student_class': '10th Grade'}