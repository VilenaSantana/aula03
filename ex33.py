'''n = int(input("Digite um número: "))
for x in range (1,n+1,1):
    if n < 0:
        print("Número inválido digite um valo maior que 0 ")
    else:
        print(x,end=" ")'''

n = int(input("Digite um número: "))
if n > 0:
    for x in range(1, n + 1, 1):
        print(x, end=" ")
else:
    print("Número inválido digite um valo maior que 0 ")