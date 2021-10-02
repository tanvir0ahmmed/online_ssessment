a = input()
b = input()

len_a = len(a)
len_b = len(b)
max_l = max(len_a, len_b)
res = ""
c = 0

for i in range(max_l):

    if i < len_b and i < len_a:
        t_sum = int(a[len_a-(i+1)]) + int(b[len_b-(i+1)]) + c
    elif i < len_b and i >= len_a:
        t_sum = int(b[len_b-(i+1)]) + c
    else:
        t_sum = int(a[len_a-(i+1)]) + c

    if t_sum >= 10:
        c = 1
        t_sum = t_sum - 10
    else:
        c = 0
    res = res + str(t_sum)
if c == 1:
    res = res + str(c)
print(res[::-1])
