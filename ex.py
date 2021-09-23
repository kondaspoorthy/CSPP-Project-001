def totalvaluespossible(n):
    num=1
    for i in range(1,n):
       num=num+pow(2,i)
    return num
def pow(r,i):
    l=1
    for i in range(0,i):
        l=l*2
    return  l
print(totalvaluespossible(32))
