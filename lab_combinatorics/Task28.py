def multy_perest(b):
    n = len(b)
    i = n - 2
    while i >= 0 and b[i] >= b[i + 1]:
        i -= 1
    if i >= 0:
        j = i + 1
        while j < n - 1 and b[j + 1] > b[i]:
            j += 1
        b[i], b[j] = b[j], b[i]
        b[i + 1:] = b[:i:-1]
        return b
    else:
        return None
 
 
 
file = open("nextmultiperm.in", "r")
n = int(file.readline().strip())
multy = [int(item) for item in file.readline().strip().split()]
fwrite = open("nextmultiperm.out", "w")
after = multy_perest(multy)
maybe = ["0"] * n
fwrite.write(" ".join(maybe)) if after is None else fwrite.write(" ".join(map(str, after)))
