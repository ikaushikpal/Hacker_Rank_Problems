user = list(map(int,input().split()))
book_bank = list(map(int,input().split()))
fine = 0

if user[1] <= book_bank[1] and user[2] <= book_bank[2] and user[0] <= book_bank[0]:
    fine = 0
elif user[2] > book_bank[2]:
    fine = 10000
elif user[1] == book_bank[1] and user[2] == book_bank[2]:
    fine = 15*(user[0]-book_bank[0])
elif user[2] == book_bank[2] and user[1] > book_bank[1]:
    fine = 500*(user[1]-book_bank[1])


print(fine)

