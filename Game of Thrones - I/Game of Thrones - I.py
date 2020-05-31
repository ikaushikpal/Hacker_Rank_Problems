string = input()


u = list(set(string))
odd_list = []

for val in u:
    count = string.count(val)
    if count %2 !=0:
        odd_list.append(count)
        

if len(odd_list)<2:
    print("YES")
else:
    print("NO")
