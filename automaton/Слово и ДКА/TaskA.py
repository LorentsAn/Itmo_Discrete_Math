f = open("problem1.in")
word = f.readline().strip()
w = list(map(int, f.readline().strip().split(" ")))
n, m, k = w[0], w[1], w[2]
way = [[0] * 2 for i in range(len(word))]
way[0][0] = 1
perehod = [[0] * 26 for i in range(n)]
 
dopusk = list(map(int, f.readline().strip().split(" ")))
 
for i in range(m):
    w = f.readline().split(" ")
    a = int(w[0])
    b = int(w[1])
    c = w[2]
    perehod[a - 1][ord(c[0]) - 97] = b
thereAre = True
old = 1
for i in range(len(word)):
    c = word[i]
    old = perehod[old - 1][ord(c) - 97]
    if old == 0:
        thereAre = False
        break
    way[i][1] = old
    if i + 1 == len(word):
        break
    way[i + 1][0] = old
 
file = open("problem1.out", "w")
thereA = False
for i in range(k):
    if way[len(word) - 1][1] == dopusk[i]:
        thereA = True
if thereA and thereAre:
    file.write("Accepts")
else:
    file.write("Rejects")
f.close()
file.close()
