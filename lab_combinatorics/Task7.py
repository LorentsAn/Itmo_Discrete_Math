def perm(a, k=0):
    global new
    if k == len(a):
        for j in range(len(a)):
            new.append(a[j])
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k + 1)
            a[k], a[i] = a[i], a[k]
 
 
file = open("permutations.in")
n = int(file.read())
b = []
new = []
arg = []
for i in range(1, n + 1):
    b.append(i)
perm(b)
fwrite = open("permutations.out", "w")
for k in range(0, len(new), n):
   arg.append(new[k:k + n])
arg.sort()
for k in arg:
    for i in range(len(k)):
        fwrite.write(str(k[i]))
        fwrite.write(" ")
    fwrite.write("\n")
