length = 6
arr = list()
for i in range(length):
    s = list(map(int,input().split()))
    arr.append(s)

tot = []
for i in range(length-2): 
    for k in range(length-2):
        val = 0
        val += sum(arr[i][k:k+3]) + arr[i+1][k+1] + sum(arr[i+2][k:k+3])
        tot.append(val)
print(max(tot))

