def jimOrders(order_id, prep):
    serving_time = dict()
    for i in range(len(prep)):
        if order_id[i]+prep[i] in serving_time.keys():
            serving_time[order_id[i]+prep[i]].append(i+1)
        else:
            serving_time[order_id[i]+prep[i]] = [i+1]

    temp = list(serving_time.keys())
    temp.sort()
    for value in temp:
        res = serving_time[value]
        for r in res:
            print(r, end=' ')


if __name__ == '__main__':
    n = int(input())
    orders = []
    order_id, prep = [], []
    for _ in range(n):
        orders = list(map(int, input().rstrip().split()))
        order_id.append(orders[0])
        prep.append(orders[1])

    jimOrders(order_id, prep)
