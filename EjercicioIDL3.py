import streamlit as st

 suma=0
 cont=0
 num=int(input("Número:"))
 while num!=0:
 	cont=cont+1
 	suma=suma+num
 	num=int(input("Número:"))
 media=float(suma)/cont
 print("La suma es %d y la media es %f"%(suma,media))
