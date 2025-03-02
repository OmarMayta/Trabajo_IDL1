# IDL_1.py
import streamlit as st
from logica import crear_trabajadores

st.title("Sistema de Recursos Humanos - Business Corporation")

# Obtener lista de trabajadores
trabajadores = crear_trabajadores()

# Mostrar información en Streamlit
for trabajador in trabajadores:
    st.subheader(trabajador.def_resumen())
    st.text(f"Jefe inmediato: {trabajador.def_jefe_inmediato()}")
    st.text(f"Estado: {trabajador.def_estado()}")
    st.write("---")
