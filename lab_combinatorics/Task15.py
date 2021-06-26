def soch(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0
 
next = 1
file = open("num2choose.in")
b = file.readline().split(" ")
n = int(b[0])
k = int(b[1])
m = int(b[2])
choose = []
while k > 0:
    if m < soch(n - 1, k - 1):
        choose.append(next)
        k -= 1
    else:
        m -= soch(n - 1, k - 1)
    n -= 1
    next += 1
fwrite = open("num2choose.out", "w")
for i in range(len(choose)):
    fwrite.write(str(choose[i]) + " ")
