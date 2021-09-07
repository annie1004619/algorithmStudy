n = int(input())
money = list(map(int, input().split()))
total = int(input())
limit = 0

start = 0
end = max(money)

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for x in money:
        if x > mid:
            sum += mid
        else:
            sum += x
    if sum > total:
        end = mid -1
    else:
        limit = mid
        start = mid + 1

print(limit)

