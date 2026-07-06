"""Mineração, Preparação e Estatística para Ciência de Dados

Este roteiro reúne exemplos práticos e notas de trabalho para:
- Mineração e extração de dados
- Preparação e limpeza (limpeza, imputação, encoding, scaling)
- Estatística descritiva e inferencial básica útil em Data Science

O código abaixo tenta importar bibliotecas comuns e oferece alternativas
quando elas não estiverem instaladas. Instalar o conjunto recomendado:
`pip install pandas numpy scikit-learn matplotlib seaborn scipy`
"""

print("Iniciando: Mineração, Preparação e Estatística - Aula 14")

try:
	import pandas as pd
	import numpy as np
	from sklearn.model_selection import train_test_split
	from sklearn.impute import SimpleImputer
	from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
	from sklearn.compose import ColumnTransformer
	from sklearn.pipeline import Pipeline
	from sklearn.feature_selection import VarianceThreshold
	from sklearn.decomposition import PCA
	from sklearn.preprocessing import OrdinalEncoder
	import matplotlib.pyplot as plt
	import seaborn as sns
	from scipy import stats
except Exception as e:
	print("Aviso: algumas bibliotecas não estão instaladas. Muitos exemplos usam pandas, sklearn e seaborn.")
	print("Erro de import:", e)


def exemplo_mineração_csv(caminho_csv: str = None):
	"""Exemplo: carregar dados CSV (ou criar DataFrame de exemplo se não houver arquivo)."""
	if caminho_csv:
		df = pd.read_csv(caminho_csv)
	else:
		# Criar DataFrame de exemplo
		rng = np.random.default_rng(42)
		df = pd.DataFrame({
			'idade': rng.integers(18, 80, size=200),
			'salario': rng.normal(5000, 1500, size=200).round(2),
			'genero': rng.choice(['M','F'], size=200),
			'comprou': rng.choice([0,1], size=200, p=[0.7,0.3])
		})
		# introduzir valores faltantes
		df.loc[rng.choice(df.index, size=10), 'salario'] = np.nan
	return df


def analise_exploratoria(df: pd.DataFrame):
	"""Passos básicos de EDA: shape, tipos, estatísticas, missing, correlações."""
	print('Shape:', df.shape)
	print('\nTipos e non-null:')
	print(df.info())
	print('\nEstatísticas descritivas:')
	print(df.describe(include='all'))
	print('\nValores faltantes por coluna:')
	print(df.isna().sum())

	# Correlação somente para numéricas
	num = df.select_dtypes(include=[np.number])
	if not num.empty:
		corr = num.corr()
		print('\nCorrelação (numéricas):')
		print(corr)
		try:
			sns.heatmap(corr, annot=True, cmap='coolwarm')
			plt.title('Correlação - heatmap')
			plt.tight_layout()
			plt.show()
		except Exception:
			pass


def preparar_dados(df: pd.DataFrame, target: str = 'comprou'):
	"""Exemplo de pipeline de preparação:
	- imputação numérica
	- codificação categórica
	- escala
	- seleção simples de variância
	Retorna (X_train, X_test, y_train, y_test, pipeline)
	"""
	# separar features/target
	if target not in df.columns:
		raise ValueError('Coluna target não encontrada')
	X = df.drop(columns=[target])
	y = df[target]

	numeric_cols = X.select_dtypes(include=['number']).columns.tolist()
	categorical_cols = X.select_dtypes(include=['object','category']).columns.tolist()

	print('Numerical cols:', numeric_cols)
	print('Categorical cols:', categorical_cols)

	# Pipelines separados
	numeric_pipeline = Pipeline([
		('imputer', SimpleImputer(strategy='median')),
		('scaler', StandardScaler()),
	])

	categorical_pipeline = Pipeline([
		('imputer', SimpleImputer(strategy='most_frequent')),
		('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False)),
	])

	preprocessor = ColumnTransformer([
		('num', numeric_pipeline, numeric_cols),
		('cat', categorical_pipeline, categorical_cols),
	], remainder='drop')

	# Pipeline final com seleção de variância
	pipeline = Pipeline([
		('pre', preprocessor),
		('var', VarianceThreshold(threshold=0.0)),
	])

	X_transformed = pipeline.fit_transform(X)
	# criar PCA opcional para diminuir dimensionalidade se necessário
	if X_transformed.shape[1] > 10:
		pca = PCA(n_components=min(10, X_transformed.shape[1]))
		X_transformed = pca.fit_transform(X_transformed)

	X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
	return X_train, X_test, y_train, y_test, pipeline


def estatistica_descritiva(X: np.ndarray):
	"""Cálculos rápidos de média, mediana, variância, skewness, kurtosis."""
	print('Média por coluna:', np.nanmean(X, axis=0))
	print('Mediana por coluna:', np.nanmedian(X, axis=0))
	print('Desvio padrão por coluna:', np.nanstd(X, axis=0))
	try:
		print('Skewness por coluna:', stats.skew(X, axis=0))
		print('Kurtosis por coluna:', stats.kurtosis(X, axis=0))
	except Exception:
		pass


def testes_inferenciais(df: pd.DataFrame):
	"""Exemplos de testes estatísticos rápidos: t-test e chi2 para independência.
	Nota: requer scipy.stats para alguns testes.
	"""
	num = df.select_dtypes(include=[np.number])
	# t-test entre duas amostras (exemplo artificial)
	if num.shape[1] >= 2:
		col1, col2 = num.columns[:2]
		tstat, pval = stats.ttest_ind(num[col1].dropna(), num[col2].dropna(), equal_var=False)
		print(f'T-test {col1} vs {col2}: t={tstat:.3f}, p={pval:.3f}')


def feature_engineering_exemplos(df: pd.DataFrame):
	"""Exemplos simples: interações, binning, transformações log/box-cox."""
	df = df.copy()
	if 'idade' in df.columns and 'salario' in df.columns:
		df['idade_x_salario'] = df['idade'] * df['salario']
		# binning
		df['idade_bin'] = pd.cut(df['idade'], bins=[0,25,40,60,100], labels=['jovem','adulto','maduro','idoso'])
		# transformação log segura
		df['salario_log'] = np.log1p(df['salario'].fillna(0))
	return df


def resumo_pratico():
	df = exemplo_mineração_csv()
	analise_exploratoria(df)
	df2 = feature_engineering_exemplos(df)
	X_train, X_test, y_train, y_test, pipeline = preparar_dados(df2, target='comprou')
	estatistica_descritiva(X_train)
	testes_inferenciais(df)
	print('Pipeline criado:', pipeline)


if __name__ == '__main__':
	resumo_pratico()

