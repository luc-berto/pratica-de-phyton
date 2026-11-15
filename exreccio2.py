numeros = []
def pegar_lista():
    lista = []
    for i in range(10):
        lista.append(int(input("Digite um numero: ")))
    return lista

numeros = pegar_lista()

def contar_ocorrencias(numeros):
    contagem = {}
    for i in range(len(numeros)):
        atual = numeros[i]

        if atual in contagem:
            contagem[atual] += 1
        else:
            contagem[atual] = 1
    return contagem

contagem = contar_ocorrencias(numeros)
maior = 0
for numero, quantidade in contagem.items():
    if quantidade  > maior:
        maior = quantidade
        numerom = numero

for numero, quantidade in contagem.items():
    if maior == quantidade:
        print("O numero "+str(numero)+" foi o que mais apareceu, com  "+str(maior)+" ocorrencias")  
