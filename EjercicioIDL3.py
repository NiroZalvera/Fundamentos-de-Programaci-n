import streamlit as st

# Función principal
def main():
    st.title("Calculadora de Suma y Media de Números")

    # Inicializar variables
    suma = 0
    contador = 0

    # Entrada de números en un bucle
    while True:
        numero = st.number_input("Ingresa un número (0 para finalizar):", step=1.0, format="%f")

        # Terminar si el usuario ingresa un 0
        if numero == 0:
            break
        
        # Acumular la suma y contar cada número ingresado
        suma += numero
        contador += 1

    # Calcular y mostrar la media solo si hay números válidos
    if contador > 0:
        media = suma / contador
        st.success(f"Suma total: {suma}")
        st.success(f"Media de los números: {media}")
    else:
        st.info("No se ingresaron números.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
