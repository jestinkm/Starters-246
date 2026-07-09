# cook your dish here
import sys
input=sys.stdin.readline
t=int(input())
o=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    o.append(max(min(a[i],a[i+1]) for i in range(n-1)))
print('\n'.join(map(str,o)))