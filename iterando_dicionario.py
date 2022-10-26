contatos = {
    "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666" },
    "maria@gmail.com" : {"nome" : "Maria" , "telefone" : "98888-5555" },
    "luis@gmail.com" : {"nome" : "Luis" , "telefone" : "99696-6969"}
}

for chave in contatos:
    print(chave, contatos[chave])

print("-" * 100)

for chave, valor in contatos.items():
    print(chave, valor)