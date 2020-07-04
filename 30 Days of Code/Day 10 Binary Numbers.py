n = int(input())
bin_n = str(bin(n))
actual_bin_num = bin_n[2:]
count = []
val = 1
for i in range(len(actual_bin_num)-1):
    if actual_bin_num[i] == '1' and actual_bin_num[i+1] == '1':
        val += 1
    else:
        count.append(val)
        val = 1
count.append(val)
print(max(count))
