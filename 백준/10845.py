import sys
from collections import deque

n = int(sys.stdin.readline())

class Queue:
    def __init__(self):
        self.queue = deque()
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        return -1 if self.empty() else self.queue.popleft()
    def size(self):
        return len(self.queue)
    def empty(self):
        return 1 if len(self.queue) == 0 else 0
    def front(self):
        return -1 if len(self.queue) == 0 else self.queue[0]
    def back(self):
        return -1 if len(self.queue) == 0 else self.queue[-1]

queue = Queue()

while n > 0:
    n -= 1
    input_split = sys.stdin.readline().split()
    op = input_split[0]

    if op == "push":
        queue.push(input_split[1])
    elif op == "pop":
        print(queue.pop())
    elif op == "size":
        print(queue.size())
    elif op == "empty":
        print(queue.empty())
    elif op == "front":
        print(queue.front())
    elif op == "back":
        print(queue.back())
