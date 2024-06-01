import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import plotly.express as px

try:
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                          'SERVER=DESKTOP-9KR0VKM;'
                          'DATABASE=Videogames;'
                          'TrustServerCertificate=yes;'
                          'Trusted_Connection=yes')
    print("Conexão estabelecida com sucesso!")

  
    query = 'SELECT * FROM dbo.X360_PS3_2008'
    
    df = pd.read_sql(query, conn)
    df = df.sort_values(by='Global_Sales', ascending=False)

    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0.0)
    df['Global_Sales'] = pd.to_numeric(df['Global_Sales'], errors='coerce').fillna(0.0)
    
    print("Dados organizados de forma decrescente por Global_Sales:")
    print(df)
    
    df_x360_2008_top5 = df[(df['Year'] == 2008) & (df['Platform'] == 'X360')].nlargest(5, 'Global_Sales')
    print("Top 5 jogos mais vendidos de X360 em 2008:")
    print(df_x360_2008_top5)

    df_ps3_2008_top5 = df[(df['Year'] == 2008) & (df['Platform'] == 'PS3')].nlargest(5, 'Global_Sales')
    print("Top 5 jogos mais vendidos de PS3 em 2008:")
    print(df_ps3_2008_top5)

        
    fig_x360 = px.bar(df_x360_2008_top5, x='Name', y='Global_Sales', title='Top 5 Jogos Mais Vendidos de X360 em 2008')
    fig_x360.write_html('x360_top5_2008.html')
    
    fig_ps3 = px.bar(df_ps3_2008_top5, x='Name', y='Global_Sales', title='Top 5 Jogos Mais Vendidos de PS3 em 2008')
    fig_ps3.write_html('ps3_top5_2008.html')
    
   
except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals():
        conn.close()
