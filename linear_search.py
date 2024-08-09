"""
    description : program to search elemnt using Linear Search algorithm
    Author: Sanjana R
    place:Bengaluru
    Date: 10/08/2024
"""

# Defining the function for  searching element using Linear search:

def linear_search(list_1, target):
    """
        Searches for the value stored in the variable target,
        in the list provided as list1.
        1. list_1 : Element to be searched
        2.Target: element to be searched in list 
    """
    #initializing the find condition
    flag=0
    for i in range(len(list_1)):
        # Checking if the element to be searched is present at the current index.
        if list_1[i] == target:
            flag=1
    # printing the out information about the element
    if flag==1:
        print("the element is in",i+1,"th place")
    else:
        print("the elements is not found")

# Defining the function to handle few edge cases.

def input_1(prompt):
    """
        To get valid input (Edge case handling)
        1. prompt : The message to be displayed to the user.
        2. ValueError is an exception that occurs when a function 
           receives an argument of the correct type but an inappropriate value.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid Datatype, Enter an integer.")

# Get valid input for the number of elements in the list.
x = input_1("Enter the number of elements in the list: ")

# Number of elements cannot be negative.
if x < 0:
    print("Number of elements cannot be negative.")
else:
    list_1 = []
    for i in range(1, x+1):
        # Get valid input for the elements in the list.
        y = input_1(f"Enter the elements {i}: ")
        list_1.append(y)
        # Get valid input for target value.
    target = input_1("Enter the target value : ")
    # Perform linear search on the list
    result = linear_search(list_1, target)

    