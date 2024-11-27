#12.  Write a Python function that takes a date in string format DD/MM/YYYY and checks if it is a valid 
#date and in the correct format.
from datetime import datetime
def validate_date():
    date_str = input("Enter a date in DD/MM/YYYY format: ")
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        print("The date is valid.")
    except ValueError:
        print("The date is invalid.")

validate_date()
    

