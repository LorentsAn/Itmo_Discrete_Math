def polinom(a, ind):
    global indx
    indx = ind
    if len(a) == 1:
        return indx
    new_a = []
    for i in range(len(a) - 1):
        new_a.append((a[i] + a[i + 1]) % 2)
    indx.append(new_a[0])
    polinom(new_a, indx)
 
 
n = int(input())
a = []
znak = []
for i in range(2 ** n):
    b = list(map(str, input().split()))
    znak.append(str(b[0]))
    a.append(int(b[1]))
ind = [a[0]]
polinom(a, ind)
for i in range(2 ** n):
    print(znak[i], end =' ')
    print(ind[i])
