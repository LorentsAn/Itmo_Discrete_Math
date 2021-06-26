def next_psp(s):
    counter_close = 0
    counter_open = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "(":
            counter_open += 1
            if counter_close > counter_open:
                break
        else:
            counter_close += 1
    m = len(s) - counter_close - counter_open
    n = len(s)
    while m != n :
        s.pop()
        m += 1
    if len(s) == 0:
        return None
    else:
        s.append(")")
        for i in range(counter_open):
            s.append("(")
        for i in range(counter_close - 1):
            s.append(")")
        return s
 
 
file = open("nextbrackets.in", "r")
 
b = list(file.readline().strip())
fwrite = open("nextbrackets.out", "w")
after = next_psp(b)
fwrite.write("-") if after is None else fwrite.write("".join(after))
