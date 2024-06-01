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

    query = 'SELECT * FROM dbo.Platform_Sales'

    df = pd.read_sql(query, conn)

    plataformas = ['3DS', 'DC', 'DS', 'GB', 'GBA', 'GC', 'GEN', 'GG', 'N64', 'NES', 'NG', 'PC', 'PCFX', 'PS', 'PS2', 'PS3', 'PS4', 'PSP', 'PSV', 'SAT', 'SCD', 'SNES', 'TG16', 'WS', 'Wii', 'WiiU', 'X360', 'XB', 'XOne']

    df = df[df['Platform'].isin(plataformas)]

    df['NA_Sales'] = pd.to_numeric(df['NA_Sales'], errors='coerce').fillna(0.0)
    df['EU_Sales'] = pd.to_numeric(df['EU_Sales'], errors='coerce').fillna(0.0)
    df['JP_Sales'] = pd.to_numeric(df['JP_Sales'], errors='coerce').fillna(0.0)
    df['Other_Sales'] = pd.to_numeric(df['Other_Sales'], errors='coerce').fillna(0.0)
    df['Global_Sales'] = pd.to_numeric(df['Global_Sales'], errors='coerce').fillna(0.0)

    df_grouped = df.groupby('Platform').sum().reset_index()

    fig = px.bar(df_grouped, x='Platform', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
                 barmode='stack',
                 labels={'value': 'Sales', 'Platform': 'Platform'},
                 title='Sales by Platform')

    fig.update_layout(xaxis_title='Platform',
                      yaxis_title='Sales',
                      title_x=0.5,
                      xaxis=dict(tickmode='array', tickvals=df_grouped['Platform'], ticktext=df_grouped['Platform']),
                      legend=dict(orientation='h', yanchor='top', y=1.15, xanchor='right', x=1),
                      barmode='stack',
                      hovermode='x unified')

    fig.write_html("sales_by_platform.html")

except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals():
        conn.close()
