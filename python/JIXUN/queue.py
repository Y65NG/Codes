# Linked List
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.count = 0
        self.start = None
        self.end = None

    def push(self, item):
        added = Node(item)
        if self.start == None: 
            self.start = added
            self.end = added
        else:
            self.end.next = added
            self.end = added
        self.count += 1

    def pop(self):
        result = self.start.value
        self.start = self.start.next
        self.count -= 1
        return result

# Circular Array
class Queue2:
    def __init__(self):
        self.arr = [None] * 5
        self.start = 0
        self.end = 0
    
    def push(self, item):
        self.arr[self.end] = item
        self.end += 1
        if self.end == len(self.arr): self.end = 0

    def pop(self):
        result = self.arr[self.start]
        self.arr[self.start] = None
        self.start += 1
        if self.start == len(self.arr): self.start = 0
        return result

queue2 = Queue2()
queue2.push(1)
queue2.push(2)
print(queue2.pop())
print(queue2.pop())
queue2.push(3)
queue2.push(4)
queue2.push(5)
print(queue2.pop())
print(queue2.pop())
queue2.push(6)

    
    