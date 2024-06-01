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
    
  
    query = 'SELECT * FROM dbo.Year_vs_Sales'
    
 
    df = pd.read_sql(query, conn)

    print(df)
    
  
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
    df['NA_Sales'] = pd.to_numeric(df['NA_Sales'], errors='coerce').fillna(0.0)
    df['EU_Sales'] = pd.to_numeric(df['EU_Sales'], errors='coerce').fillna(0.0)
    df['JP_Sales'] = pd.to_numeric(df['JP_Sales'], errors='coerce').fillna(0.0)
    df['Other_Sales'] = pd.to_numeric(df['Other_Sales'], errors='coerce').fillna(0.0)
    df['Global_Sales'] = pd.to_numeric(df['Global_Sales'], errors='coerce').fillna(0.0)

    print(df.dtypes)
    

    df_grouped = df.groupby('Year').sum().reset_index()
    
  
    print(df_grouped)

    fig = px.line(df_grouped, x='Year', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
                  labels={'value': 'Sales (in millions)', 'Year': 'Year'},
                  title='Video Game Sales by Year')
    
    fig.update_traces(mode='markers+lines')
    fig.update_layout(xaxis=dict(tickmode='linear', dtick=5, range=[1984, 2015]),
                      yaxis=dict(tickmode='linear', dtick=100, range=[0, 900]),
                      legend=dict(orientation='h', yanchor='top', y=1.15, xanchor='right', x=1),
                      xaxis_title='Year',
                      yaxis_title='Sales (in millions)',
                      title_x=0.5,
                      hovermode='x unified')
    
    fig.write_html("video_game_sales.html")
    
except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals():
        conn.close()
