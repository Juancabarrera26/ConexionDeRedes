import pandas as pd
import matplotlib.pyplot as plt

def graficar_resultados(csv_file, titulo):
    """
    Función para graficar los resultados de velocidad de red.
    :param csv_file: Ruta del archivo CSV con los datos.
    :param titulo: Título del gráfico.
    """
    # Cargar los datos
    datos = pd.read_csv(csv_file)
    
    # Verificar que el CSV tiene las columnas esperadas
    if 'Tiempo' not in datos.columns or 'Velocidad' not in datos.columns:
        print("Error: El archivo CSV no tiene las columnas necesarias (Tiempo, Velocidad)")
        return
    
    # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(datos['Tiempo'], datos['Velocidad'], marker='o', linestyle='-', color='b')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (Mbps)')
    plt.title(titulo)
    plt.grid()
    plt.show()

# Ejemplo de uso
graficar_resultados('resultadoRed.csv', 'Velocidad de la Red a lo Largo del Tiempo')
