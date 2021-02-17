n = int(input())
w = 6
i = 8
while i <= n:
    t = i
    while t%2==0: t /= 2
    while t%3==0: t /= 3 
    while t%5==0: t /= 5
    if t==1:
        w += 1
    i += 1
print(w)