def solution(s):
    answer = True
    if(len(s)!=4 and len(s) != 6):
        return False

    try:
        for value in s:
            int(value)
    except:
        answer = False
    return answer


s = "1234"

print(solution(s))

