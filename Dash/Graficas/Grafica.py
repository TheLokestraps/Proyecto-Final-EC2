import dash
import dash_core_components as dcc
import dash_html_components as html
import mysql.connector as mysql
import pandas as pd
import pandas.io.sql as sqlio
import plotly.graph_objs as go
import plotly.express as px



if __name__ == "__main__":
    Conexion = mysql.connect(host='db', user='user', passwd='password',db='universidad')
    sql_select_Query1 = "select * from persona"
    sql_select_Query2 = "select * from departamento"
    cursor = Conexion.cursor(buffered=True)
    cursor.execute(sql_select_Query1)
    
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
    records = cursor.fetchall()
    Persona = int(cursor.rowcount)

    cursor.execute(sql_select_Query2)
    Departamento = int(cursor.rowcount)

    Datos = [Persona,Departamento]

    Nombres = ['Persona','Departamento'] 

    df = px.data.iris()
    data1 = px.bar(df,x=Nombres,y=Datos,title="Proyecto Final de Estructuras del Computador 2 \n Presentado por Ivan Perez, Diego Palacios y Jairo Gonzalez")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
    sql_select_Query1 = "select * from curso_escolar"
    sql_select_Query2 = "select * from asignatura"
    
    cursor.execute(sql_select_Query1)
    curso_escolar = int(cursor.rowcount)
    
    cursor.execute(sql_select_Query2)
    Asignatura = int(cursor.rowcount)
    
    Datos = [curso_escolar,Asignatura]
    Nombres = ['curso_escolar','Asignatura'] 
   
    data2 = px.bar(df,x=Nombres,y=Datos,title="Proyecto Final de Estructuras del Computador 2 \n Presentado por Ivan Perez, Diego Palacios y Jairo Gonzalez")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
    sql_select_Query1 = "select * from profesor"
    sql_select_Query2 = "select * from persona"
    
    cursor.execute(sql_select_Query1)
    Profesor = int(cursor.rowcount)
    
    cursor.execute(sql_select_Query2)
    Persona = int(cursor.rowcount)
    
    Datos = [Profesor,Persona]
    Nombres = ['curso_escolar','Persona'] 

    data3 = px.bar(df,x=Nombres,y=Datos,title="Proyecto Final de Estructuras del Computador 2 \n Presentado por Ivan Perez, Diego Palacios y Jairo Gonzalez")

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div(children=[
    html.H1(children='Proyecto Final de Estructuras del Computador 2',style={'textalign':'right'}),

    dcc.Graph(
        id='Grafico 1',
        figure=data1
    ),

    dcc.Graph(
        id='Grafico 2',
        figure=data2
    ),

    dcc.Graph(
        id='Grafico 3',
        figure=data3
    )
])
    app.run_server(host='0.0.0.0', debug=True, port=8050)

