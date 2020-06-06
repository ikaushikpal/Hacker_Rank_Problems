def kaprekarNumbers(p, q):
    count = 0
    for i in range(p,q+1):
        val = str(i**2)
        length = len(val)
        if val == '1':
            print(1,end=' ')
            count += 1
        elif length>1:
            mid = length//2
            l = int(val[0:mid])
            r = int(val[mid:])
            if l+r == int(i):
                print(i,end=' ')
                count += 1
    if count == 0:
        print("INVALID RANGE")



if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)