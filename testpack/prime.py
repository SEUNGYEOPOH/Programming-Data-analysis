def prime_print(n):
    for i in range(2,n+1):
        count=0
        for z in range(1,i+1):
                if i%z==0:
                    count+=1
        if count==2:
            print(i)