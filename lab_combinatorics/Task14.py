import math
 
file = open("perm2num.in")
num_of_object = 0
n = int(file.readline())
peresytanovka = file.readline().split(" ")
value_less = [0] * n
for i in range(n):
    number = int(peresytanovka[i])
    for j in range(i + 1, n):
        if number > int(peresytanovka[j]):
            value_less[i] += 1
for i in range(1, n + 1):
    num_of_object += value_less[i - 1] * math.factorial(n - i)
 
fwrite = open("perm2num.out", "w")
fwrite.write(str(num_of_object))
