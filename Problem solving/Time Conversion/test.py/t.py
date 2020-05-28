# ar = '1 2 3 4 3 3 2 1'.split()
# ar = [int(x) for x in ar]
# print(ar)


# def cutTheSticks(arr):
#     print(len(arr))
#     while len(arr)!=1:
#         count = 0
#         low = min(arr)
#         for i in range(len(arr)):
#             arr[i] = arr[i] - low
#         i = 0    
#         t= False
#         while i < len(arr):
#             if arr[i]<=0:
#                 arr.pop(i)
#                 t = True
#             else:
#                 count +=1 
#                 i += 1
#         if count!=0:
#             print(count)
#         if not arr:
#             return
        
                
# cutTheSticks(ar)

# ar = '8 8 14 10 3 5 14 12'.split()
# ar = [int(x) for x in ar]
# print(ar)
# cutTheSticks(ar)


def nonDivisibleSubset(k, s):
    count_list = [0]*k
    for val in s:
        count_list[val%k] += 1
    count = min(count_list[0],1)

    for i in range(1,k//2+1):
        if i!=k-i:
            count += max(count_list[i],count_list[k-i])
    if k%2==0:
        count += 1
    return count


ar = '8 8 14 10 3 5 14 12'.split()
ar = [int(x) for x in ar]
print(nonDivisibleSubset(4,))