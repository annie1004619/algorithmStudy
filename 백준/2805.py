n,m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    sum = 0 
    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
