from math import sqrt

n = int(input())
a1=0
a2=1
b1=0
b2=1
if n==0: print("Tak")
while a2 <= n:
    a1, a2 = a2, a1+a2

sq = sqrt(n)
while sq <= a2:
    if n%a2==0:
        t=n//a2
        while b2<t:
            b1, b2 = b2, b1+b2
        if b2==t:
            print("TAK", a2, b2)
            exit()
    a1, a2 = a2-a1, a1

print("NIE")

