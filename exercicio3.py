
alunos = {}


for i in range(5):
        nome = input("Digite um nome: ")
        nota = input("Digite uma nota: ")
        alunos[nome] = float(nota)

def calcular_media(alunos):
    media = 0
    contador = 0
    for nota in alunos.values():
        media += nota
        contador += 1
    resultado = media / contador
    return resultado
resultado = calcular_media(alunos)
print("Media da turma: ", resultado)
def acima_da_media(alunos,resultado):
    
    for nome, nota in alunos.items():
        if nota > resultado:
            print(f"{nome} está acima da media com nota {nota}")

acima_da_media(alunos, resultado)  
   
