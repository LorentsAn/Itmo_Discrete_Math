def next_perestanovka(a):
    n = len(a)
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            minim = i + 1
            for j in range(i + 1, n):
                if a[j] < a[minim] and a[j] > a[i]:
                    minim = j
            a[i], a[minim] = a[minim], a[i]
            a[i + 1:] = a[:i:-1]
            return a
 
 
def before_perestanovka(a):
    n = len(a)
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            maxim = i + 1
            for j in range(i + 1, n):
                if a[j] > a[maxim] and a[j] < a[i]:
                    maxim = j
            a[i], a[maxim] = a[maxim], a[i]
            a[i + 1:] = a[:i:-1]
            return a
 
 
file = open("nextperm.in", "r")
n = int(file.readline().strip())
perest = [int(item) for item in file.readline().strip().split()]
perest1 = perest.copy()
fwrite = open("nextperm.out", "w")
before = before_perestanovka(perest)
after = next_perestanovka(perest1)
maybe = ["0"] * n
fwrite.write(" ".join(maybe)) if before is None else fwrite.write(" ".join(map(str, before)))
fwrite.write("\n")
fwrite.write(" ".join(maybe)) if after is None else fwrite.write(" ".join(map(str, after)))
