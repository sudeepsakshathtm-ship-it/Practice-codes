def fact(a):
    g=a
    k=1
    while 0<a:
        k=k*a
        a-=1
    print("The factorial of",g,"value is",k)
fact(int(input("enter a value")))