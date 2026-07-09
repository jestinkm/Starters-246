# cook your dish here
import sys
input=sys.stdin.readline
o=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    e=0
    tot=0
    for x in a:
        e=max(x,e)
        tot+=e-x
    o.append(tot)
print('\n'.join(map(str,o)))