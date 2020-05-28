def countApplesAndOranges(s, t, a, b, apples, oranges):
    no_of_apples = 0
    no_of_oranges = 0
    for val in apples:
        dist = val + a
        if dist>=s and dist<=t:
            no_of_apples += 1
    for val in oranges:
        dist = val + b
        if dist>=s and dist<=t:
            no_of_oranges += 1
    print(f"{no_of_apples}\n{no_of_oranges}")
    
    
countApplesAndOranges(2, 3,1, 5,[2],[-2])