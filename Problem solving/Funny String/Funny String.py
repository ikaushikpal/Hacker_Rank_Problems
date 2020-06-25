def funnyString(s):
    s_rev = s[::-1]
    s1 =[]
    s2 = []
    for i in range(1,len(s)):
        s1.append(ord(s[i])-ord(s[i-1]))
    for i in range(1,len(s)):
        s2.append(abs(ord(s_rev[i])-ord(s_rev[i-1])))
        
    if s1!=s2:
        return 'Not Funny'
    return 'Funny'
        

print(funnyString("acxz"))
print(funnyString("bcxz"))
print(funnyString("lmnop"))

