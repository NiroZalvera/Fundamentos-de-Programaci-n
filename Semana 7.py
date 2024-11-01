import streamlit as st

def verificar_contrasena():
    st.title("Verificación de contraseña")

    #Variable para almacenar la contraseña
    contraseña_correcta = "asdasd"
    contrasena_ingresada = ""

    #Repetir hasta que la contraseña sea correcta

    while contrasena_ingresada != contrasena_correcta:
        contrasena_ingresada = st.text_input("Ingrese la contraseña", type="password")
        if contrasena_ingresada == contrasena_correcta
            st.success("Bienvenido")
            break
        elif contrasena_ingresada
            st.error("Contraseña incorrecta, intente de nuevo")

if __name__ == "__main__":
    verificar_contrasena()