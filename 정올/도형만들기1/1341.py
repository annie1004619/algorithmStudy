N, M = map(int, input().split())

if(N < M):
  for x in range(N, M+1):
    for y in range(1, 10):
        print(x ,'*' , y , "=" ,str(x*y).rjust(2) ,end="   ")
        if(y%3 == 0):
            print(" ")
    print(" ")

if(N > M):
  for x in range(N, M-1, -1):
    for y in range(1, 10):
        print(x ,'*' , y , "=" ,str(x*y).rjust(2),end="   ")
        if(y%3 == 0):
            print("")
    print(" ")