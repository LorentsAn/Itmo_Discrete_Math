file = open("brackets2num.in")
s = file.readline()
n = len(s) // 2
 
d = [[0] * (n + 2) for _ in range(2 * n + 1)]
d[0][0] = 1
for i in range(2*n):
    for j in range(n+1):
        if j+1 <= n:
            d[i + 1][j + 1] += d[i][j]
        if j > 0:
            d[i + 1][j - 1] += d[i][j]
k = 0
lenth = 0
for i in range(2*n):
    if s[i] == '(':
        lenth += 1
    else:
        k += d[2 * n - (i + 1)][lenth + 1]
        lenth -= 1
fwrite = open("brackets2num.out", "w")
fwrite.write(str(k))
