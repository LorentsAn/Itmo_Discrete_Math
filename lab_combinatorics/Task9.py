def psp(n, count_open, count_close, arg):
    if count_open + count_close == 2 * n:
        fwrite.write(arg)
        fwrite.write("\n")
        return
    if count_open < n:
        psp(n, count_open + 1, count_close, arg + "(")
    if count_open > count_close:
        psp(n, count_open, count_close + 1, arg + ")")
 
file = open("brackets.in")
b = file.readline().split(" ")
n = int(b[0])
fwrite = open("brackets.out", "w")
psp(n, 0, 0, "")
