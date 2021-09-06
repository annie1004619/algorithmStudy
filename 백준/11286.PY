import heapq

n = int(input())
abs_heap = []

while n >0:
    n -= 1
    x = int(input())
    if (x == 0):
        if (len(abs_heap) == 0):
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])
        continue

    heapq.heappush(abs_heap,(abs(x),x))

