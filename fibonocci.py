def fib(n):
    s=[]
    a,b=0,1
    for i in range(1,n+1):
        s.append(a)
        a,b=b,a+b
    return s
N=int(input("Enter number:"))
print(fib(N))
        
