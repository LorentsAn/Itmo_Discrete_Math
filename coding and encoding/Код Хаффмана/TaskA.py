import sys
 
 
def huffman_cod(a, n):
    b = [1000000001] * n
    ans = 0
    i, j = 0, 0
    for k in range(n - 1):
        if i + 1 <= n - 1 and j + 1 <= n - 1:
            if a[i] + a[i + 1] <= a[i] + b[j] and a[i] + a[i + 1] <= b[j] + b[j + 1]:
                b[k] = a[i] + a[i + 1]
                ans += b[k]
                i += 2
                continue
            if a[i] + b[j] <= a[i] + a[i + 1] and a[i] + b[j] <= b[j] + b[j + 1]:
                b[k] = a[i] + b[j]
                ans += b[k]
                i += 1
                j += 1
                continue
            if b[j] + b[j + 1] <= a[i] + a[i + 1] and b[j] + b[j + 1] <= a[i] + b[j]:
                b[k] = b[j] + b[j + 1]
                ans += b[k]
                j += 2
        elif i + 1 <= n - 1 and j >= n:
            if a[i] + a[i + 1] <= a[i] + b[j]:
                b[k] = a[i] + a[i + 1]
                ans += b[k]
                i += 2
                continue
            if a[i] + b[j] <= a[i] + a[i + 1]:
                b[k] = a[i] + b[j]
                ans += b[k]
                i += 1
                j += 1
                continue
        elif j + 1 <= n - 1 and i <= n - 1:
            if a[i] + b[j] <= b[j] + b[j + 1]:
                b[k] = a[i] + b[j]
                ans += b[k]
                i += 1
                j += 1
                continue
            if b[j] + b[j + 1] <= a[i] + b[j]:
                b[k] = b[j] + b[j + 1]
                ans += b[k]
                j += 2
        elif j + 1 <= n - 1 < i:
            b[k] = b[j] + b[j + 1]
            ans += b[k]
            j += 2
 
    return ans
 
 
n = int(input())
a = [0] * n
c = sys.stdin.readline().split()
for i in range(n):
    a[i] = int(c[i])
a.sort()
print(huffman_cod(a, n))
