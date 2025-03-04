while True:
    A,B,C = map(int,input().split())

    if A==0 and B == 0 and C == 0:
        break
    
    list_sorted = sorted([A,B,C])
    if list_sorted[0]**2 + list_sorted[1]**2 == list_sorted[2]**2:
        print("right")
    else:
        print("wrong")