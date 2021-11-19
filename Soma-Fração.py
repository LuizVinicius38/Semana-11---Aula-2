print("H = 1 + 1/2 + 1/3.... + 1/n!")
n = 0
h = 0
while n <= 1:
    entrada = int(input("Digite o valor de (n)! "))
    h = h +(1 / entrada)
    n = n + 1
print(h)