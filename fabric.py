
def fab(n):
  if n==1:
    return 1
  if n==0:
    return 0
  else:
    result=int(fab(n-1))+int(fab(n-2))    
    return result
    
f=open("e:/fabaric.txt","w")
answer=input("Input your max number:")
for i in range(answer):     #give a test in range 0---111
  print(fab(i),file=f)
  
