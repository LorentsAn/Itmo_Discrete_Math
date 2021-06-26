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
 
num_of_choose = 0
file = open("choose2num.in")
b = file.readline().split(" ")
n, k = int(b[0]), int(b[1])
choose = list(map(int, file.readline().split(" ")))
choose.insert(0, 0)
for i in range(1, k + 1):
    for j in range(choose[i - 1] + 1, choose[i]):
        num_of_choose += soch(n - j, k - i)
fwrite = open("choose2num.out", "w")
fwrite.write(str(num_of_choose))
