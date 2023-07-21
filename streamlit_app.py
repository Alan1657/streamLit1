import streamlit as st
import graphviz as graphviz

def draw_context_diagram():
    dot = graphviz.Digraph(format='png')
    
    dot.node('Sistema', shape='box', style='filled', fillcolor='lightblue', label='Lista de Requerimientos\nFuncionales y No Funcionales')
    dot.node('Usuarios', shape='oval', style='filled', fillcolor='lightgreen', label='Usuarios\n(Padres, Docentes, Alumnos)')
    dot.node('Cliente', shape='oval', style='filled', fillcolor='lightcoral', label='Cliente\n(Colegios peruanos\ny Equipo Directivo)')
    dot.node('Administrador', shape='oval', style='filled', fillcolor='lightyellow', label='Administrador\ndel sistema')

    dot.edges(['Sistema -> Usuarios', 'Sistema -> Cliente', 'Sistema -> Administrador'])
    
    st.graphviz_chart(dot.source)

def main():
    st.title('Diagrama de Contexto')
    st.markdown('''
    Este es un ejemplo de un diagrama de contexto creado con Streamlit y Graphviz.
    ''')
    draw_context_diagram()

if __name__ == "__main__":
    main()
