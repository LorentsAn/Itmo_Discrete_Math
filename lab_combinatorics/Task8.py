def combination(n, k, arg):
    if arg == []:
        arg = [0] * k
        for i in range(k):
            arg[i] = i + 1
        return arg
    for i in range(k - 1, -1, -1):
        if arg[i] < n - k + i + 1:
            arg[i] += 1
            for j in range(i, k - 1):
                arg[j + 1] = arg[j] + 1
            return arg
    return []
 
 
file = open("choose.in")
b = file.readline().split(" ")
n = int(b[0])
k = int(b[1])
arg = []
arg = combination(n, k, arg)
fwrite = open("choose.out", "w")
while arg:
    for i in range(len(arg)):
        fwrite.write(str(arg[i]))
        fwrite.write(" ")
    fwrite.write("\n")
    arg = combination(n, k, arg)
