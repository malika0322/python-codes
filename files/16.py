# 16. Demonstrate Renaming, Moving, Copying, and Removing operations of Files in python with 
# or without shutil package.
import os
import shutil

# Rename
os.rename("test1.txt", "test2.txt")
print("Renamed test1.txt to test2.txt")

# Move
shutil.move("test2.txt", "folder/")
print("Moved test2.txt to folder/")

# Copy
shutil.copy("folder/test2.txt", "copy_test2.txt")
print("Copied test2.txt to copy_test2.txt")

# Remove
os.remove("copy_test2.txt")
print("Removed copy_test2.txt")

#output:
'''Renamed test1.txt to test2.txt
Moved test2.txt to folder/        
Copied test2.txt to copy_test2.txt
Removed copy_test2.txt'''
