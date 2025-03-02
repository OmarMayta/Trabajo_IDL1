# IDL_1.py

import streamlit as st
import os, sys

# Asegura que Python "vea" la carpeta actual (por si hay problemas de importación)
sys.path.append(os.path.dirname(__file__))

from logica import crear_trabajadores

def main():
    st.title("Gestión de Recursos Humanos - Business Corporation")

    # Obtenemos el array de objetos (trabajadores)
    lista = crear_trabajadores()

    # Recorremos la lista y mostramos la información
    for t in lista:
        st.subheader(t.get_nombre())            # Nombre del trabajador
        st.write("Resumen:", t.def_resumen())   # Puesto y rango
        st.write("Jefe Inmediato:", t.def_jefe_inmediato())  
        st.write("Estado:", t.def_estado())     # Estado del trabajador
        st.markdown("---")

if __name__ == "__main__":
    main()
