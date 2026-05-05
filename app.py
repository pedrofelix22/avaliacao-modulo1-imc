import streamlit as st

st.title("Calculadora imc 📱")
st.subheader("Feito com Streamlit ")

altura = st.number_input("digite a sua altura", min_value=0.0)
peso = st.number_input("digite o seu peso", min_value=0.0)

imc = peso / altura ** 2

if st.button("calcular"):
  
   if imc < 18.5:
      st.error("Abaixo do peso ")
   elif imc < 24.9:
      st.write("Peso normal ")
   elif imc < 29.9:
      st.write("sobrepeso ")
   elif imc < 34.9:
      st.write("obesidade gral 1 ")

   elif imc < 39.9:
      st.write("obesiade gral 2 ")   

   else:
      st.write("obesiade gral 3 ")