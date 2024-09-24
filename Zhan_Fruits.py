
def fruits(n,x,y):

    if y >= x :
        if n % x == 0:
            return n // x
        else:
            if n < x:
                return 1
            return (n // x) + 1

    else:
        if n % y == 0:
            return n // y
        else:
            if n < y:
                return 1
            return (n // y) + 1

t = int(input())
while( t > 0):
    n = int(input())
    x,y = map(int,input().split())
    print(fruits(n,x,y))
    t -= 1
