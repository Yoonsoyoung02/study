num_list = list(map(int,input().split()))

if num_list == sorted(num_list):
    print("ascending")
elif num_list == sorted(num_list, reverse=True):
    print("descending")
else:
    print("mixed")