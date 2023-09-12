print("funcao F = 2x+1")
print("funcao G = x+4")
print(" ")
print(" ")
print("(1) GoF")
print("(2) GoG")
print("(3) FoF")
print("(4) FoG")

varescolha=(input("insira a operação que deseja realizar "))
if varescolha == 1:
    varX = int(input("insira um valor para x "))
    funF = 2 * varX + 1
    varY = funF
    funG = varY + 4
    print(funG)
elif varescolha == 2:
    varX = int(input("insira um valor para x "))
    funG = varX + 4
    varY = funG
    funG = varY + 4
    print(funG)
elif varescolha == 3:
    varX = int(input("insira um valor para 'x' "))
    funF = 2 * varX + 1
    varY = funF
    funF = 2 * varY + 1
    print(funF)
elif varescolha == 4:
    varX = int(input("insira um valor para 'x' "))
    funG = varX + 4
    varY = funG
    funF = 2 * varY + 1
    print(funF)
else:
   print ("digite um numero de 1 ate 4")