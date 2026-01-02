def binary(a):
    c=""
    while a!=0:
        b=a%2
        a=a//2
        c=str(b)+c
    print(c)
binary(55)    