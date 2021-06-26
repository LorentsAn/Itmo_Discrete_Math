def bin_vector(args):
    if len(args) == 1:
        return args
    for i in range(len(args) // 2):
        args[i] = args[i] + "0"
 
    for i in range(len(args) // 2, len(args)):
        args[i] = args[i] + "1"
 
    args[0: len(args) // 2] = bin_vector(args[0: len(args) // 2])
    args[len(args) // 2: len(args)] = bin_vector(args[len(args) // 2: len(args)])
 
    return args
 
 
file = open("allvectors.in")
n = int(file.read())
b = [""] * (2 ** n)
b = bin_vector(b)
fwrite = open("allvectors.out", "w")
for elem in b:
    fwrite.write(elem + "\n")
