'''
1. Crie uma agenda utilizando dicionário, a agenda deve ter uma lista de 3 contatos.

2. Os contatos, além do nome, devem possuir telefone e email.

3. Verifique se há algum contato com o nome 'marcos'.

4. Altere o telefone do primeiro contato.

5. calcule quanto contatos possuem na lista.
'''
contatos = {
    'Léo':['(11)91234-5678','leo@gmail.com'],
    'Luan':['(11)99876-5432','luan@gmail.com'],
    'Marcos':['(11)91234-1234', 'marcos@gmai.com'],
}
resultado = False
cont = 0

for keys in contatos:
    cont += 1
    if keys == 'Marcos':
        resultado = True

if resultado == True:
    print('Há um Marcos nos contatos')
else:
    print('Não há um Marcos nos contatos')

contatos['Léo'][0] = '(16)98181-8282'

print('O dicionário possui', cont, 'contatos.')