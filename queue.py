"""
Description: Program to implement queue
Author: Sanjana R
Date: 22/08/2024
Place: Bangalore
"""

class Queue:
    def __init__(self):
        # Initialize an empty list to store queue items
        self.queue = []

    def enqueue(self, item):
        # Add the item to the back of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the front item from the queue
        # (The first item added)
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def __repr__(self):
        # Return a string representation of the queue
        return f"{self.queue}"

# Example usage:
queue = Queue()
a = int(input("Enter the number of elements in the queue: "))
for i in range(a):
    b = int(input('Enter the element to the queue: '))
    queue.enqueue(b)

print("The queue elements are:", queue)

if queue:
    print("Element popped is", queue.dequeue()) 
    print("Element popped is", queue.dequeue())  
else:
    print("Queue is empty")
