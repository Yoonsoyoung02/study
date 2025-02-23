n,h,v = map(int,input().split())

v2 = n-v
h2 = n-h

size1 = h*v
size2 = h*v2
size3 = h2*v
size4 = h2*v2

max_size = max(size1,size2,size3,size4)

print(max_size*4)