numeros = (10, 20, 30, 40, 50)
terceironum = numeros[2]
print("Terceiro numero:", terceironum)
flag = 0
for i in range(5):
    if numeros[i] == 20:
        flag = 1
if flag==1:
    print("Número 20 está na lista")
else:
    print("Número 20 não está na lista")
numlista = list(numeros)
print("Nova lista: ", numlista)