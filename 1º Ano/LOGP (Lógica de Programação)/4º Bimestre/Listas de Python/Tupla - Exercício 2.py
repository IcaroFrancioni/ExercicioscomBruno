cores = ('vermelho', 'azul', 'verde', 'amarelo', 'preto')
for i in range(5):
    if cores[i] == 'verde':
        indiceverde = i +1

if indiceverde > 0:
    print("O índice do verde é: ", indiceverde)
else:
    print("Não tem índice verde")
numazul = 0
for i in range(5):
    if cores[i] == 'azul':
        numazul = numazul+1
print(f"O numero azul aparece {numazul} vezes na tupla")
novatupla = cores + ('branco', 'cinza')
print("Nova tupla: ", novatupla)