import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
# Asegúrate de tener un archivo CSV llamado 'avocado.csv'
df = pd.read_csv('avocado.csv')

# 1. Obtener cuántas filas y cuántas columnas tiene el conjunto de datos
filas, columnas = df.shape
print(f"El conjunto de datos tiene {filas} filas y {columnas} columnas.")

# 2. Mostrar los primeros 100 registros
print("Primeros 100 registros:")
print(df.head(100))

# 3. Mostrar los últimos 20 registros
print("Últimos 20 registros:")
print(df.tail(20))

# 4. Precio mínimo, máximo y promedio del aguacate
precio_min = df['AveragePrice'].min()
precio_max = df['AveragePrice'].max()
precio_promedio = df['AveragePrice'].mean()

print(f"Precio mínimo: {precio_min}")
print(f"Precio máximo: {precio_max}")
print(f"Precio promedio: {precio_promedio:.2f}")

# 5. Generar un gráfico de tipo scatter para 'year' vs 'AveragePrice' en 3 regiones

# Filtrar datos para tres regiones específicas
region1 = df[df['region'] == 'Albany']
region2 = df[df['region'] == 'Atlanta']
region3 = df[df['region'] == 'West']

# Crear un subplot correctamente
fig, x1 = plt.subplots(figsize=(8, 6))

# Crear los gráficos de dispersión en función de las variables 'year' y 'AveragePrice'
g_region1 = region1.plot(x='year', y='AveragePrice', kind='scatter', color='red', ax=x1, label='Albany')
g_region2 = region2.plot(x='year', y='AveragePrice', kind='scatter', color='green', ax=x1, label='Atlanta')
g_region3 = region3.plot(x='year', y='AveragePrice', kind='scatter', color='blue', ax=x1, label='West')

# Añadir título y etiquetas
plt.title('Precio Promedio de Aguacate por Año en Diferentes Regiones')
plt.xlabel('Año')
plt.ylabel('Precio Promedio ($)')

# Mostrar el gráfico en pantalla
plt.show()
