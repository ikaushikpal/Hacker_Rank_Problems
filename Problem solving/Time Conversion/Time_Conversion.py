s = "07:05:45PM"

def timeConversion(s):
    s=s.split(':')
    day = 1
    time_list =[]
    if 'PM' in s[2]:
        day = 0
    if day==0:
        if(s[0]!='12'):
            val = s[0]
            val = int(val)
            val += 12
            val = str(val)
            time_list.append(val)
        else:
            time_list.append(s[0])
    else:
        if(s[0]!='12'):
            time_list.append(str(s[0]))
        else:
            time_list.append('00')
    time_list.append(str(s[1]))
    tmp = str(s[2])
    sec = str(tmp[0])+str(tmp[1])
    sec = str(sec)
    time_list.append(sec)
    return ':'.join(time_list)

print(timeConversion("12:45:54PM"))


di = {i:i**2 for i in range(5)}
print(di.items())
di2 = {j:i for (i,j) in di.items()}

li = list(map(lambda x: x**2,di.values()))

import heapq as heap
heap.heapify(li)

import numpy as np

