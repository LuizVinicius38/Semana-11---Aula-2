entrada = int(input(""))
x = int(input(""))
for aux in range(entrada, x +1):
    if aux > 1:
        for i in range(2, aux):
            if aux % i == 0:
                break
            else:
                print(aux)
                break
