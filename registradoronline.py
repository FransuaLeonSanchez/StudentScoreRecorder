import streamlit as st
import pandas as pd

# Definir los datos de los estudiantes
estudiantes = []
with open("SI605U.txt", "r") as file:
    for line in file:
        partes = line.strip().split(" ")
        if len(partes) >= 3:
            apellido1 = partes[0]
            apellido2 = partes[1]
            nombre = " ".join(partes[2:])
            apellido = f"{apellido1} {apellido2}"
            estudiantes.append({"apellido": apellido, "nombre": nombre})

# Inicializar st.session_state si no está definido
if "puntajes" not in st.session_state:
    st.session_state.puntajes = [0] * len(estudiantes)

# Definir la función para registrar puntajes
def registrar_puntajes(fecha_actual, puntajes):
    # Crear un DataFrame con los datos de la tabla
    data = []
    for i, estudiante in enumerate(estudiantes):
        data.append(
            {
                "Apellido": estudiante["apellido"],
                "Nombre": estudiante["nombre"],
                fecha_actual: puntajes[i],
            }
        )

    df = pd.DataFrame(data)

    # Crear el nombre del archivo con la fecha
    nombre_archivo = f"Registro_Puntajes_{fecha_actual}.xlsx"

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(nombre_archivo, index=False, sheet_name="Registros")

    # Mostrar mensaje de puntajes registrados correctamente
    mensaje = f"Puntajes de la fecha {fecha_actual} correctamente registrados"
    st.success(mensaje)

    return nombre_archivo

# Crear la aplicación Streamlit
def main():
    st.title("Puntos Ciencia de datos y seguridad de la información")

    # Cuadro desplegable para seleccionar fecha
    fecha_actual = st.date_input("Selecciona la fecha", pd.Timestamp.today())

    # Crear la tabla de asistencia
    st.write("### Tabla de Puntajes")
    for i, estudiante in enumerate(estudiantes):
        apellido_nombre = f"{estudiante['apellido']} {estudiante['nombre']}"
        st.session_state.puntajes[i] = st.number_input(
            f"{apellido_nombre}", value=st.session_state.puntajes[i]
        )

    # Botón para registrar puntajes
    if st.button("Registrar Puntajes"):
        nombre_archivo = registrar_puntajes(fecha_actual.strftime("%d_%m_%Y"), st.session_state.puntajes)
        try:
            with open(nombre_archivo, "rb") as file:
                data = file.read()
                st.download_button(
                    label="Descargar archivo Excel",
                    data=data,
                    file_name=nombre_archivo,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
        except FileNotFoundError:
            st.warning(
                "No se encontró el archivo Excel. Por favor, primero registra los puntajes."
            )

if __name__ == "__main__":
    main()