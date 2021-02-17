def czy_palindrom(n):
    s = str(n)
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True

def czy_palindrom_2(n):
    s = bin(n)[2:]
    print(s)
    return czy_palindrom(s)

n = int(input())
print(czy_palindrom(n))
print(czy_palindrom_2(n))

