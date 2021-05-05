N, M = map(int, input().split())
num = 0
for x in range(0, N):
  for y in range (0,M):
    num +=1
    print(num, end=" ")
  print('')