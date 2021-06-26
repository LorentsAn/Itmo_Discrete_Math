import math
 
import math
def perestanov(n, k):
    global perestanovka
    global was
    for i in range(1, n + 1):
        already = k // math.factorial(n - i)
        k %= math.factorial(n - i)
        cur_free = 0
        for j in range(1, n + 1):
            if not was[j]:
                cur_free += 1
                if cur_free == already + 1:
                    perestanovka[i] = j
                    was[j] = True
    return perestanovka
 
 
 
 
file = open("num2perm.in")
b = file.readline().split(" ")
n = int(b[0])  # размерность
k = int(b[1])  # сочетания от 1 до k
was = [False] * (n + 1)
perestanovka = [0] * (n + 1)
perestanov(n, k)
perestanovka.pop(0)
fwrite = open("num2perm.out", "w")
