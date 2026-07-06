"""Ampliando Conhecimento de Estruturas de Dados e Fluxos de Controle (Parte 1)

Conteúdo focado em técnicas práticas e exercícios: uso de `zip`, `enumerate`,
`all`/`any`, `itertools`, `match-case` (pattern matching), técnicas de
iteração eficientes, dicas de complexidade e pequenos exercícios práticos.
"""

from itertools import permutations, combinations, chain, islice
from time import perf_counter

print("# ZIP e ENUMERATE")
nomes = ["Ana", "Bruno", "Carlos"]
notas = [8.5, 7.0, 9.0]

for nome, nota in zip(nomes, notas):
	print(f"{nome} teve nota {nota}")

for idx, nome in enumerate(nomes, start=1):
	print(f"{idx} - {nome}")

print("\n" + "-"*40 + "\n")

print("# all / any")
valores = [2, 4, 6, 8]
print("Todos pares?", all(x%2==0 for x in valores))
print("Algum ímpar?", any(x%2!=0 for x in valores))

print("\n" + "-"*40 + "\n")

print("# itertools: combinações e permutações")
items = ['A','B','C']
print("permutations:", list(permutations(items, 2)))
print("combinations:", list(combinations(items, 2)))
print("chain example:", list(chain([1,2],[3,4])))

print("\n" + "-"*40 + "\n")

print("# Pattern matching (match-case) - Python 3.10+")
def classifica(valor):
	match valor:
		case 0:
			return "zero"
		case 1 | 2:
			return "um ou dois"
		case [x, y]:
			return f"lista com dois elementos: {x}, {y}"
		case {'chave': v}:
			return f"dicionário com chave: {v}"
		case _:
			return "outro"

print(classifica(0))
print(classifica(2))
print(classifica([10,20]))
print(classifica({'chave': 'valor'}))

print("\n" + "-"*40 + "\n")

print("# Táticas de iteração eficientes")
def soma_iter(it):
	s = 0
	for x in it:
		s += x
	return s

N = 1_000_00
lista = list(range(N))
t0 = perf_counter(); s1 = sum(lista); t1 = perf_counter()
t_sum = t1 - t0
t0 = perf_counter(); s2 = soma_iter(iter(lista)); t1 = perf_counter()
t_loop = t1 - t0
print(f"sum built-in: {t_sum:.6f}s, loop: {t_loop:.6f}s")

print("\n" + "-"*40 + "\n")

print("# Exercícios curtos")

print("Ex 1: Dado duas listas, crie um dicionário com zip (nome->nota)")
def ex1(nomes, notas):
	return {n: p for n, p in zip(nomes, notas)}

print(ex1(nomes, notas))

print("Ex 2: Encontre o par com maior soma em uma lista de inteiros")
def ex2(lista):
	best = None
	for a, b in combinations(lista, 2):
		s = a + b
		if best is None or s > best[0]:
			best = (s, (a, b))
	return best

print(ex2([1,5,3,9,2]))

print("\n" + "-"*40 + "\n")

print("# Exercício 3: verificação de palíndromo (usando slicing e iterator)")
def is_palindrome(s: str) -> bool:
	s = ''.join(ch.lower() for ch in s if ch.isalnum())
	return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("python"))

print("\n" + "-"*40 + "\n")

print("# Pequenas dicas de complexidade")
print("- Usar set para membership test é O(1) médio")
print("- List concatenation é O(n); prefer append + join para strings")
print("- Evite operações dentro de loops quando possível pré-computar")

print("\nConteúdo Parte 1 criado: exemplos, dicas e exercícios curtos.")

