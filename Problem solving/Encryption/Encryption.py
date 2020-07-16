import math


base_text = input()
l = len(base_text)
m = int(math.sqrt(l))
n = int(math.ceil(math.sqrt(l)))

if(m*n < l):
    m = max(m, n)
    n = m

encripted_text = []
for i in range(m):
    start = i*n
    end = start + n
    base = list(base_text[start:end])
    encripted_text.append(base)


for i in range(len(encripted_text[m-1]), n+1):
    encripted_text[m-1].append(0)

for i in range(n):
    for j in range(m):
        if encripted_text[j][i] != 0:
            print(encripted_text[j][i], end='')
    print(" ", end='')
