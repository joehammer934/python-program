from functools import reduce

def change(s):
    return (s[:1].upper()+s[1:].lower())

a=['micheL','liSA','FriENDS']
r=list(map(change,a))
print(r)
