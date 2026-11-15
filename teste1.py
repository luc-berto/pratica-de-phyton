acuracy = 0
tp = 0
fp = 0
fn = 0
tn = 0
resultados = [
    {"real": "spam", "previsto": "spam"},
    {"real": "normal", "previsto": "normal"},
    {"real": "spam", "previsto": "normal"},
    {"real": "spam", "previsto": "spam"},
    {"real": "normal", "previsto": "spam"},
    {"real": "normal", "previsto": "normal"},
    {"real": "spam", "previsto": "spam"},
    {"real": "normal", "previsto": "normal"}
]

def calcular_acuracy(resultados):
    
    previsoes = [resultados[i]["previsto"] for i in range(len(resultados))]
    reais = [resultados[i]["real"] for i in range(len(resultados))]
    acertos = 0
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    for i in range(len(resultados)):
        if previsoes[i] =="spam" and reais[i] == "spam":
            tp += 1
        elif  previsoes[i] == "spam" and reais[i] == "normal":
            fp += 1
        elif previsoes[i] == "normal" and reais[i] == "spam":
            fn += 1
        elif previsoes[i] == "normal" and reais[i] == "normal":
            tn += 1
    acertos = tp + tn
    acuracy = (acertos / len(resultados)) * 100
    precision = tp / (tp+fp) * 100
    recall = tp / (tp+fn) *100
    return (acuracy, precision, recall, tp, fp, fn, tn)

acuracy, precision, recall, tp, fp, fn, tn = calcular_acuracy(resultados)
print(f"Acurácia: {acuracy:.2f}%") 
print(f"Precision: {precision:.2f}%")
print(f"Recall: {recall:.2f}%")
print(f"TP: {tp}, FP: {fp}, FN: {fn}, TN: {tn}")