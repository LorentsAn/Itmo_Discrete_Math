def before_vector(a):
    n = len(a) - 1
    while n >= 0 and a[n] != "1":
        a[n] = "1"
        n -= 1
    if n == -1:
        return "-"
    a[n] = "0"
    return "".join(a)
 
 
def next_vector(b):
    n = len(b) - 1
    while n >= 0 and b[n] != "0":
        b[n] = "0"
        n -= 1
    if n == -1:
        return "-"
    b[n] = "1"
    return "".join(b)
 
file = open("nextvector.in", "r")
vector = file.readline().strip()
fwrite = open("nextvector.out", "w")
 
fwrite.write(before_vector(list(vector)))
fwrite.write('\n')
fwrite.write(next_vector(list(vector)))
 
fwrite.close()
