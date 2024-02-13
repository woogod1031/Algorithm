N = int(input())  # (1 ≤ N ≤ 2,000)
li = list(map(int, input().split()))  # <= 10,000,000
li.reverse()
# 4 2 5 8 4 11 15
dp = [1] * N
# [1,1,2,3,3,4,5]

#  4 2 3,4,5,8,2,4 6 8 9 11 15
# [1,1,2,2,3,4,5,6,7

for i in range(0, N):  # 0부터 N전까지
    for j in range(0, i):  # 0부터 i전까지
        if li[i] > li[j]:  # 조건에 같으면 안 되고 무조건 커야된다고 함
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
# 첫째 줄에 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수를 출력한다.
# 오름차순

# 2 3 4 1 2 3 5
# 1 2 3 1 2 3 4
