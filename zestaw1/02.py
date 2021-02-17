a = int(input())
b = int(input())
n = int(input())


print(a//b, end='.')
for _ in range(n):
    a = a%b
    a*=10
    print(a//b, end='')
