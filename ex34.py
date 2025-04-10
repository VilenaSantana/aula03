a = 0
for x in range (1,11):
    n = int(input(f"Digite o número {x}: "))
    if n < 0:
        a += 1
print(f"A quantidade de números negativos é {a}.")