nota = [0]* 5

media = 0
resultado = 0

for i in range(5):
        nota[i] = int(input("Digite uma nota: "))

def calcular_media(nota):
    media = 0
    for i in range(5):
        media += nota[i]
    resultado = media / 5
    return resultado

resultado = calcular_media(nota)

    
print("Media: ",resultado)
if resultado >=7.0:
    print("Situacao: Aprovado")
else:
    print("Situacao: Reprovado")
