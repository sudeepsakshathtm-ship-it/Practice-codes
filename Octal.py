i=0
decimal=55
f=decimal
octal=8
k=""
while decimal!=0:
    j=decimal%octal
    print(j)
    k=str(j)+k
    decimal=decimal//octal
    print(decimal)
print("the octal number of",f,"is",k)