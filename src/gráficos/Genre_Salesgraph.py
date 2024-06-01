import pandas as pd
import pyodbc
import plotly.express as px

try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                          'SERVER=DESKTOP-9KR0VKM;'
                          'DATABASE=Videogames;'
                          'TrustServerCertificate=yes;'
                          'Trusted_Connection=yes')
    print("Conexão estabelecida com sucesso!")

    query = 'SELECT * FROM dbo.Genre_Sales'

    df = pd.read_sql(query, conn)

    generos = ['Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']

    df = df[df['Genre'].isin(generos)]

    df['NA_Sales'] = pd.to_numeric(df['NA_Sales'], errors='coerce').fillna(0.0)
    df['EU_Sales'] = pd.to_numeric(df['EU_Sales'], errors='coerce').fillna(0.0)
    df['JP_Sales'] = pd.to_numeric(df['JP_Sales'], errors='coerce').fillna(0.0)
    df['Other_Sales'] = pd.to_numeric(df['Other_Sales'], errors='coerce').fillna(0.0)
    df['Global_Sales'] = pd.to_numeric(df['Global_Sales'], errors='coerce').fillna(0.0)

    df_grouped = df.groupby('Genre').sum().reset_index()

    fig = px.bar(df_grouped, x='Genre', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
                 barmode='stack',
                 labels={'value': 'Sales', 'Genre': 'Genre'},
                 title='Sales by Genre')

    fig.update_layout(xaxis_title='Genre',
                      yaxis_title='Sales',
                      title_x=0.5,
                      xaxis=dict(tickmode='array', tickvals=df_grouped['Genre'], ticktext=df_grouped['Genre']),
                      legend=dict(orientation='h', yanchor='top', y=1.15, xanchor='right', x=1),
                      barmode='stack',
                      hovermode='x unified')

    fig.write_html("sales_by_genre.html")

except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals():
        conn.close()
