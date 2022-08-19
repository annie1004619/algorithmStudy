from collections import deque
import copy
import math

def solution(progresses, speeds):
    answer = []

    p_queue = deque(progresses)
    s_queue = deque(speeds)

    while p_queue:
        day = math.ceil((100-p_queue[0])/s_queue[0])
        count = 0

        # 작업 업데이트 
        for i in range(len(p_queue)):
            p_queue[i] += (s_queue[i]*day)
        
        copy_queue = copy.deepcopy(p_queue)

        for i in range(len(copy_queue)):
            if copy_queue[i] >= 100:
                p_queue.popleft()
                s_queue.popleft()
                count += 1
            else: 
                break

        if count > 0:
            answer.append(count)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses,speeds))