"""POO: Orientação a Objetos com Python (Parte 1)

Exemplos e explicações de POO em Python: classes, instâncias,
atributos, métodos, encapsulamento, propriedades, métodos de classe,
estáticos, herança, polimorfismo, métodos mágicos, composição e exercícios.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

print("# Conceitos básicos: Classe e Instância")
class Pessoa:
	especie = 'Homo sapiens'  # atributo de classe

	def __init__(self, nome: str, idade: int):
		self.nome = nome  # atributo de instância
		self.idade = idade

	def falar(self, texto: str) -> None:
		print(f"{self.nome} diz: {texto}")

p = Pessoa('Alice', 30)
print("Pessoa:", p.nome, p.idade, Pessoa.especie)
p.falar('Olá!')

print("\n" + "-"*40 + "\n")

print("# Encapsulamento e atributos privados (name mangling)")
class Conta:
	def __init__(self, titular: str, saldo: float = 0.0):
		self.titular = titular
		self._saldo = saldo  # convenção de 'protegido'
		self.__chave_privada = 'segredo'  # name mangling

	def deposito(self, valor: float):
		if valor <= 0:
			raise ValueError('Valor deve ser positivo')
		self._saldo += valor

	def saldo(self):
		return self._saldo

conta = Conta('Bruno', 100)
conta.deposito(50)
print('Saldo:', conta.saldo())
try:
	print(conta.__chave_privada)
except AttributeError:
	print('Atributo privado não acessível diretamente')

print("\n" + "-"*40 + "\n")

print("# Propriedades: getter, setter e deleter")
class Retangulo:
	def __init__(self, largura: float, altura: float):
		self._largura = largura
		self._altura = altura

	@property
	def largura(self):
		return self._largura

	@largura.setter
	def largura(self, val):
		if val <= 0:
			raise ValueError('Largura deve ser positiva')
		self._largura = val

	@property
	def area(self):
		return self._largura * self._altura

r = Retangulo(3, 4)
print('Área:', r.area)
try:
	r.largura = -1
except ValueError as e:
	print('Erro ao setar largura:', e)

print("\n" + "-"*40 + "\n")

print("# Métodos de classe e estáticos")
class PessoaUtil:
	contador = 0

	def __init__(self, nome: str):
		self.nome = nome
		PessoaUtil.contador += 1

	@classmethod
	def total_pessoas(cls):
		return cls.contador

	@staticmethod
	def eh_adulto(idade: int) -> bool:
		return idade >= 18

print('Total antes:', PessoaUtil.total_pessoas())
PessoaUtil('X')
PessoaUtil('Y')
print('Total depois:', PessoaUtil.total_pessoas())
print('Eh adulto 20?:', PessoaUtil.eh_adulto(20))

print("\n" + "-"*40 + "\n")

print("# Herança e polimorfismo")
class Animal:
	def __init__(self, nome: str):
		self.nome = nome

	def falar(self):
		raise NotImplementedError()

class Cachorro(Animal):
	def falar(self):
		return 'au au'

class Gato(Animal):
	def falar(self):
		return 'miau'

def faz_falar(a: Animal):
	print(f"{a.nome} -> {a.falar()}")

faz_falar(Cachorro('Rex'))
faz_falar(Gato('Mimi'))

print("\n" + "-"*40 + "\n")

print("# Métodos mágicos e representação")
class Vetor2D:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vetor2D(self.x + other.x, self.y + other.y)

	def __repr__(self):
		return f"Vetor2D(x={self.x}, y={self.y})"

v1 = Vetor2D(1,2)
v2 = Vetor2D(3,4)
print('Soma vetorial:', v1 + v2)

print("\n" + "-"*40 + "\n")

print("# Composição e agregação")
class Motor:
	def __init__(self, potencia):
		self.potencia = potencia

class Carro:
	def __init__(self, modelo: str, motor: Motor):
		self.modelo = modelo
		self.motor = motor  # composição/aggregação dependendo do ciclo de vida

motor = Motor(150)
carro = Carro('Fusca', motor)
print('Carro modelo:', carro.modelo, 'potencia motor:', carro.motor.potencia)

print("\n" + "-"*40 + "\n")

print("# Classe abstrata (ABC) e contrato")
class Forma(ABC):
	@abstractmethod
	def area(self):
		pass

class Circulo(Forma):
	def __init__(self, raio):
		self.raio = raio
	def area(self):
		return 3.1415 * self.raio * self.raio

print('Area circulo r=2:', Circulo(2).area())

print("\n" + "-"*40 + "\n")

print("# Dataclass como alternativa concisa")
@dataclass
class Produto:
	nome: str
	preco: float

p = Produto('Caneta', 1.5)
print('Produto dataclass:', p)

print("\n" + "-"*40 + "\n")

print("# __slots__ para economia de memória (quando apropriado)")
class Ponto:
	__slots__ = ('x','y')
	def __init__(self, x, y):
		self.x = x
		self.y = y

pt = Ponto(1,2)
print('Ponto com slots:', pt.x, pt.y)

print("\n" + "-"*40 + "\n")

print("# Boas práticas: pequenas dicas")
print("- Prefira composição a herança quando possível")
print("- Mantenha métodos pequenos e com responsabilidade única")
print("- Use dataclasses para modelos de dados simples")

print("\nExercícios propostos:")
print("1) Implemente uma classe Banco que gerencie várias `Conta` e permita transferências seguras")
print("2) Crie uma hierarquia de veículos com métodos específicos e teste polimorfismo")
print("3) Use dataclasses para modelar uma entidade e implemente comparação entre objetos")

