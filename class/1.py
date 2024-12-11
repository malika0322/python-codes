'''1. Define a Python function student(). Using function attributes display the names of all 
arguments. '''
def student(arg1=None, arg2=None):
    student.args = locals()
    print("Argument names:")
    for arg in student.args.keys():
        print(arg)

student("John", 20)
#output-Argument names:
# arg1
# arg2