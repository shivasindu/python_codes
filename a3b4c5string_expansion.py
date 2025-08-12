s="a3b4c5"
chars=s[::2]
count=s[1::2]
res=''.join(x*int(y) for x,y in zip(chars,count))
print(res)
