#numbersfollwedbyzeroes

l=['0','1','2','3','0','0']
b=[]
c=[]
for i in l:
    if i=='0':
        c.append(i)
    else:
        b.append(i)
res=b+c
print(res)
