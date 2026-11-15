contagem = {}
numero = [2, 5, 2, 8, 5, 2, 10, 8, 5, 5]

for i in range(len(numero)):
    atual = numero[i]

    if atual in contagem:
        contagem[atual] += 1
    else:
        contagem[atual] = 1

for numero, quantidade in contagem.items():
    print(numero,quantidade)
