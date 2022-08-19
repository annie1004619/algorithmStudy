import math
answer = 0

def solution(numbers, target):
    visited = [0,0]
    graph = [0,0]
    for i in range(1,len(numbers)+1):   
        positive, negative = numbers[i-1], -numbers[i-1]
        graph.extend((positive,negative)*(2**i//2))
        visited.extend((0,0)*(2**i//2))

    dfs(graph,1,visited,0,0,target)
    return answer


def dfs(graph,v,visited,sum,cnt,target):
        global answer
        visited[v] = 1
        sum += graph[v]
        cnt += 1
    
        if cnt == math.ceil(math.log2(len(graph))) and sum == target:
            answer +=1

        if v > len(graph)//2 -1:
            return 

        if not visited[v*2]:
            dfs(graph,v*2,visited,sum,cnt,target) #왼쪽 자식 노드
        if not visited[v*2+1]:
            dfs(graph,v*2+1,visited,sum,cnt,target) #오른쪽 자식 노드

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers,target))