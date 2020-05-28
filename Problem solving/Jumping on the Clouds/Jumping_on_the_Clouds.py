# input from console 
n = int(input())
arr = list(map(int,input().split()))

count,i = 0 ,0

while(i<len(arr)):
    if i+2<len(arr) and arr[i+2]==0:
        i += 2
    else:
        i += 1
    count +=1

print(count-1)