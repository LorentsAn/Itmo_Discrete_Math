def ternary_vector(args):
    if len(args) == 1:
        return args
    for i in range(len(args) // 3):
        args[i] = args[i] + "0"
    for i in range(len(args) // 3, 2 * len(args) // 3):
        args[i] = args[i] + "1"
    for i in range(2 * len(args) // 3, len(args)):
        args[i] = args[i] + "2"
    args[0: len(args) // 3] = ternary_vector(args[0: len(args) // 3])
    args[len(args) // 3: 2* len(args) // 3] = ternary_vector(args[len(args) // 3: 2* len(args) // 3])
    args[2 * len(args) // 3: len(args)] = ternary_vector(args[2 * len(args) // 3: len(args)])
    return args
 
file = open("antigray.in")
n = int(file.read())
b = []
 
first = ["0"] * (3 ** (n -1))
first = ternary_vector(first)
 
for i in range(len(first)):
    b.append(first[i])
    m = first[i]
    n = ""
    for j in range(len(m)):
        n = n + str((int(m[j]) + 1) % 3)
    b.append(n)
    k = ""
    for j in range(len(m)):
        k = k + str((int(n[j]) + 1) % 3)
    b.append(k)
 
fwrite = open("antigray.out", "w")
for elem in b:
    fwrite.write(elem + "\n")
