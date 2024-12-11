'''5. Write a Python class named Student with two attributes: student_id, student_name. Add a 
new attribute: student_class. Create a function to display all attributes and their values in the 
Student class.'''
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        for attr, value in vars(self).items():
            print(f"{attr}: {value}")
     

student = Student(1, "malika")
student.student_class = "10th Grade"
student.display_attributes()

#output
# student_id: 1
# student_name: malika     
# student_class: 10th Grade
