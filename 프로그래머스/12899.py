
def solution(n):
    answer = ''
    number = ['1','2','4']
    while(n>0):
        if (n%3 != 0):
            answer = number[n%3-1]+answer 
            n = n//3
        else:
            answer = number[-1]+answer
            n = n//3 - 1
        
    return answer

print(solution(14))