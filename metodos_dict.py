# Método clear
contatos = {
    "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666" },
    "maria@gmail.com" : {"nome" : "Maria" , "telefone" : "98888-5555" },
    "luis@gmail.com" : {"nome" : "Luis" , "telefone" : "99696-6969"}
}

contatos.clear()
print(contatos)

print("-" * 100)

# Método copy
contatos = {
    "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666"}
}

copia = contatos.copy()
copia["fernando@gmail.com"] = {"nome" : "Fer"}
print(contatos["fernando@gmail.com"])
print(copia["fernando@gmail.com"])

print("-" * 100)

# Método fromkeys
print(dict.fromkeys(["nome", "telefone"]))
print(dict.fromkeys(["nome", "telefone"], "exemplo"))

print("-" * 100)

# Método get

contatos = {
    "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666"}
}

contatos["chave"]  # KeyError

resultado = contatos.get("chave") # None
print(resultado)

resultado = contatos.get("chave", {}) # {}
print(resultado)

resultado = contatos.get("fernando@gmail.com", {}) # "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666"}
print(resultado)

print("-" * 100)

# Método items

contatos = {
    "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666"}
}

print(contatos.items()) # retorna uma lista de tupla

print("-" * 100)

# Método Keys
print(contatos.keys()) # retorna chaves

# Método pop

resultado = contatos.pop("fernando@gmail.com") # None
print(resultado)

resultado = contatos.pop("fernando@gmail.com", {}) # {}
print(resultado)

#contatos.popitem() # retira itens na sequencia

print("-" * 100)

# Método setdefault
contato = {"nome" : "Fernando", "telefone" : "99999-6666"}

contato.setdefault("nome", "Maria") # Não altera o que já existe
print(contato)
contato.setdefault("idade", "34") # Cria uma chave e valor que não existe
print(contato)

print("-" * 100)

# Método update
contatos = {
    "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666"}
}

contatos.update({"fernando@gmail.com" : {"nome" : "Fer"}}) # Subistitui o valor de uma chave existente
print(contatos)

contatos.update({"maria@gmail.com" : {"nome" : "Maria", "telefone" : "99999-5555"}}) # adiciona uma nova chave com valores
print(contatos)

print("-" * 100)

# Método values
contatos = {
    "fernando@gmail.com" : {"nome" : "Fernando" , "telefone" : "99999-6666" },
    "maria@gmail.com" : {"nome" : "Maria" , "telefone" : "98888-5555" },
    "luis@gmail.com" : {"nome" : "Luis" , "telefone" : "99696-6969"}
}

print(contatos.values())

print("-" * 100)

# Método in

resultado = "fernando@gmail.com" in contatos
print(resultado)

resultado = "fer@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["fernando@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["maria@gmail.com"]
print(resultado)

print("-" * 100)

# Método del

del contatos["fernando@gmail.com"]["telefone"]
del contatos["luis@gmail.com"]
print(contatos)