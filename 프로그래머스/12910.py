def solution(arr, divisor):
    answer = []
    arr.sort()
    for value in arr:
        result = divide(value, divisor)
        if result != None : answer.append(result)

    if(len(answer) == 0):
        answer.append(-1)

    return answer


def divide(target, divisor):
    if (target % divisor == 0):
        return target


arr = [5, 9, 7, 10]
divisor = 5

print(solution(arr,divisor))