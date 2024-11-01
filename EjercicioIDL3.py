import streamlit as st

# Función principal
def main():
    st.title("Datos del Automóvil")

    # Entrada de datos
    marca = st.text_input("Ingrese la marca del automóvil: ")
    modelo = st.text_input("Ingrese el modelo del automóvil: ")
    kilometraje = st.number_input("Ingrese el kilometraje del automóvil: ", min_value=1, step=1)

    # Verificar si el botón de registro es presionado
    if st.button("Registrar Automóvil"):
        # Validación de campos
        if not marca:
            st.error("Por favor, ingrese una marca válida.")
        elif not modelo:
            st.error("Por favor, ingrese un modelo válido.")
        elif kilometraje < 0:
            st.error("Por favor, ingrese un kilometraje mayor o igual a cero.")
        else:
            # Si todo está correcto, mostrar el resultado
            st.success(f"Automóvil registrado con éxito:")
            st.write(f"Marca: {marca}")
            st.write(f"Modelo: {modelo}")
            st.write(f"Kilometraje: {kilometraje} km")

# Ejecutar el programa
if __name__ == "__main__":
    main()