h1 = [3,2,1,1 ,1]
h2 = [4 ,3, 2]
h3 = [1 ,1, 4, 1]

"""  my code 
def equalStacks(h1, h2, h3):
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)
    while s1 !=0 and s2 != 0 and s3 != 0 and (s1!=s2 or s2!=s3):
        print(s1,s2,s3)
        if(s1>s2 and s1>s3):
            s1 -= h1[0]
            h1.pop(0)
            
        elif(s2>s1 and s2>s3):
            s2 -= h2[0]
            h2.pop(0)
            
        else:
            s3 -= h3[0]
            h3.pop(0)
    if(s1 == s2 and s2 == s3):
        return s1
    else:
        return 0  
 """

 
def equalStacks(h1, h2, h3):
    l1, l2, l3 = 0, 0, 0
    for each in h1:
        l1 = l1 + each
    for each in h2:
        l2 = l2 + each
    for each in h3:
        l3 = l3 + each
    while l1 !=0 and l2 != 0 and l3 != 0 and (l1!=l2 or l2!=l3):
        if max(l1, l2, l3) == l1:
            l1 = l1 - h1[0]
            h1.pop(0)
        elif max(l1, l2, l3) == l2:
            l2 = l2 - h2[0]
            h2.pop(0)
        else:
            l3 = l3 - h3[0]
            h3.pop(0)
    else:
        if l1==l2 and l2==l3:
            return l1
        else:
            return 0  


print(equalStacks(h1,h2,h3))