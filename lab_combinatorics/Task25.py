def pred_choose(a, n, k):
    a.insert(0, 0)
    for i in range(k, 0, -1):
        if a[i] - a[i - 1] > 1:
            a[i] -= 1
            t = max(a[i] + 1, n - (k - i) + 1)
            for j in range(i + 1, k + 1):
                a[j] = t
                t += 1
            return a[1:]
    return None
 
 
def next_choose(a, n, k):
    b = [0] * (k + 1)
    for i in range(k):
        b[i] = a[i]
    b[k] = n + 1
    i = k - 1
    while i >= 0 and b[i + 1] - b[i] < 2:
        i -= 1
    if i >= 0:
        b[i] += 1
        for j in range(i + 1, k):
            b[j] = b[j - 1] + 1
        for i in range(k):
            a[i] = b[i]
        return a
    else:
        return None
 
file = open("nextchoose.in", "r")
b = file.readline().strip().split()
n = int(b[0])
k = int(b[1])
choose = [int(item) for item in file.readline().strip().split()]
fwrite = open("nextchoose.out", "w")
after = next_choose(choose, n, k)
fwrite.write("-1") if after is None else fwrite.write(" ".join(map(str, after)))
