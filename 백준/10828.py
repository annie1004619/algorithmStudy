import sys
n = int(input())

class Stack:
    def __init__(self):
        self.list = []
    def push(self,value):
        self.list.append(value)
    def pop(self):
        if self.empty():
            return -1
        return self.list.pop()
    def size(self):
        return len(self.list)
    def empty(self):
       return 1 if len(self.list) == 0 else 0
    def top(self):
        return self.list[-1] if len(self.list) != 0 else -1

stack = Stack()  

while n > 0:
    n -=1

    input_split = sys.stdin.readline().split()
    op = input_split[0]

    if op == "push":
        stack.push(input_split[1])
    elif op == "pop":
        print(stack.pop())
    elif op == "size":
        print(stack.size())
    elif op == "empty":
        print(stack.empty())
    elif op == "top":
        print(stack.top())

