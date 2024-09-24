def check_arr(l,arr):
    arr_sorted=sorted(arr)
    i=0
    j=0
    while(i<l):
        x=arr[:i]
        y=arr[i:]
        if y+x == arr_sorted:
            return 'Yes'
        i+=1
    else:
        return 'No'
            


n=int(input())
while n>0:
    l=int(input())
    arr=list(map(int,input().split()))
    print(check_arr(l,arr))
    n-=1