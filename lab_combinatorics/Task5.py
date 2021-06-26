def kod_grey_for_k(b, n, k):
    global reverse
    m = 0
    if len(b[0]) == 0 or reverse[n - len(b[0]) - 1] == False:
        for i in range(k):
            for j in range(len(b) // k):
                b[m] = str(i) + b[m]
                m += 1
        reverse[n - len(b[0])] = True
    else:
        for i in range(k - 1, -1, -1):
            for j in range(len(b) // k):
                b[m] = str(i) + b[m]
                m += 1
        reverse[n - len(b[0])] = False
 
    for i in range(k):
        if len(b[i * (len(b) // k): (i + 1) * (len(b) // k)]) > 1:
            b[i * (len(b) // k): (i + 1) * (len(b) // k)] = kod_grey_for_k(
                b[i * (len(b) // k): (i + 1) * (len(b) // k)], n, k)
        else:
            return b
    return b
 
 
 
 
file = open("telemetry.in")
argument = list(file.readline().split())
n = int(argument[0]) # len of vector
k = int(argument[1]) #  к ичный вектор
b = [""] * (k ** n)
reverse = [False] * n
b = kod_grey_for_k(b, n, k)
fwrite = open("telemetry.out", "w")
for elem in b:
    fwrite.write(elem + "\n")
