import streamlit as st
from graphviz import Digraph

def draw_context_diagram():
    dot = Digraph(comment='Context Diagram', format='png')
    dot.node('Sistema', 'Sistema')
    dot.node('Usuarios', 'Usuarios')
    dot.node('Cliente', 'Cliente')
    dot.node('Administrador', 'Administrador')
    dot.edges([('Sistema', 'Usuarios'), ('Sistema', 'Cliente'), ('Sistema', 'Administrador')])

    st.graphviz_chart(dot.source)

def main():
    st.title("Diagrama de Contexto")
    draw_context_diagram()

if __name__ == "__main__":
    main()
