file = open("subsets.in")
b = file.readline().split(" ")
n = int(b[0])
arg = [[] for i in range(2 ** n)]
m = 0
for mask in range(1 << n):
    for q in range(n):
        if mask & (1 << q):
            arg[m].append(q + 1)
    m += 1
arg.sort()
fwrite = open("subsets.out", "w")
for i in range(2 ** n):
    elem = arg[i]
    for j in range(len(elem)):
        if len(elem) == 0:
            fwrite.write(" ")
        fwrite.write(str(elem[j]) + " ")
    fwrite.write("\n")
