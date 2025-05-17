alphabet = input()

croatian = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for alpha in croatian :
    alphabet = alphabet.replace(alpha,"*")

print(len(alphabet))