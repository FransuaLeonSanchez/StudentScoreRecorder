import streamlit as st
import pandas as pd

# Definir los datos de los estudiantes
estudiantes = [
    {"apellido": "Adauto Huaman", "nombre": "Isaac"},
    {"apellido": "Alvarado Osorio", "nombre": "Alexander Oliver"},
    {"apellido": "Alvarez Huaringa", "nombre": "Sandro Enrique"},
    {"apellido": "Andia Fernandez", "nombre": "Diego Paolo"},
    {"apellido": "Aymachoque Aymachoque", "nombre": "Luis Jairo"},
    {"apellido": "Ballarta Ulloa", "nombre": "Natalia Paula"},
    {"apellido": "Bravo Olano", "nombre": "Randy Piero"},
    {"apellido": "Callupe Pardo", "nombre": "Yoselyn Patricia"},
    {"apellido": "Carhuas Romero", "nombre": "Jhon Jesus"},
    {"apellido": "Chávez Arifaela", "nombre": "Niels Mauro"},
    {"apellido": "Del Rio Gutierrez", "nombre": "Jairo Kazuo"},
    {"apellido": "Dionicio Achachagua", "nombre": "Cesar Alonso"},
    {"apellido": "Farfan Esteban", "nombre": "Gabriel Martin"},
    {"apellido": "Flores Dalia", "nombre": "Gerson Donato"},
    {"apellido": "Flores Velarde", "nombre": "Roberto Carlos"},
    {"apellido": "Leon Sanchez", "nombre": "Fransua Mijail"},
    {"apellido": "Mallma Orihuela", "nombre": "Gherson Bryan"},
    {"apellido": "Mallma Pardo", "nombre": "Telesforo"},
    {"apellido": "Meza Alvino", "nombre": "Fabian Alessandro Moises"},
    {"apellido": "Montes Lozano", "nombre": "Diego Martin"},
    {"apellido": "Nuñez Poma", "nombre": "Robert Gianpierro Jesus"},
    {"apellido": "Palacios Palacios", "nombre": "Rafael Enrique"},
    {"apellido": "Palomino Valdivia", "nombre": "Erick Da Silva"},
    {"apellido": "Quispe Mitma", "nombre": "Cesar Fernando"},
    {"apellido": "Quispe Rojas", "nombre": "Alfredo Martin"},
    {"apellido": "Quispe Tenorio", "nombre": "Ximena Lucia"},
    {"apellido": "Ramirez Villaverde", "nombre": "Oscar Leonardo"},
    {"apellido": "Rodriguez Inga", "nombre": "Fernando Frans"},
    {"apellido": "Salirrosas Avila", "nombre": "Sebastian Jose"},
    {"apellido": "Soto Cossio", "nombre": "Edwin Isaac"},
    {"apellido": "Urbano Chocce", "nombre": "Yeison Stiven"},
    {"apellido": "Valencia Grey", "nombre": "William Gerardo"},
    {"apellido": "Valerio Contreras", "nombre": "Cristhian Jesus"},
    {"apellido": "Velasquez Solis", "nombre": "Walter Antonio"},
    {"apellido": "Villanueva Reyes", "nombre": "Juan Axel"},
]

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
    st.title("Registrador de Puntos SI605U Arquitectura Empresarial")

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