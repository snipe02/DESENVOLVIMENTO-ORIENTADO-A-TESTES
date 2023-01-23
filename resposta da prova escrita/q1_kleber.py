def soma(n1, n2):
    if n2 > n1:
        somas = 0
        for c in range(n1, n2+1):
            somas += c
    return somas

num1 = int(input())
num2 = int(input())

ch = soma(num1, num2)
print(ch)
