entrada = int(input(""))
cont = 0
for c in range(1, entrada + 1):
    if entrada % c == 0:
        cont = cont + 1
if cont == 2:
    print("True")
else:
    print("False")
    
