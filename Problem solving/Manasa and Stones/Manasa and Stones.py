def stone(a,b,n,count,my_list):
    if n==1:
        my_list.append(count)
        return
    stone(a,b,n-1,count+a,my_list)
    stone(a,b,n-1,count+b,my_list)

t = int(input())
for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    my_list = []
    stone(a,b,n,0,my_list)
    my_list = list(set(my_list))
    my_list.sort()
    for v in my_list:
        print(v,end=' ')
    print()

