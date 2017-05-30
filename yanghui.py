def yanghui(m,n):
    a = [1]
    l = 0
    while True:
        if l == m:
            return a
        a = [1] + [a[i] + a[i + 1] for i in range(len(a) - 1)] + [1]
        l = l + 1
        if l % 1000 == 0:
            print l

if __name__ == '__main__':
    m,n = 500000,22
    ans = yanghui(m,n)
    print ans[n]
