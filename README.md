# Aplicación Web de Análisis de Datos de Vehículos

Este proyecto es una aplicación web interactiva construida con Streamlit para el análisis exploratorio de un conjunto de datos de anuncios de vehículos.

## Propósito

La aplicación sirve como una herramienta de visualización que permite a los usuarios explorar la distribución y las relaciones dentro del conjunto de datos `vehicles_us.csv`. Proporciona una interfaz gráfica sencilla para generar gráficos sin necesidad de escribir código.

## Funcionalidad

La aplicación web actual incluye las siguientes características:

- **Encabezado principal**: Un título claro que describe el propósito de la aplicación.
- **Histograma de Odómetro**: Un botón que, al ser presionado, genera y muestra un histograma de la distribución del odómetro de los vehículos.
- **Gráfico de Dispersión Odómetro vs. Precio**: Un segundo botón que construye un gráfico de dispersión para visualizar la relación entre el kilometraje y el precio de los vehículos.

## Cómo Ejecutar la Aplicación

1.  Asegúrate de tener Python instalado.
2.  Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ejecuta la aplicación desde la terminal en el directorio raíz de tu proyecto:
    ```bash
    streamlit run app.py
    ```