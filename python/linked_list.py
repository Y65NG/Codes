class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        self.start = None
        self.end = None
        self.count = 0

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

queue1 = Node(1)
queue1.push(2)
queue1.push(3)
print(queue1.pop())
print(queue1.pop())