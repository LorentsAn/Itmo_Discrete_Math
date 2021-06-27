def check_out(tabl, ind, otv, class_p):
    self_dual, monoton, linear = True, True, True
 
    t0 = True if tabl[0] == 0 else False
    if t0 == False or class_p[0] == 5:
        class_p[0] = t0
 
    t1 = True if tabl[len(tabl) - 1] == 1 else False
    if t1 == False or class_p[1] == 5:
        class_p[1] = t1
 
    polinom(tabl, ind)
    for i in range(1, len(indx)):
        if (i != 0 and i != 1 and i != 2 and i != 4 and i != 8 and i != 16 and i != 32) and indx[i] == 1:
            linear = False
    if linear == False or class_p[2] == 5:
        class_p[2] = linear
 
    for i in range(len(tabl) // 2):
        if tabl[i] == tabl[len(tabl) - i - 1]:
            self_dual = False
    if len(tabl) == 1:
        self_dual = False
    if self_dual == False or class_p[3] == 5:
        class_p[3] = self_dual
 
    mono(tabl, otv)
    if otv1 == False or class_p[4] == 5:
        class_p[4] = otv1
    return class_p
 
 
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
 
 
def mono(a, otv):
    global otv1
    otv1 = otv
    if len(a) == 1 or otv1 == False:
        return otv1
    else:
        for i in range(len(a) // 2):
            if a[i] > a[i + len(a) // 2]:
                otv1 = False
                break
        middle = int(len(a) / 2)
        left = mono(a[:middle], otv1)
        right = mono(a[middle:], otv1)
 
 
n = int(input())
class_post = [5, 5, 5, 5, 5]
#   сох0, сох1, линейна, двойст, монотонна
for i in range(n):
    arg = list(map(str, input().split()))
    value_arg = arg[0]
    array = list(arg[1])
    for i in range(len(array)):
        array[i] = int(array[i])
    index = [array[0]]  # для полинома жигалкина
    otv = True
 
    class_post = check_out(array, index, otv, class_post)
k = True
for i in range(5):
    if class_post[i]:
        k = False
        break
print('yes') if k == True else print('no')
