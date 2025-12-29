def sarr(sarr):
    i=0
    while i<len(sarr):
        k=i+1
        while k<len(sarr):
            if sarr[i]>sarr[k]:
                t=sarr[k]
                sarr[k]=sarr[i]
                sarr[i]=t
            k+=1
        i+=1
    print(sarr)

sarr([8,4,6,7,3,2,0])   