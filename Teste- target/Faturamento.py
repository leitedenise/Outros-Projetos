'3- Faturamneto: '

f = [31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269, 0.0000, 6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000, 39807.6622, 27261.6304, 39775.6434, 29797.6232, 17216.5017, 0.0000,  0.0000, 12974.2000, 28490.9861, 8748.0937, 8889.0023, 17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 10299.6761, 39874.1073]

if f[0] != 0:
    menor = f[0]
    maior = f[0]

soma = 0
quant = 0
for i in range(len(f)):
    if f[i] != 0:
        if f[i] < menor:
            menor = f[i]

        if f[i] > maior:
            maior = f[i]

        soma += f[i]
        quant += 1
med = soma / quant

dias = 0
for i in range(len(f)):
    if f[i] > med:
        dias += 1

print(f'O menor valor de faturamento foi: {menor}\nO maior valor de faturamento foi: {maior}\nMédia mensal: {med:.2f}\nNúmero de dias em que o faturamento diário foi superior à média: {dias}')