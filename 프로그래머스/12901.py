def solution(a, b):
    answer = ''
    numberOfDays = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]

    answer = week[(sum(numberOfDays[:a])+b)%7]
    return answer


print(solution(1,1))