def toten(a):
    return int()
def chain(n):
    current = "0" * (n-1) + "1"
    b = ["0" * n, current]
    already = [0] *(2**n)
    while (current[1:] + "0") != "0" * n:
        prefix = current[1:]
        prefix_with_one = prefix + "1"
        prefix_with_zero = prefix + "0"
        if already[int(prefix_with_one, 2)] == 0:
            current = prefix_with_one
            already[int(prefix_with_one, 2)] = 1
        elif already[int(prefix_with_zero, 2)] == 0:
            current = prefix_with_zero
            already[int(prefix_with_zero, 2)] = 1
        else:
            break
        b.append(current)
    return b
 
 
file = open("chaincode.in")
n = int(file.read())
b = chain(n)
fwrite = open("chaincode.out", "w")
for elem in b:
    fwrite.write(elem + "\n")
