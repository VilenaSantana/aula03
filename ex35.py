a = 0
for x in range (1,11):
    n = int(input(f"Digite o número {x}: "))
    if n >= 10 and n <= 20:
        a += 1
print(f"A quantidade de números entre 10 e 20 é {a}.")
