nums = int(input())
capacity = int(input())
weights = []
for i in range(nums):
  weights.append(int(input()))

dp = [ [0] * (capacity+1) for _ in range(nums+1) ]

dp[0][0] = 0

choice = [[False] * (capacity + 1) for _ in range(nums + 1)]

for i in range(1, nums + 1):
  for j in range(1, capacity+1):
    if j-weights[i-1] < 0:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j-weights[i-1]] + 1, dp[i-1][j])

print(nums-dp[nums][capacity])
