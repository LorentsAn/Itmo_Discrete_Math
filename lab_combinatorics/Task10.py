file = open("partition.in")
b = file.readline().split(" ")
n = int(b[0])
fwrite = open("partition.out", "w")
a = []
for i in range(n):
    a.append(1)
arg = []
 
while True:
    slovo = []
    for i in range(len(a)):
        slovo.append(a[i])
    arg.append(slovo)
    if a[-1] == n:
        break
    last = a[-1]
    minim = len(a) - 1
    i = len(a) - 1
    while i != 0:
        if a[i] < last:
            last = a[i]
            minim = i
        i -= 1
    a[minim] += 1
    a[0] -= 1
    a = a[minim:]
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    for i in range(n - sum):
        a.insert(i, 1)
 
 
arg.sort()
for i in range(len(arg)):
    slovo = arg[i]
    for j in range(len(slovo)):
        fwrite.write(str(slovo[j]))
        if j != len(slovo) - 1:
            fwrite.write("+")
    fwrite.write("\n")
