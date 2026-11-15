numero = [0]* 5

pares = 0
impares = 0

for i in range(5):
    numero[i] = int(input("Digite um numero:"))

print("Numeros pares:", end=" ,")
for i in range(5):
    if numero[i] % 2 == 0:
        pares+= numero[i]
        print(numero[i], end=" ,")
    else:
        impares += 1

print("\nQuantidade de numeros impares: "+str(impares))
print("Soma dos numero pares: "+str(pares))