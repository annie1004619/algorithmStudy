N = int(input())

class Stack:
    def __init__(self):
        self.len = 0
        self.list = []

    def i(self, num):
        self.list.append(num)
        self.len += 1

    def o(self):
        if self.c() == 0:
            return "empty"
        pop_result = self.list[self.len - 1]
        del self.list[self.len - 1]
        self.len -= 1
        return pop_result

    def c(self):
        return self.len




stack = Stack()
while(N > 0):
    N -= 1
    input_split = input().split()

    op = input_split[0]

    if op == "i":
        stack.i(input_split[1])
    elif op == "o":
        print(stack.o())
    elif op == "c":
        print(stack.c())
    else:
        print("unacceptable op")