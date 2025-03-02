# idl1.py
import streamlit as st
from logica import crear_trabajadores

def main():
    st.title("Listado de Trabajadores - Business Corporation")
    
    trabajadores = crear_trabajadores()
    
    for t in trabajadores:
        st.subheader(t.get_nombre())
        st.write("Resumen:", t.def_resumen())
        st.write("Jefe Inmediato:", t.def_jefe_inmediato())
        st.write("Estado:", t.def_estado())
        st.markdown("---")

if __name__ == '__main__':
    main()
