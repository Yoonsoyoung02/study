str = input()
new_str = []

new_str = "".join([i.upper() if i.islower() else i.lower() for i in str])
print(new_str)