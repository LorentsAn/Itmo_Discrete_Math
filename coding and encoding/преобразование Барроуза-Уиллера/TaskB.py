n = input()
a = [''] * len(n)
a[0] = n
for i in range(1, len(n)):
    a[i] = n[1:] + n[0]
    n = n[1:] + n[0]
a.sort()
ans = ''
for i in range(len(n)):
    b = a[i]
    ans = ans + b[-1]
print(ans)
