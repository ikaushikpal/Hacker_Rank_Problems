n, k = map(int,input().split())
my_list = list(map(int, input().split()))
count = 0
p = 1
for val in my_list:
    for i in range(1,val+1):
        if i==p:
            count += 1
        if i==val or i%k ==0:
            p +=1 
            
        
print(count)
        
    
    