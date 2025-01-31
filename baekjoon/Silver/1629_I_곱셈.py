import sys
input = sys.stdin.readline

source = list(map(int,input().split()))

def times(a,b,c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (times(a,b//2,c)**2)%c
    else :
        return (times(a,b//2,c)**2*a)%c

print(times(source[0],source[1],source[2]))