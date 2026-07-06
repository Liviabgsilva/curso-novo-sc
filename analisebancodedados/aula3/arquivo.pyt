"""Estrutura de Dados: Listas, Dicionários, Tuplas, Módulos e Pacotes (Parte 1)

Exemplos de uso em Python para cada um desses conceitos.
"""

# Listas: coleção ordenada e mutável
frutas = ["maçã", "banana", "laranja"]
print("Lista inicial:", frutas)

# Adicionar e remover itens
frutas.append("uva")
print("Após append:", frutas)
frutas.remove("banana")
print("Após remove:", frutas)

# Acessar por índice e fatiar
print("Primeira fruta:", frutas[0])
print("Últimas duas frutas:", frutas[-2:])

# Iterar sobre uma lista
for fruta in frutas:
    print("Fruta:", fruta)

print("\n" + "-" * 40 + "\n")

# Dicionários: coleção de pares chave-valor
aluno = {
    "nome": "João",
    "idade": 21,
    "curso": "Análise de Dados"
}
print("Dicionário inicial:", aluno)

# Inserir e atualizar valores
aluno["idade"] = 22
aluno["email"] = "joao@example.com"
print("Após atualizações:", aluno)

# Acessar valores
print("Nome do aluno:", aluno["nome"])
print("Chaves do dicionário:", list(aluno.keys()))
print("Valores do dicionário:", list(aluno.values()))

# Iterar em pares chave-valor
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("\n" + "-" * 40 + "\n")

# Tuplas: coleção ordenada e imutável
coordenadas = (10.123, -49.456)
print("Tupla de coordenadas:", coordenadas)
print("Latitude:", coordenadas[0])
print("Longitude:", coordenadas[1])

# Tentar modificar uma tupla causa erro, então usamos listas se precisamos alterar
try:
    coordenadas[0] = 11.0
except TypeError as error:
    print("Erro ao modificar tupla:", error)

print("\n" + "-" * 40 + "\n")

# Módulos: organizar funções em arquivos separados
# Em um projeto real, você criaria outro arquivo Python, por exemplo utils.py,
# e importaria as funções.

from meu_pacote import soma_lista, media_lista
from meu_pacote.strings import formata_titulo

valores = [10, 20, 30, 40]
print("Soma dos valores:", soma_lista(valores))
print("Média dos valores:", media_lista(valores))

print("\n" + "-" * 40 + "\n")

# Pacotes: pastas com módulos agrupados
# Um pacote real precisa de uma pasta com __init__.py.
# Exemplo real criado em aula3/meu_pacote:
#   meu_pacote/__init__.py
#   meu_pacote/calculos.py
#   meu_pacote/strings.py
#
# Agora usamos o pacote para importar funções e textos formatados.

titulo = formata_titulo("Pacote de Exemplo")
print(titulo)
print("O pacote funciona corretamente e agrupa módulos em uma estrutura limpa.")

print("\n" + "-" * 40 + "\n")
print("Este arquivo demonstra:")
print("- Listas")
print("- Dicionários")
print("- Tuplas")
print("- Módulos (funções reutilizáveis)")
print("- Pacotes (estrutura de pastas para módulos)")
