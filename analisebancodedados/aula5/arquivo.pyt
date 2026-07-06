"""Tipos, Estruturas de Dados e Fluxos de Controle (Parte 1)
Exemplos práticos de Python para entender os conceitos fundamentais.
"""

# Tipos básicos
inteiro = 42
flutuante = 3.14
texto = "Olá, Python!"
booleano = True

print("Tipos básicos:")
print("inteiro:", inteiro, type(inteiro))
print("flutuante:", flutuante, type(flutuante))
print("texto:", texto, type(texto))
print("booleano:", booleano, type(booleano))

print("\n" + "-" * 40 + "\n")

# Conversões de tipo
print("Convertendo inteiro para string:", str(inteiro))
print("Convertendo string para inteiro:", int("100"))
print("Convertendo inteiro para float:", float(inteiro))
print("Convertendo booleano para inteiro:", int(False))

print("\n" + "-" * 40 + "\n")

# Estruturas de dados básicas
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30)
dicionario = {"nome": "Ana", "idade": 28}
conjunto = {1, 2, 2, 3}

print("Lista:", lista)
print("Tupla:", tupla)
print("Dicionário:", dicionario)
print("Conjunto:", conjunto)

print("Tipo de lista:", type(lista))
print("Tipo de dicionário:", type(dicionario))

print("\n" + "-" * 40 + "\n")

# Acesso a elementos
default = dicionario.get("peso", "Não informado")
print("Acesso em lista [2]:", lista[2])
print("Acesso em tupla [1]:", tupla[1])
print("Acesso em dicionário ['nome']:", dicionario["nome"])
print("Acesso com get em dicionário:", default)

print("\n" + "-" * 40 + "\n")

# Controle de fluxo if / elif / else
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")

nota = 7.5
if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
elif nota >= 5:
    conceito = "C"
else:
    conceito = "D"

print("Conceito:", conceito)

print("\n" + "-" * 40 + "\n")

# Laços for e while
print("Laço for")
for numero in lista:
    print(numero, end=" ")
print()

print("\nLaço for com range")
for i in range(5):
    print(i, end=" ")
print()

print("\nLaço while")
contador = 0
while contador < 5:
    print(contador, end=" ")
    contador += 1
print()

print("\n" + "-" * 40 + "\n")

# Controle de fluxo com break e continue
print("Uso de break")
for numero in lista:
    if numero == 3:
        print("Encontrado 3, saindo do loop")
        break
    print(numero)

print("\nUso de continue")
for numero in lista:
    if numero % 2 == 0:
        continue
    print("Ímpar:", numero)

print("\n" + "-" * 40 + "\n")

# Iteração sobre estrutura de dados
enumerate_lista = list(enumerate(lista))
print("Enumerate:", enumerate_lista)

print("Dicionário itens:")
for chave, valor in dicionario.items():
    print(f"{chave} = {valor}")

print("\n" + "-" * 40 + "\n")

# Unpacking e múltiplas atribuições
a, b, c = lista[0], lista[1], lista[2]
print("A, B, C:", a, b, c)

x, y, z = tupla
print("X, Y, Z:", x, y, z)

print("\n" + "-" * 40 + "\n")

# Expressões condicionais e funções simples
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)


def verifica_par(numero):
    return numero % 2 == 0

print("2 é par?", verifica_par(2))
print("3 é par?", verifica_par(3))

print("\nConteúdo concluído: tipos, estruturas de dados e fluxos de controle.")
