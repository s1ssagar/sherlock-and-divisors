z = input()
for cas in xrange(z):
    n = input()
    if n % 2: # odd
        print 0
    else:
        n /= 2
        ans = 1
        p = 2
        while p <= n:
            if p * p > n: p = n
            e = 0
            while n % p == 0:
                print n, p
                e += 1
                n /= p
            ans *= e + 1
            p += 1
        print ans