#Fibonacci Series
n=int(input("Enter the range you want to print Fibonacci series: "))
a,b=0,1
c=a+b
print(a,b,end=" ")
while c<n:
    print(c,end=" ")
    a=b
    b=c
    c=a+b