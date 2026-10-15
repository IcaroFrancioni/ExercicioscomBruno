nomes = ['Ana', 'Carlos', 'Beatriz', 'Daniel', 'Elisa']
flag = 0
for i in range(5):
    if nomes[i] == 'Carlos':
        flag = 1
if flag == 1:
    print("O nome Carlos está na lista")
else:
    print("O nome Carlos não está na lista")
nomeana = 0 
nomes[2] = 'Bruna'
for i in range(5):
    if nomes[i] == 'Ana':
        nomeana = nomeana+1
print("O nome Ana aparece:", nomeana)
print(nomes)
