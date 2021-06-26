def bin_vector(args):
    if len(args) == 1:
        return args
    for i in range(len(args) // 2):
        args[i] = args[i] + "0"
 
    for i in range(len(args) // 2, len(args)):
        vector = args[i]
        if len(vector) == 1 and vector[len(vector) - 1] != 1:
            args[i] = args[i] + "1"
        else:
            args.pop(i)
 
    args[0: len(args) // 2] = bin_vector(args[0: len(args) // 2])
    args[len(args) // 2: len(args)] = bin_vector(args[len(args) // 2: len(args)])
 
    return args
 
def next_without_doubl(a):
    global b
    if a[0] == 1:
        return
    if a[-1] == 1:
        a.pop(0)
        a.append(0)
        b.append("".join(map(str,a)))
        next_without_doubl(a)
    elif a[-1] == 0:
        c = a.copy()
        a.pop(0)
        a.append(0)
        b.append("".join(map(str,a)))
        next_without_doubl(a)
        c.pop(0)
        c.append(1)
        b.append("".join(map(str,c)))
        next_without_doubl(c)
 
file = open("vectors.in")
n = int(file.read())
a = [0] * n
a.pop(0)
a.append(1)
b = ["0" * n]
b.append("".join(map(str,a)))
next_without_doubl(a)
b.sort()
fwrite = open("vectors.out", "w")
fwrite.write(str(len(b)) + "\n")
for elem in b:
    fwrite.write(elem + "\n")
