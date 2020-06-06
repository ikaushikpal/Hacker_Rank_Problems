n = int(input())
my_list = list(map(int,input().split()))

result = []
for i in range(len(my_list)):

    for j in range(i+1, len(my_list)):
        if my_list[i]==my_list[j]:
            value = abs(i-j)
            result.append(value)

if len(result)>=1:
    print(min(result))
else:
    print(-1)

