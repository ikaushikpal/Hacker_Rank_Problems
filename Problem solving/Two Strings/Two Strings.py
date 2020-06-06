q = int(input())

while q!=0:
    s1= input()
    s2 = input()
    if s1==s2:
        print("YES")
    else:
        f=0
        s1 = list(set(s1))
        s2 = list(set(s2))
        for i in range(len(s1)):
            if f==1:
                break
            for j in range(len(s2)):
                if s1[i]==s2[j]:
                    print("YES")
                    f=1
                    break
            
        if f==0:
            print("NO")
    q -= 1
