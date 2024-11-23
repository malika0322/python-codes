'''12. Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* '''
   rows = 5

# Upper part of the pattern
for i in range(1, rows + 1):
    print('* ' * i)

# Lower part of the pattern
for i in range(rows - 1, 0, -1):
    print('* ' * i)
