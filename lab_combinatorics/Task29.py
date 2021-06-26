def next_slagaemoe(b):
    b[len(b) - 1] -= 1
    b[len(b) - 2] += 1
    if b[len(b) - 2] > b[len(b) - 1]:
        b[len(b) - 2] += b[len(b) - 1]
        b.pop(len(b) - 1)
    else:
        while b[len(b) - 2] * 2 <= b[len(b) - 1]:
            b.append(b[len(b) - 1] - b[len(b) - 2])
            b[len(b) - 2] = b[len(b) - 3]
    return b
 
file = open("nextpartition.in", "r")
a = file.readline().strip()
b = []
slag = False
sum = 0
for i in range(len(a)):
    if a[i] == "=":
        slag = True
        k = i + 1
        break
while k < len(a):
    slovo = ""
    while k < len(a) and a[k] != "+":
        slovo = slovo + a[k]
        k +=1
    b.append(int(slovo))
    sum += int(slovo)
    k += 1
fwrite = open("nextpartition.out", "w")
if len(b) == 1:
    fwrite.write("No solution")
else:
    after = next_slagaemoe(b)
    fwrite.write(str(sum) + "=")
    for i in range(len(after) - 1):
        fwrite.write(str(after[i]) + "+")
    fwrite.write(str(after[-1]))
