from collections import deque

def solution(numbers):
    # 문자열로 변환
    str_list = list(map(str,numbers))
    str_list.sort(key=lambda x: x*3 ,reverse=True)

    return str(int(''.join(str_list)))

