"""Tipos, Estruturas de Dados e Fluxos de Controle (Parte 2)

Conteúdo complementar e avançado cobrindo conceitos que não foram detalhados
na Parte 1: strings avançadas, conjuntos, compreensões, funções de ordem
superior, geradores, cópias, exceções, context managers, decorators,
recursão, dataclasses, file I/O, logging e exemplos práticos.
"""

# ----------------- STRINGS AVANÇADAS -----------------
texto = "  Olá, Mundo! Bem-vindo ao curso de Análise de Dados.  "
print("Original:", repr(texto))

print("lower():", texto.lower())
print("upper():", texto.upper())
print("strip():", texto.strip())
print("split():", texto.strip().split())
print("join():", "-".join(["a","b","c"]))
print("replace():", texto.replace("Mundo", "Python"))
print("contains 'curso':", "curso" in texto)

# f-strings e formatação
nome = "Mariana"
pontuacao = 9.5
print(f"Aluno: {nome}, nota: {pontuacao:.1f}")

print("\n" + "-"*40 + "\n")

# ----------------- SETS (CONJUNTOS) -----------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("A union B:", a | b)
print("A intersection B:", a & b)
print("A difference B:", a - b)
print("A symmetric_difference B:", a ^ b)
print("isdisjoint:", a.isdisjoint({7,8}))
print("issubset/issuperset:", {1,2}.issubset(a), a.issuperset({1,2}))

print("\n" + "-"*40 + "\n")

# ----------------- DICIONÁRIOS AVANÇADOS -----------------
from collections import defaultdict, Counter, OrderedDict

# defaultdict facilita valores padrão
dd = defaultdict(list)
dd['chave'].append(1)
print("defaultdict:", dd)

# Counter para contagens rápidas
c = Counter(['maçã','banana','maçã','uva','banana','maçã'])
print("Counter mais comuns:", c.most_common(2))

# Ordenação com key
produtos = [{'nome':'A', 'preco':10}, {'nome':'B','preco':5}, {'nome':'C','preco':20}]
print("Ordenado por preco:", sorted(produtos, key=lambda p: p['preco']))

print("\n" + "-"*40 + "\n")

# ----------------- COMPREHENSIONS AVANÇADAS -----------------
lista = list(range(10))
pares = [x for x in lista if x % 2 == 0]
quadrados = {x: x**2 for x in lista}
conjunto = {x for x in lista if x % 3 == 0}
print("pares:", pares)
print("quadrados dict:", quadrados)
print("multiples of 3:", conjunto)

print("\n" + "-"*40 + "\n")

# ----------------- MAP / FILTER / REDUCE -----------------
from functools import reduce

dobro = list(map(lambda x: x*2, lista))
filtrados = list(filter(lambda x: x%2==0, lista))
somados = reduce(lambda a,b: a+b, lista)
print("map dobro:", dobro)
print("filter pares:", filtrados)
print("reduce soma:", somados)

print("\n" + "-"*40 + "\n")

# ----------------- LAMBDAS E FUNÇÕES DE ORDEM SUPERIOR -----------------
def aplicar(func, valores):
	return [func(v) for v in valores]

print("aplicar lambda:", aplicar(lambda x: x+1, [1,2,3]))

def multiplicador(n):
	def mult(x):
		return x * n
	return mult

duplica = multiplicador(2)
print("duplica(5):", duplica(5))

print("\n" + "-"*40 + "\n")

# ----------------- GERADORES E ITERADORES -----------------
def gera_pares(n):
	for i in range(n):
		if i % 2 == 0:
			yield i

g = gera_pares(10)
print("generator next:", next(g))
print("generator restante:", list(g))

# generator expression
gen_expr = (x*x for x in range(5))
print("gen expression:", list(gen_expr))

class Contador:
	def __init__(self, n):
		self.n = n
		self.i = 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.i < self.n:
			v = self.i
			self.i += 1
			return v
		raise StopIteration

print("Contador custom:", list(Contador(5)))

print("\n" + "-"*40 + "\n")

# ----------------- CÓPIA: SHALLOW vs DEEP -----------------
import copy
original = [[1,2],[3,4]]
shallow = list(original)
deep = copy.deepcopy(original)
original[0].append(99)
print("original after mutate:", original)
print("shallow reflects change:", shallow)
print("deep copy independent:", deep)

print("\n" + "-"*40 + "\n")

# ----------------- EXCEÇÕES E CONTEXTO -----------------
try:
	x = 1 / 0
except ZeroDivisionError as e:
	print("Erro capturado:", e)
finally:
	print("Finally executado")

class MeuErro(ValueError):
	pass

def verifica_positivo(n):
	if n < 0:
		raise MeuErro("Número negativo não permitido")
	return True

try:
	verifica_positivo(-1)
except MeuErro as e:
	print("MeuErro capturado:", e)

from contextlib import contextmanager

@contextmanager
def abre_arquivo(path, modo='w'):
	f = open(path, modo, encoding='utf-8')
	try:
		yield f
	finally:
		f.close()

with abre_arquivo('temp_output.txt','w') as f:
	f.write('Exemplo de context manager\n')

print("Arquivo escrito: temp_output.txt")

print("\n" + "-"*40 + "\n")

# ----------------- FUNÇÕES AVANÇADAS: *args, **kwargs, docstrings -----------------
def soma(*args):
	"""Soma uma quantidade arbitrária de números."""
	return sum(args)

def configura(**kwargs):
	return kwargs

print("soma variadic:", soma(1,2,3,4))
print("configura:", configura(timeout=30, debug=True))

print("\n" + "-"*40 + "\n")

# ----------------- DECORATORS SIMPLES -----------------
import time

def timer(func):
	def wrapper(*args, **kwargs):
		t0 = time.time()
		res = func(*args, **kwargs)
		t1 = time.time()
		print(f"{func.__name__} demorou {t1-t0:.6f}s")
		return res
	return wrapper

@timer
def espera(n):
	time.sleep(n)
	return 'done'

print("Chamada de função decorada:", espera(0.01))

print("\n" + "-"*40 + "\n")

# ----------------- RECURSÃO -----------------
def fatorial(n):
	if n <= 1:
		return 1
	return n * fatorial(n-1)

print("fatorial(5):", fatorial(5))

print("\n" + "-"*40 + "\n")

# ----------------- DATACLASSES -----------------
from dataclasses import dataclass

@dataclass
class Pessoa:
	nome: str
	idade: int

p = Pessoa('Rafael', 29)
print("Dataclass Pessoa:", p)

print("\n" + "-"*40 + "\n")

# ----------------- TYPING BÁSICO -----------------
from typing import List, Dict, Tuple

def media(nums: List[float]) -> float:
	return sum(nums) / len(nums)

print("media typing:", media([1.0,2.0,3.0]))

print("\n" + "-"*40 + "\n")

# ----------------- FILE I/O -----------------
with open('exemplo_io.txt','w', encoding='utf-8') as f:
	f.write('Linha1\nLinha2\n')

with open('exemplo_io.txt','r', encoding='utf-8') as f:
	conteudo = f.read()
print("Conteúdo de exemplo_io.txt:\n", conteudo)

print("\n" + "-"*40 + "\n")

# ----------------- LOGGING BÁSICO -----------------
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('aula6')
logger.info('Mensagem de informação do logger')

print("\n" + "-"*40 + "\n")

# ----------------- ASSERT E TESTES SIMPLES -----------------
assert soma(1,2,3) == 6, "Soma está incorreta"
print("Asserção OK")

print("\nConteúdo da Parte 2 concluído: itens avançados adicionados.")

