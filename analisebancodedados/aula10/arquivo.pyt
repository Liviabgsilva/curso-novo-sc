"""Programação Funcional e Lidando com Erros de Programação (Parte 2)

Conteúdo complementar à Parte 1: corrotinas baseadas em geradores, uso de
`contextlib` avançado (`suppress`, `ExitStack`), padrões de retry e backoff,
circuit breaker simples, `dataclasses` imutáveis, validação funcional,
uso de `typing.Callable` e `Protocol`, e técnicas de teste e depuração.
"""

from contextlib import suppress, ExitStack, contextmanager
from dataclasses import dataclass
from functools import wraps
from typing import Callable, Protocol
import time
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('aula10')

print("# CORROTINAS E GERADORES QUE RECEBEM VALORES (coroutines)")
def coro_print():
	print("Iniciando coro_print")
	try:
		while True:
			msg = (yield)
			print("Recebido na coro:", msg)
	except GeneratorExit:
		print("Corrotina fechada")

g = coro_print()
next(g)  # inicializa
g.send("Olá")
g.send("Teste")
g.close()

print("\n" + "-"*40 + "\n")

print("# CONTEXTLIB: suppress e ExitStack")
with suppress(FileNotFoundError):
	open('não_existe_2.txt', 'r')

with ExitStack() as stack:
	files = [stack.enter_context(open(__file__, 'r', encoding='utf-8'))]
	print("Arquivo atual aberto via ExitStack");

print("\n" + "-"*40 + "\n")

print("# RETRY DECORATOR com backoff exponencial")
def retry(max_attempts=3, base_delay=0.1):
	def deco(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			delay = base_delay
			for attempt in range(1, max_attempts+1):
				try:
					return func(*args, **kwargs)
				except Exception as e:
					logger.warning(f"Tentativa {attempt} falhou: {e}")
					if attempt == max_attempts:
						raise
					time.sleep(delay)
					delay *= 2
		return wrapper
	return deco

@retry(max_attempts=4, base_delay=0.05)
def talvez_falhe(prob=0.7):
	if random.random() < prob:
		raise RuntimeError("falha aleatória")
	return "sucesso"

try:
	print("Resultado talvez_falhe:", talvez_falhe(0.9))
except RuntimeError as e:
	print("Método realmente falhou após retries:", e)

print("\n" + "-"*40 + "\n")

print("# CIRCUIT BREAKER SIMPLES")
class CircuitBreaker:
	def __init__(self, max_failures=3, reset_time=5):
		self.max_failures = max_failures
		self.reset_time = reset_time
		self.failures = 0
		self.opened_at = None

	def call(self, func: Callable, *args, **kwargs):
		if self.opened_at and (time.time() - self.opened_at) < self.reset_time:
			raise RuntimeError("Circuit open - operação bloqueada")
		try:
			result = func(*args, **kwargs)
			self.failures = 0
			return result
		except Exception:
			self.failures += 1
			if self.failures >= self.max_failures:
				self.opened_at = time.time()
			raise

cb = CircuitBreaker(max_failures=2, reset_time=2)
def flaky():
	if random.random() < 0.8:
		raise RuntimeError('flaky')
	return 'ok'

for i in range(4):
	try:
		print(cb.call(flaky))
	except Exception as e:
		print('Call failed:', e)
	time.sleep(0.5)

print("\n" + "-"*40 + "\n")

print("# DADOS IMUTÁVEIS e dataclasses frozen")
@dataclass(frozen=True)
class Usuario:
	nome: str
	idade: int

u = Usuario('Lara', 27)
print("Usuario imutável:", u)

print("\n" + "-"*40 + "\n")

print("# Typing avançado: Callable e Protocol")
class Transformer(Protocol):
	def __call__(self, x: int) -> int: ...

def aplica_transformer(t: Transformer, v: int) -> int:
	return t(v)

def dobra(x: int) -> int: return x*2
print("aplica_transformer(dobra,5):", aplica_transformer(dobra,5))

print("\n" + "-"*40 + "\n")

print("# Validação funcional: retornando Result-like tuples")
from typing import Tuple, Any

def valida_nome(nome: str) -> Tuple[bool, Any]:
	if not nome:
		return (False, "Nome vazio")
	return (True, nome.strip())

ok, value = valida_nome('  Pedro  ')
print(ok, value)

print("\n" + "-"*40 + "\n")

print("# Testes e debug: asserts, doctest e dicas de unit test")
def soma(a: int, b: int) -> int:
	"""Soma dois números.

	>>> soma(2,3)
	5
	"""
	return a + b

assert soma(2,3) == 5
print("Exemplo doctest/asserção OK")

print("\nConteúdo Parte 2 criado: tópicos funcionais e padrões de tratamento de erro.")

