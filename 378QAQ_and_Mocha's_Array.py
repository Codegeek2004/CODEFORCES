def beautiful(t,arr):
    count=0
    i=0
    while( i<t ):
        k=arr[i]
        c=0
        b=0
        for j in range(t):
            
            if arr[j] % k == 0:
                c+=1
                   
            if arr[j] % l ==0:
                b+=1  
        if c+b >= t:
            count+=1
        i+=1
    if count >= 1:
        return 'Yes'
    else:
        return 'No'



n=int(input())
while n>0:
    t=int(input())
    arr=list(map(int,input().split()))
    print(beautiful(t,arr))
    n-=1