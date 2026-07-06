"""NumPy: Objetos, Vetorização e Fundamentos da Estatística

Exemplos práticos cobrindo:
- criação de arrays e dtypes
- shape, reshape, broadcasting e vetorização
- indexing, slicing e boolean masking
- ufuncs, reduce, accumulate, einsum
- performance, views vs copies, memory layout
- estatística descritiva com NumPy (mean, var, std, percentiles)
- amostragem, distribuições e demonstração do TCL

Execute este arquivo com uma instalação Python que tenha `numpy`.
"""

import numpy as np
import math

print('# NumPy - criação e tipos')
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1.0, 2.0, 3.0])
arr3 = np.zeros((2,3), dtype=np.float64)
arr4 = np.arange(0, 10, 2)
arr5 = np.linspace(0, 1, 5)
print('arr1:', arr1, 'dtype:', arr1.dtype)
print('arr3 shape:', arr3.shape)
print('arr4:', arr4)
print('arr5:', arr5)

print('\n' + '-'*40 + '\n')

print('# Shape, reshape e transposição')
a = np.arange(12)
print('original:', a)
a2 = a.reshape((3,4))
print('reshape 3x4:\n', a2)
print('transpose:\n', a2.T)

print('\n' + '-'*40 + '\n')

print('# Broadcasting e vetorização')
M = np.arange(12).reshape(3,4)
v = np.array([1, 0, 1, 0])
print('M:\n', M)
print('v:', v)
print('M + v broadcasts across rows:\n', M + v)

# operações element-wise são muito rápidas
print('sqrt vectorized:', np.sqrt(M))
print('sum axis=0:', M.sum(axis=0))

print('\n' + '-'*40 + '\n')

print('# Indexing avançado e boolean masking')
arr = np.array([10, 15, 20, 25, 30])
mask = arr > 18
print('arr[mask]:', arr[mask])
arr[arr % 20 == 0] = -1
print('modified arr:', arr)

print('\n' + '-'*40 + '\n')

print('# Fancy indexing (advanced integer indexing)')
X = np.arange(16).reshape(4,4)
rows = np.array([0,2])
cols = np.array([1,3])
print('select rows,cols diagonal-like:', X[rows[:,None], cols])

print('\n' + '-'*40 + '\n')

print('# Views vs Copies (important for memory/performance)')
orig = np.arange(6)
view = orig.reshape(2,3)
slice_view = orig[1:4]
copy_arr = orig.copy()
orig[2] = 99
print('orig after change:', orig)
print('view reflects change:', view)
print('slice reflects change:', slice_view)
print('copy independent:', copy_arr)

print('\n' + '-'*40 + '\n')

print('# Memory layout: C vs F order')
arr_c = np.arange(12).reshape(3,4)
arr_f = np.asfortranarray(arr_c)
print('C-contiguous:', arr_c.flags['C_CONTIGUOUS'], 'F-contiguous:', arr_f.flags['F_CONTIGUOUS'])

print('\n' + '-'*40 + '\n')

print('# Universal functions (ufuncs), reduce, accumulate, outer')
print('add ufunc:', np.add(arr1, 10))
print('multiply reduce:', np.multiply.reduce([1,2,3,4]))
print('add accumulate:', np.add.accumulate([1,2,3,4]))
print('outer:', np.multiply.outer([1,2,3], [3,4]))

print('\n' + '-'*40 + '\n')

print('# einsum: compacto e rápido para produtos/contruições')
A = np.arange(6).reshape(2,3)
B = np.arange(6).reshape(3,2)
print('A einsum B (matrix multiply) =', np.einsum('ik,kj->ij', A, B))

print('\n' + '-'*40 + '\n')

print('# Estruturas para dados heterogêneos: structured arrays')
dtype = np.dtype([('nome', 'U10'), ('idade', 'i4'), ('salario', 'f8')])
data = np.array([('Ana', 30, 5000.0), ('Bruno', 25, 4200.5)], dtype=dtype)
print('structured:', data)
print('idade coluna:', data['idade'])

print('\n' + '-'*40 + '\n')

print('# Estatística descritiva básica com NumPy')
rng = np.random.default_rng(0)
vals = rng.normal(loc=50, scale=10, size=1000)
print('mean:', vals.mean())
print('median:', np.median(vals))
print('std:', vals.std(ddof=0))
print('variance:', vals.var())
print('percentiles (25,50,75):', np.percentile(vals, [25,50,75]))

print('\n' + '-'*40 + '\n')

print('# Covariância e correlação (matrizes)')
X = rng.normal(size=(100,3))
cov = np.cov(X, rowvar=False)
corr = np.corrcoef(X, rowvar=False)
print('cov shape:', cov.shape)
print('corr shape:', corr.shape)

print('\n' + '-'*40 + '\n')

print('# Sampling e distribuições: numpy.random')
print('binomial n=10 p=0.5 sample 10:', rng.binomial(10,0.5, size=10))
print('poisson lambda 3 sample 10:', rng.poisson(3, size=10))

print('\n' + '-'*40 + '\n')

print('# Central Limit Theorem (demonstração simples)')
def clt_demo(sample_size=1000, trials=5000):
	means = [rng.exponential(scale=1.0, size=sample_size).mean() for _ in range(trials)]
	means = np.array(means)
	return means

means = clt_demo(sample_size=100, trials=1000)
print('CLT sample means mean/std:', means.mean(), means.std())

print('\n' + '-'*40 + '\n')

print('# Performance tip: prefer vectorized ops a loops')
big = rng.integers(0, 100, size=1_000_000)
py_sum = sum([int(x) for x in big])  # slower Python loop (force cast)
np_sum = big.sum()
print('np_sum:', np_sum, 'py_sum (same):', py_sum)

print('\n' + '-'*40 + '\n')

print('# IO: salvar e carregar arrays')
np.save('exemplo_array.npy', big)
loaded = np.load('exemplo_array.npy')
print('saved and loaded shape:', loaded.shape)

print('\n' + '-'*40 + '\n')

print('Exercícios propostos:')
print('1) Reescreva uma função que soma linhas de uma matriz usando vectorização e compare tempo com loop')
print('2) Usando masking, calcule média de salários apenas para um grupo categórico (ex: genero=="F")')
print('3) Experimente usar einsum para calcular produto matricial e comparação de performance com dot')

