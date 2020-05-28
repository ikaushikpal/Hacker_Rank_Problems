n=6
k=7
cookie = [1, 2, 3, 9, 10, 12]

""" my code

def cookies(k, A):
    A.sort()
    count = 0
    while A[0]<k and len(A)>2:
        if A[0]<k:
            val = A[0] + 2*A[1]
            A.pop(0)
            A.pop(0)
            A.append(val)
            A.sort()
            count += 1
    if A[0]<k:
        return -1
    else:
        return count

"""

import heapq

def cookies(k, heap):
    heapq.heapify(heap)
    ops = 0
    while heap[0] < k:
        c = heapq.heappop(heap) + 2 * heapq.heappop(heap)
        heapq.heappush(heap, c)
        ops += 1
    return ops

try:
    result = cookies(k, my_cookies_list)
except IndexError:
    result = -1
print(result)    



print(cookies(3581,[6214, 8543, 9266, 1150, 7498, 7209, 9398, 1529, 1032 ,7384 ,6784 ,34 ,1449 ,7598 ,8795 ,756 ,7803 ,4112 ,298 ,4967 ,1261 ,1724 ,4272 ,1100,9373]))