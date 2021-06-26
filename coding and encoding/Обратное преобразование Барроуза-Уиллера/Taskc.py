n = input()
dict_of_first = {}
a = [[0] * 2 for i in range(len(n))]
for i in range(len(n)):
    if n[i] in dict_of_first:
        dict_of_first[n[i]] += 1
    else:
        dict_of_first[n[i]] = 0
    a[i][0] = n[i]
    a[i][1] = dict_of_first[n[i]]
b = [0] * len(dict_of_first)
n = list(n)
n.sort()
 
dict_of_second = {}
 
count = 0
for i in range(len(n)):
    if n[i] not in dict_of_second:
        dict_of_second[n[i]] = count
        count += 1
    else:
        count += 1
 
ans = ""
sum = 0
for i in range(len(n)):
    ans = a[sum][0] + ans 
    sum = a[sum][1] + dict_of_second[a[sum][0]]
print(ans)
