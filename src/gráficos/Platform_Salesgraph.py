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

    query = 'SELECT * FROM dbo.Platform_Sales'
    
    df = pd.read_sql(query, conn)
   
   
    plataformas = ['3DS', 'DC', 'DS', 'GB', 'GBA', 'GC', 'GEN', 'GG', 'N64', 'NES', 'NG', 'PC', 'PCFX', 'PS', 'PS2', 'PS3', 'PS4', 'PSP', 'PSV', 'SAT', 'SCD', 'SNES', 'TG16', 'WS', 'Wii', 'WiiU', 'X360', 'XB', 'XOne']

    df = df[df['Platform'].isin(plataformas)]

    print(df)
    
 
    df['NA_Sales'] = pd.to_numeric(df['NA_Sales'], errors='coerce').fillna(0.0)
    df['EU_Sales'] = pd.to_numeric(df['EU_Sales'], errors='coerce').fillna(0.0)
    df['JP_Sales'] = pd.to_numeric(df['JP_Sales'], errors='coerce').fillna(0.0)
    df['Other_Sales'] = pd.to_numeric(df['Other_Sales'], errors='coerce').fillna(0.0)
    df['Global_Sales'] = pd.to_numeric(df['Global_Sales'], errors='coerce').fillna(0.0)
    
    df_grouped = df.groupby('Platform').sum().reset_index()
    print(df_grouped)
    
   
    plt.figure(figsize=(12, 8))
    
    
    plt.bar(df_grouped['Platform'], df_grouped['NA_Sales'], label='NA Sales')
    plt.bar(df_grouped['Platform'], df_grouped['EU_Sales'], label='EU Sales', bottom=df_grouped['NA_Sales'])
    plt.bar(df_grouped['Platform'], df_grouped['JP_Sales'], label='JP Sales', bottom=df_grouped['NA_Sales'] + df_grouped['EU_Sales'])
    plt.bar(df_grouped['Platform'], df_grouped['Other_Sales'], label='Other Sales', bottom=df_grouped['NA_Sales'] + df_grouped['EU_Sales'] + df_grouped['JP_Sales'])
    plt.bar(df_grouped['Platform'], df_grouped['Global_Sales'], label='Global Sales', bottom=df_grouped['NA_Sales'] + df_grouped['EU_Sales'] + df_grouped['JP_Sales'] + df_grouped['Other_Sales'])

    plt.xlabel('Platform')
    plt.ylabel('Sales')
    plt.title('Sales by Platform')
    plt.legend()
    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()
    
except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals():
        conn.close()
