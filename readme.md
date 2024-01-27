# Registrador de Puntos SI605U Arquitectura Empresarial

Este programa fue desarrollado en Python utilizando la biblioteca PyQt5 y Pandas. Su propósito es permitir a los profesores registrar puntos adicionales para sus alumnos, asignando puntajes positivos o negativos en diferentes fechas. Además, el programa proporciona la funcionalidad de visualizar y actualizar estos puntajes de manera fácil y eficiente.

## Características principales

1. **Interfaz Gráfica Intuitiva:** El programa cuenta con una interfaz gráfica fácil de usar, desarrollada con PyQt5, que permite al profesor navegar y realizar acciones de manera eficiente.

2. **Registro por Fecha:** Los puntajes se registran y se pueden visualizar de acuerdo con la fecha en que se asignaron. Esto proporciona un seguimiento claro del rendimiento de los estudiantes en diferentes momentos.

3. **Almacenamiento en Archivo Excel:** Los datos se almacenan en un archivo Excel llamado "Registro_Puntaje_SI650U.xlsx". Si el archivo no existe, el programa lo crea automáticamente. Este archivo contiene la información de los estudiantes, sus puntajes y las fechas asociadas.

4. **Funciones de Asignar y Quitar Puntos:** Se proporcionan botones específicos para asignar y quitar puntos a cada estudiante de manera individual.

5. **Visualización de Puntajes Actuales:** Los puntajes actuales de los estudiantes se muestran en una tabla en la interfaz gráfica, permitiendo al profesor verificar rápidamente el estado actual de los puntajes.

## Uso del Programa

1. **Inicio:**
   - Al ejecutar el programa, se abrirá la ventana principal con el título "Registrador de Puntos".
   - La interfaz incluye un cuadro desplegable para seleccionar la fecha y un botón para registrar los puntajes.

2. **Registro de Puntajes:**
   - El profesor puede asignar o quitar puntos a cada estudiante utilizando los botones "Asignar Punto" y "Quitar Punto" en la tabla.
   - Después de realizar cambios, se debe hacer clic en el botón "Registrar Puntaje" para guardar los puntajes en el archivo Excel.

3. **Visualización por Fecha:**
   - El cuadro desplegable de fecha permite seleccionar la fecha deseada para visualizar los puntajes asignados en esa fecha específica.

4. **Datos en Excel:**
   - Los datos se almacenan en el archivo Excel mencionado anteriormente, proporcionando una estructura clara con información detallada de cada estudiante.

## Requisitos y Dependencias

- Python 3.x
- PyQt5
- Pandas

## Instalación

1. Clona o descarga el repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado.
3. Instala las dependencias ejecutando el siguiente comando:
   ```
   pip install PyQt5 pandas
   ```

## Ejecución

Ejecuta el programa utilizando el siguiente comando en la terminal o línea de comandos:

```
python nombre_del_archivo.py
```

Reemplaza `nombre_del_archivo.py` con el nombre real del archivo que contiene el código.

## Notas Adicionales

- Asegúrate de tener los permisos necesarios para leer y escribir en el sistema de archivos, especialmente al trabajar con el archivo Excel.
- En caso de no existir el archivo Excel al inicio, el programa creará automáticamente un archivo con la estructura necesaria.

¡Disfruta utilizando el Registrador de Puntos SI605U Arquitectura Empresarial! Si tienes alguna pregunta o encuentras problemas, no dudes en contactar al desarrollador.