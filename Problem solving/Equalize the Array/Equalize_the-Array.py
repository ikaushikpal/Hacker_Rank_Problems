# input from console 
n = int(input())
arr = list(map(int,input().split()))

# logic
arr_unique = list(set(arr)) # making set of arr and then convert to list for slicing
my_list = []


for val in arr_unique:
    my_list.append(n- arr.count(val))

print(min(my_list))

    