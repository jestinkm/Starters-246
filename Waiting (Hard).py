import sys

def solve(n, a):
    pm = [0]*n
    pm[0] = a[0]
    for i in range(1, n):
        pm[i] = max(pm[i-1], a[i])
    w = [pm[i]-a[i] for i in range(n)]
    ps = [0]*(n+1)
    for i in range(n):
        ps[i+1] = ps[i] + w[i]
    best = ps[n]
    for k in range(n):
        pb = pm[k-1] if k else 0
        base = ps[k]
        cm = pb if k else 1
        add = 0
        for i in range(k+1, n):
            cm = cm if cm > a[i] else a[i]
            if cm == pm[i]:
                add += ps[n] - ps[i]
                break
            add += cm - a[i]
        c = base + add
        if c < best:
            best = c
    return best

def main():
    d = sys.stdin.buffer.read().split()
    p = 0
    t = int(d[p]); p += 1
    r = []
    for _ in range(t):
        n = int(d[p]); p += 1
        a = list(map(int, d[p:p+n])); p += n
        r.append(str(solve(n, a)))
    sys.stdout.write('\n'.join(r) + '\n')

main()