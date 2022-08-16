def solution(n):
    answer = ''
    str = "수박"
    repeat = n // 2
    if(n%2 == 0):
        answer = str * repeat
    else:
        answer = (str*(repeat+1))[0:n]

    return answer


print(solution(3))