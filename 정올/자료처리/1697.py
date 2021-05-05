from collections import deque

N = int(input())

class Queue(deque):
  def enqueue(self, x):
    super().append(x)

  def dequeue(self):
    if self.count() == 0:
      return "empty"

    return super().popleft()

  def count(self):
    return len(self)


queue = Queue()

while(N > 0):
    N -= 1
    input_split = input().split()

    op = input_split[0]

    if op == "i":
        queue.enqueue(input_split[1])
    elif op == "o":
        print(queue.dequeue())
    elif op == "c":
        print(queue.count())
    else:
        print("unacceptable op")