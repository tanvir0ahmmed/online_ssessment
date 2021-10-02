a = input()
c = 0
i=0
while(i<len(a)):
    if a[i] == '/':
        c += 1
    elif a[i] != '/' and c > 0:
        c = 0
    if c >= 2:
        a = a[:i] + a[i + 1:]
    else: i+=1
print(a)