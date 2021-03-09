Coding:
  
def fac(n):
  if n==0:
    return 1
  else:
    return n*fac(n-1)
a=int(input())
b=int(fac(a))
c=0  
while (c==0):
  c=int(b%10)
  b=int(b/10)
print(c)
