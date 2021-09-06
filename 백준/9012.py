import sys
n = int(input())

while n > 0:
    n -= 1
    p_string = list(input())
    sum = 0
    while p_string:
        str = p_string.pop()
        if str == ")":
            sum += 1
        if str == "(":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    
    if sum == 0:
        print("YES")
    if sum > 0:
        print("NO")
