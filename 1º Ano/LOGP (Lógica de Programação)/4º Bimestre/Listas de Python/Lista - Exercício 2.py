numeros = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
numeros.sort()
soma = 0
for i in range(10):
    soma += numeros[i]

maiornum = max(numeros)
menornum = min(numeros)

print(soma)
print("Maior número: ", maiornum)
print("Menor número: ", menornum)
print(numeros)