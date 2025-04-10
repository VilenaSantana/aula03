n = int(input("Digite um numero: "))
print (f"Os números impares até {n} são:")
for x in range (0,n+1,1):
  if x%2!=0:
   print (x,end=" ")
   