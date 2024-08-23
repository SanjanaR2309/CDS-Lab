"""
Description: Program to implement stack
Author: Sanjana R
Date: 22/08/2024
Place: Bangalore
"""
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.stack = []

    def push(self, item):
        # Add the item to the top of the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the top item from the stack
        # (The last item added)
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def __repr__(self):
        # Return a string representation of the stack
        return f"{self.stack}"

# Example usage:
stack = Stack()
a = int(input("Enter the number of elements in the stack: "))
for i in range(a):
    b = int(input("Enter the element to stack: ")) 
    stack.push(b) 

print("The elements in stack are:", stack) 

if stack:
    print("Element popped from stack:", stack.pop())
    print("Element popped from stack:", stack.pop())
else:
    print("Stack is empty")
