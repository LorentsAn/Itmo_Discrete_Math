def kod_gray(b, n):
    for i in range(1, n):
        for k in range(len(b) - 1, -1, -1):
            b.append(b[k])
        for k in range(len(b) // 2):
            b[k] = "0" + b[k]
        for k in range(len(b) // 2, len(b)):
            b[k] = "1" + b[k]
    return b
 
 
 
 
file = open("gray.in")
n = int(file.read())
b = ["0", "1"]
b = kod_gray(b, n)
fwrite = open("gray.out", "w")
for elem in b:
    fwrite.write(elem + "\n")
