import pandas as pd
import matplotlib.pyplot as plt

# Carga del archivo CSV
netflix_data = pd.read_csv('netflix_titles.csv')

#  Visualizar los primeros 10 registros del conjunto de datos
print('Los 10 primero registros:')
print(netflix_data.head(10))

# Visualizar los últimos 15 registros del conjunto de datos
print('Los 15 ultimos registros:')
print(netflix_data.tail(15))

#   Generar los estadísticos básicos
print(' Estadísticos básicos:')
netflix_data.describe()

# Completar los datos vacios (NaN) con ceros (0)
netflix_data.fillna(0, inplace=True)

# Asegurarse de que 'release_year' sea numérico
netflix_data['release_year'] = pd.to_numeric(netflix_data['release_year'], errors='coerce')

# Filtrar datos entre 2010 y 2021
filtered_data = netflix_data[(netflix_data['release_year'] >= 2010) & (netflix_data['release_year'] <= 2021)]

# Agrupar por año y tipo, contando los registros
grouped_data = filtered_data.groupby(['release_year', 'type']).size().unstack(fill_value=0)

# Imprimir los datos agrupados para verificar
print(grouped_data)

# Crear el gráfico
plt.figure(figsize=(12, 6))
grouped_data.plot(kind='bar', stacked=False, color=['blue', 'orange'])
plt.title('Comparación de Películas vs Series por Año (2010-2021)')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.legend(title='Tipo', labels=['Películas', 'Series'])
plt.grid(axis='y')

# Mostrar el gráfico
plt.show()
