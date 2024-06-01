import pandas as pd
import pyodbc
import matplotlib.pyplot as plt


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
    
  
    plt.figure(figsize=(12, 8))
 
    plt.bar(df_grouped['Genre'], df_grouped['NA_Sales'], label='NA Sales')
    plt.bar(df_grouped['Genre'], df_grouped['EU_Sales'], label='EU Sales', bottom=df_grouped['NA_Sales'])
    plt.bar(df_grouped['Genre'], df_grouped['JP_Sales'], label='JP Sales', bottom=df_grouped['NA_Sales'] + df_grouped['EU_Sales'])
    plt.bar(df_grouped['Genre'], df_grouped['Other_Sales'], label='Other Sales', bottom=df_grouped['NA_Sales'] + df_grouped['EU_Sales'] + df_grouped['JP_Sales'])
    plt.bar(df_grouped['Genre'], df_grouped['Global_Sales'], label='Global Sales', bottom=df_grouped['NA_Sales'] + df_grouped['EU_Sales'] + df_grouped['JP_Sales'] + df_grouped['Other_Sales'])

    plt.xlabel('Genre')
    plt.ylabel('Sales')
    plt.title('Sales by Genre')
    plt.legend()
    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()
    
except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals():
        conn.close()
