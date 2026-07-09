# cook your dish here
for _ in range(int(input())):
    r,y=map(int,input().split())
    print(r+max(0,y-r)//2)