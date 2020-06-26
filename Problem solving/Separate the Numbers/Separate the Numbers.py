def separateNumbers(s):
    s = str(s) 
    length = len(s)
    s_rev = s[::-1]
    i = 1
    flag = 0
    while(2*i<length):
        if abs(int(s_rev[0])-int(s_rev[i])) == 1:
            if abs(int(s_rev[i])-int(s_rev[2*i])) == 1:
                flag = 1
                count = i
                break
        i += 1
    if flag==0:
        return 'NO'
    i = 1
    count_temp = count
    while i<(length//count):
        count_temp += count
        if abs(int(s[0:count])-int(s[count_temp-count:count_temp])) != i:
            return 'NO'
        i += 1    
    return f"YES {s[0:count]}" 



print(separateNumbers("13"))
print(separateNumbers("91011"))
print(separateNumbers("1234"))
print(separateNumbers("99100"))
print(separateNumbers("101103"))
print(separateNumbers("13"))
print(separateNumbers("13"))
print(separateNumbers("13"))
