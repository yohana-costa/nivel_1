historico = []  

print("=== PDV - Ponto de Venda ===")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    valor = float(input("Valor da compra (R$): "))

    if valor == 0:
        break

    if valor < 0:
        print("Aviso: o valor não pode ser negativo. Tente novamente.\n")
        continue

    idade = int(input("Idade do cliente: "))

    if idade < 0:
        print("Aviso: a idade não pode ser negativa. Tente novamente.\n")
        continue

    valor_final = valor
    if idade >= 65:
        valor_final = valor_final * 0.8

    if valor_final > 100:
        valor_final = valor_final * 0.9

    valor_final = round(valor_final, 2)
    desconto = round(valor - valor_final, 2)

    print(f"Valor final: R$ {valor_final:.2f}\n")

    historico.append({
        "valor_original": valor,
        "idade": idade,
        "desconto": desconto,
        "valor_final": valor_final,
    })


total_bruto = 0
total_descontos = 0
total_final = 0

for compra in historico:
    total_bruto += compra["valor_original"]
    total_descontos += compra["desconto"]
    total_final += compra["valor_final"]

print("\n=== Resumo do dia ===")
print(f"Compras registradas: {len(historico)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")