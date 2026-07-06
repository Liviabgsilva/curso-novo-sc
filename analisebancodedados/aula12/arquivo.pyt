"""POO: Orientação a Objetos com Python (Parte 2)

Conteúdo avançado complementar ao Parte 1: padrões de projeto simples,
mixins, múltipla herança e MRO, descriptors, metaclasses, operator overloading,
serialização, copy/equality, thread-safety, context managers em objetos e
boas práticas de design (SOLID aplicados em Python).
"""

import json
import pickle
from dataclasses import dataclass, field
from functools import wraps
from threading import Lock, Thread
import copy
from typing import Any

print("# Mixins e composição versus herança")
class ToJsonMixin:
	def to_json(self):
		return json.dumps(self.__dict__)

class TimestampMixin:
	def timestamp(self):
		import time
		return time.time()

class Mensagem(ToJsonMixin, TimestampMixin):
	def __init__(self, texto):
		self.texto = texto

msg = Mensagem('Olá')
print('Mensagem JSON:', msg.to_json())
print('Timestamp:', msg.timestamp())

print("\n" + "-"*40 + "\n")

print("# Múltipla herança e MRO (method resolution order)")
class A:
	def quem(self):
		return 'A'

class B(A):
	def quem(self):
		return 'B'

class C(A):
	def quem(self):
		return 'C'

class D(B, C):
	pass

print('MRO D:', [c.__name__ for c in D.__mro__])
print('D.quem():', D().quem())

print("\n" + "-"*40 + "\n")

print("# Descriptors: controlando acesso a atributos")
class Positive:
	def __init__(self, name='var'):
		self.name = name

	def __get__(self, instance, owner):
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if value < 0:
			raise ValueError('Must be non-negative')
		instance.__dict__[self.name] = value

class Produto:
	preco = Positive('preco')

	def __init__(self, preco):
		self.preco = preco

p = Produto(10)
print('Preco OK:', p.preco)
try:
	p.preco = -5
except ValueError as e:
	print('Descriptor impediu valor inválido:', e)

print("\n" + "-"*40 + "\n")

print("# Metaclasses: criar classes com comportamento customizado")
class NomeMensagemMeta(type):
	def __new__(mcls, name, bases, namespace):
		namespace['tipo'] = name.lower()
		return super().__new__(mcls, name, bases, namespace)

class MensagemBase(metaclass=NomeMensagemMeta):
	pass

class Alerta(MensagemBase):
	pass

print('Alerta.tipo via metaclass:', Alerta.tipo)

print("\n" + "-"*40 + "\n")

print("# Operator overloading e protocolos de comparação")
class Fracao:
	def __init__(self, num, den=1):
		self.num = num
		self.den = den

	def __add__(self, other):
		return Fracao(self.num*other.den + other.num*self.den, self.den*other.den)

	def __repr__(self):
		return f"{self.num}/{self.den}"

f1 = Fracao(1,2)
f2 = Fracao(1,3)
print('Soma de fracoes:', f1 + f2)

print("\n" + "-"*40 + "\n")

print("# Serialização: JSON e Pickle")
obj = {'a':1, 'b':2}
js = json.dumps(obj)
print('JSON:', js)
pk = pickle.dumps(obj)
print('Pickle bytes length:', len(pk))

print("\n" + "-"*40 + "\n")

print("# Copy protocol: shallow vs deep and implementando __copy__/__deepcopy__")
class Nodo:
	def __init__(self, valor, filho=None):
		self.valor = valor
		self.filho = filho

	def __repr__(self):
		return f"Nodo({self.valor})"

node = Nodo(1, Nodo(2))
sh = copy.copy(node)
dp = copy.deepcopy(node)
node.filho.valor = 99
print('Original filho:', node.filho)
print('Shallow filho (refletiu):', sh.filho)
print('Deep filho (independente):', dp.filho)

print("\n" + "-"*40 + "\n")

print("# Thread-safety: locks em atributos compartilhados")
class ContaSegura:
	def __init__(self, saldo=0):
		self.saldo = saldo
		self._lock = Lock()

	def saque(self, valor):
		with self._lock:
			if self.saldo >= valor:
				self.saldo -= valor
				return True
			return False

conta = ContaSegura(1000)
def correntista():
	for _ in range(1000):
		conta.saque(1)

threads = [Thread(target=correntista) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print('Saldo após saques concorrentes (thread-safe):', conta.saldo)

print("\n" + "-"*40 + "\n")

print("# Context manager em objetos (com __enter__/__exit__)")
class Recurso:
	def __enter__(self):
		print('Abrindo recurso')
		return self
	def __exit__(self, exc_type, exc, tb):
		print('Fechando recurso')
		return False

with Recurso() as r:
	print('Usando recurso')

print("\n" + "-"*40 + "\n")

print("# Equality e hashing: __eq__ e __hash__ para objetos imutáveis")
@dataclass(frozen=True)
class Coordenada:
	x: int
	y: int

co1 = Coordenada(1,2)
co2 = Coordenada(1,2)
print('co1 == co2:', co1 == co2)
print('set with coords:', {co1, co2})

print("\n" + "-"*40 + "\n")

print("# Boas práticas SOLID (resumo aplicável a Python)")
print("S - Single Responsibility: classes pequenas e coesas")
print("O - Open/Closed: estender via herança/composição, não modificar classes existentes")
print("L - Liskov Substitution: subclasses substituem a base sem quebrar contrato")
print("I - Interface Segregation: prefira várias interfaces pequenas (Protocols) ")
print("D - Dependency Inversion: dependa de abstrações (Protocol) não de implementações")

print("\nExercícios propostos:")
print("1) Implemente um pattern Factory para criar diferentes tipos de `Produto`")
print("2) Escreva um descriptor que valide tipos em tempo de atribuição")
print("3) Modele um pequeno sistema com múltiplas threads e proteja recursos compartilhados")

