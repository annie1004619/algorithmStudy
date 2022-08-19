def solution(numbers,target):
    answer = 0
    stack = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)

    while stack:
        sum, idx = stack.pop()
        idx += 1
        if idx < n:
            stack.append([sum+numbers[idx],idx])
            stack.append([sum-numbers[idx],idx])
        else:
            if sum == target:
                answer += 1
    return answer