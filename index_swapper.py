n=int(input())
s=list(map(int,input().split()))
i1=int(input())
i2=int(input())
s[i1],s[i2]=s[i2],s[i1]
print(s)
