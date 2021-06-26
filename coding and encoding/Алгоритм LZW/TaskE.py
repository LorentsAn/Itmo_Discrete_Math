a = input()
alfabet = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
 
 
count = 27
ans = ''
was = False
word_now = a[0]
for i in range(len(a)):
    if i + 1 == len(a):
        ans = ans + str(alfabet.get(word_now) - 1)
        continue
    if word_now + a[i + 1] in alfabet:
        was = True
        word_now = word_now + a[i + 1]
    else:
        alfabet[word_now + a[i + 1]] = count
        ans = ans + str(alfabet.get(word_now) - 1) + " "
        count += 1
        was = False
        word_now = a[i + 1]
 
print(ans)
