# cook your dish here

import sys
input=sys.stdin.readline
MOD=998244353
mx=2005
fact=[1]*(mx+1)
for i in range(1,mx+1):fact[i]=fact[i-1]*i%MOD
inv=[1]*(mx+1)
inv[mx]=pow(fact[mx],MOD-2,MOD)
for i in range(mx,0,-1):inv[i-1]=inv[i]*i%MOD
def C(n,r):
    if r<0 or r>n or n<0:return 0
    return fact[n]*inv[r]%MOD*inv[n-r]%MOD
o=[]
for _ in range(int(input())):
    n,k=map(int,input().split())
    tt=0
    for t in range(n):
        m=n-t+1
        s=0;sign=1;i=0
        while i*k<=t:
            s=(s+sign*C(m,i)*C(t-i*k+m-1,m-1))%MOD
            sign=-sign;i+=1
        tt=(tt+s*fact[t]%MOD*fact[n-t])%MOD
    o.append(tt%MOD)
print('\n'.join(map(str,o)))