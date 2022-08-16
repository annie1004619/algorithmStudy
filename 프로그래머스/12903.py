def solution(s):
    answer = ''
    length = len(s)
    quotient = length // 2

    if (length%2 == 0):
        answer = s[quotient-1:quotient+1]
    else:
        answer = s[quotient]

    return answer




s = "qwer"

print(solution(s))