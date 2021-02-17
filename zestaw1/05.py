n = input()
k = int(input())
for i in range(1, 2**int(len(n))):
    t = bin(i)[2:].zfill(len(n))
    s=''
    for j in range(len(t)):
        if t[j]=='1':
            s += n[j]
    if int(s)%k==0: print(s)
    