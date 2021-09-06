import sys
k = int(input())
answer = []

for _ in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        answer.append(num)
    if num == 0:
         answer.pop()

print(sum(answer))

