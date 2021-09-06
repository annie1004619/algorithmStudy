n,k = map(int,input().split())
coin = []
dp = [0 for _ in range(k+1)]
for _ in range(n):
    coin.append(int(input()))

for i in range(1,k+1):
    array = []
    for j in coin:
        if j <= i and dp[i-j] != -1 :
            array.append(dp[i-j])
    if not array:
        dp[i] = -1
    else:
        dp[i] = min(array) + 1

print(dp[k])

