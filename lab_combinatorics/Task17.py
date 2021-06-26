file = open("num2brackets.in")
b = file.readline().split(" ")
n = int(b[0]) #  количество пар скобок в последовательности
k = int(b[1]) # номер псп
depth = 0
s = ""
dp = [[0]*(n+2) for _ in range(2*n+1)]
dp[0][0] = 1
for i in range(2*n):
    for j in range(n+1):
        if j+1 <= n:
            dp[i+1][j+1] += dp[i][j]
        if j > 0:
            dp[i+1][j-1] += dp[i][j]
for i in range(2*n ):
    if dp[2 * n - (i + 1)][depth + 1] > k:
        s += '('
        depth += 1
    else:
        k -= dp[2 * n - (i + 1)][depth + 1]
        s += ')'
        depth -= 1
fwrite = open("num2brackets.out", "w")
fwrite.write(s)
