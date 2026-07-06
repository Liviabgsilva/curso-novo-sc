"""Estrutura de Dados: Listas, Dicionários, Tuplas, Módulos e Pacotes
Conteúdo mais completo sobre o assunto, complementando a aula 3.
"""

from collections import namedtuple
from estrutura import (
    atualiza_dicionario,
    cria_aluno,
    descompacta_tupla,
    lista_comprehension,
    lista_quadrados,
    soma_notas,
    tupla_chaves,
)

# ------- LISTAS avançadas -------
print("# LISTAS")
idades = [25, 18, 30, 22, 19]
print("Lista original:", idades)

# Adicionar, inserir e estender
idades.append(27)
idades.insert(2, 29)
idades.extend([35, 40])
print("Após append, insert e extend:", idades)

# Remover, extrair e limpar
idade_removida = idades.pop(1)
print("Removido com pop:", idade_removida)
idades.remove(30)
print("Após remove:", idades)
print("Quantidade de elementos:", len(idades))

# Copiar e ordenar sem alterar o original
idades_copia = idades.copy()
idades_ordenadas = sorted(idades_copia)
print("Cópia ordenada:", idades_ordenadas)
print("Original continua:", idades)

# Contagem, índice e reversing
print("Quantidade de 22 na lista:", idades.count(22))
print("Índice de 19:", idades.index(19))
idades.reverse()
print("Em ordem reversa:", idades)
idades.reverse()

# Fatias com passo e sublistas
print("Fatia de 2 em 2:", idades[::2])
print("Últimos 3 elementos:", idades[-3:])

# Lista de listas (estrutura aninhada)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matriz)
print("Elemento [1][2]:", matriz[1][2])

# List comprehension
quadrados = [x ** 2 for x in range(1, 11)]
print("Quadrados de 1 a 10:", quadrados)
pares = [x for x in range(1, 21) if x % 2 == 0]
print("Números pares:", pares)

# Uso como pilha e fila
pilha = []
pilha.append("primeiro")
pilha.append("segundo")
pilha.append("terceiro")
print("Pilha antes do pop:", pilha)
print("Retirado da pilha:", pilha.pop())

from collections import deque
fila = deque(["a", "b", "c"])
fila.append("d")
print("Fila antes de popleft:", list(fila))
print("Retirado da fila:", fila.popleft())

print("\n" + "-" * 50 + "\n")

# ------- DICIONÁRIOS avançados -------
print("# DICIONÁRIOS")
produto = {"nome": "Notebook", "preco": 3500.0, "estoque": 10}
print("Dicionário inicial:", produto)

# Acessar com get e setdefault
print("Marca:", produto.get("marca", "Marca não informada"))
produto.setdefault("marca", "Marca Padrão")
print("Após setdefault:", produto)

# Atualizar valores e mesclar dicionários
produto_atualizado = {"preco": 3300.0, "estoque": 8}
produto.update(produto_atualizado)
print("Após update:", produto)

# Remoção segura
ultimo_item = produto.popitem()
print("Item removido com popitem:", ultimo_item)
produto["categoria"] = "Eletrônicos"
print("Após popitem e nova chave:", produto)

# Dicionário aninhado
turma = {
    "aluno1": {"nome": "Ana", "nota": 8.5},
    "aluno2": {"nome": "Bruno", "nota": 9.0},
}
print("Turma aninhada:", turma)
print("Nota do aluno1:", turma["aluno1"]["nota"])

# Comprehension de dicionário
quadrados_dict = {x: x ** 2 for x in range(1, 6)}
print("Dicionário de quadrados:", quadrados_dict)

# Usar tuplas como chave de dicionário
pontos = {(10, 20): "A", (0, 0): "Origem"}
print("Dicionário com tupla como chave:", pontos)

print("\n" + "-" * 50 + "\n")

# ------- TUPLAS avançadas -------
print("# TUPLAS")
coordenadas = (3.5, 7.2)
print("Tupla inicial:", coordenadas)

# Descompactação e atribuição múltipla
x, y = coordenadas
print(f"x={x}, y={y}")

# Tuplas aninhadas
agenda = (("Maria", 28), ("Carlos", 35), ("Lúcia", 22))
print("Agenda de tuplas:", agenda)

# Tuple como chave imutável
agenda_dict = {("Maria",): "Atendida", ("Carlos",): "Pendente"}
print("Agenda com tupla como chave:", agenda_dict)

# namedtuple para registro com nomes de campos
Pessoa = namedtuple("Pessoa", ["nome", "idade", "cidade"])
p1 = Pessoa("Fábio", 31, "Recife")
print("NamedTuple Pessoa:", p1)
print("Nome via namedtuple:", p1.nome)

print("\n" + "-" * 50 + "\n")

# ------- MÓDULOS e PACOTES -------
print("# MÓDULOS e PACOTES")

# Importar funções de um pacote real criado em aula4/estrutura
print("Quadrados do pacote:", lista_quadrados([1, 2, 3, 4, 5]))
print("Lista compreensiva do pacote:", lista_comprehension([1, 2, 3, 4, 5, 6]))

aluno = cria_aluno("Carla", 23, "Ciência de Dados")
print("Aluno criado via módulo:", aluno)
print("Soma de notas via módulo:", soma_notas({"prova1": 8.5, "prova2": 9.0}))

print(atualiza_dicionario(aluno, email="carla@email.com", curso="DA"))
print(descompacta_tupla((15, 25)))
print("Dicionário com tupla-chave do pacote:", tupla_chaves())

# Explicação de pacotes
# Um pacote é uma pasta com __init__.py que reúne vários módulos.
# O arquivo __init__.py permite que o pacote seja importado como um único módulo,
# e também pode expor funções e classes para uso externo.

# Exemplo de importação:
# from estrutura import lista_quadrados
# from estrutura.listas import filtra_strings

print("Conteúdo avançado de listas, dicionários, tuplas, módulos e pacotes concluído.")
