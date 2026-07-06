"""Ampliando Conhecimento de Estruturas de Dados e Fluxos de Controle (Parte 2)

Este arquivo completa os tópicos da Parte 1 com utilitários e técnicas úteis
para manipulação eficiente de dados e controle de fluxo: `heapq`, `bisect`,
`itertools.groupby`, `itertools.accumulate`, `functools.lru_cache`, profiling,
`asyncio` básico, `threading`/`concurrent.futures`, `array`/`memoryview`, e dicas
de performance com `timeit`.
"""

print("# heapq - fila de prioridade (min-heap)")
import heapq

heap = []
for val in [5, 1, 3, 2, 4]:
	heapq.heappush(heap, val)

print("Heap ordenado (pop):", [heapq.heappop(heap) for _ in range(len(heap))])

print("\n" + "-"*40 + "\n")

print("# bisect - inserir mantendo ordenação")
import bisect

arr = [1,3,4,7]
bisect.insort(arr, 5)
print("Após insort:", arr)
pos = bisect.bisect_left(arr, 4)
print("Posição de inserção (left) para 4:", pos)

print("\n" + "-"*40 + "\n")

print("# itertools: groupby e accumulate")
from itertools import groupby, accumulate

data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('C', 5)]
for key, group in groupby(data, key=lambda x: x[0]):
	print(key, list(group))

nums = [1,2,3,4]
print("accumulate:", list(accumulate(nums)))

print("\n" + "-"*40 + "\n")

print("# functools.lru_cache - memoização simples")
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

print("fib(30):", fib(30))

print("\n" + "-"*40 + "\n")

print("# array module e memoryview para dados binários eficientes")
import array
arr = array.array('i', range(5))
mv = memoryview(arr)
print("Array original:", arr.tolist())
mv[0] = 99
print("Array após memoryview alteração:", arr.tolist())

print("\n" + "-"*40 + "\n")

print("# threading vs concurrent.futures (exemplo simples)")
import threading
from concurrent.futures import ThreadPoolExecutor

def tarefa(n):
	return n * n

with ThreadPoolExecutor(max_workers=4) as ex:
	resultados = list(ex.map(tarefa, range(10)))

print("ThreadPoolExecutor resultados:", resultados)

print("\n" + "-"*40 + "\n")

print("# asyncio - coroutine simples")
import asyncio

async def hello(n):
	await asyncio.sleep(0)
	return f'hello {n}'

async def run_async():
	tasks = [hello(i) for i in range(3)]
	return await asyncio.gather(*tasks)

res = asyncio.run(run_async())
print("asyncio results:", res)

print("\n" + "-"*40 + "\n")

print("# timeit e profiling básicos")
import timeit

code1 = "sum(range(1000))"
code2 = "s=0\nfor i in range(1000): s+=i"
print("timeit sum():", timeit.timeit(code1, number=1000))
print("timeit loop:", timeit.timeit(code2, number=1000))

print("\n(Para profiling mais detalhado, use cProfile em scripts maiores.)")

print("\n" + "-"*40 + "\n")

print("# heapq como fila de prioridade com tuplas (prioridade, item)")
pq = []
items = [(2,'tarefa baixa'), (0,'tarefa critica'), (1,'tarefa media')]
for p, item in items:
	heapq.heappush(pq, (p, item))

while pq:
	p, item = heapq.heappop(pq)
	print(f"Processando {item} com prioridade {p}")

print("\n" + "-"*40 + "\n")

print("# Exercícios práticos")

print("Ex 1: Dado uma lista ordenada, insira um valor mantendo ordem usando bisect")
def insert_sorted(lst, value):
	bisect.insort(lst, value)
	return lst

print(insert_sorted([1,3,5,7], 4))

print("Ex 2: Usando groupby, agregue soma por chave")
def aggregate_sum(data):
	result = {}
	for key, group in groupby(sorted(data, key=lambda x: x[0]), key=lambda x: x[0]):
		result[key] = sum(item[1] for item in group)
	return result

print(aggregate_sum([('A',1),('B',2),('A',3)]))

print("\nConteúdo Parte 2 criado: tópicos complementares adicionados.")

