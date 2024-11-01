import streamlit as st

def marca():
def modelo():
def kilometraje():
    if kilometraje < 0:
         st.write("Por favor, ingrese un radio mayor a cero.")

def main():
    st.title("Datos del Automóvil")

    marca = st.text_input("Ingrese la marca del automóvil: ")
    modelo = st.text_input("Ingrese el modelo del automóvil: ")
    kilometraje = st.number_input("Ingrese el kilometraje del automóvil: ")
    
    #Mostrar el resultado
    st.write(f"La marca es: {marca}, el modelo es: {modelo}, el kilometraje es: {kilometraje}")

if __name__ == "__main__":
    main()
