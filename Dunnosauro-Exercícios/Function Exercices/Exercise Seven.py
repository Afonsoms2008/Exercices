def valor_pagamento(valor, atraso):
    if atraso > 0:
        multa = 0.03 + 0.001 * atraso
        valor = valor + valor * multa

    return valor


prestacoes = 0
gasto = 0

while True:
    prestacao = float(input("Introduz o valor da prestação: "))

    if prestacao == 0:
        break

    atraso = int(input("Introduz quantos dias de atraso tem: "))

    valor = valor_pagamento(prestacao, atraso)

    print(f"O valor a ser pago é de {valor:.2f} euros")

    prestacoes += 1
    gasto += valor


print("-" * 50)
print(f"Foram pagas {prestacoes} prestações")
print(f"E foi pago um total de {gasto:.2f} euros")