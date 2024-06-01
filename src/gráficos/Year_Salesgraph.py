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

    plt.figure(figsize=(12, 8))
    
    plt.plot(df_grouped['Year'], df_grouped['NA_Sales'], label='NA Sales', marker='o')
    plt.plot(df_grouped['Year'], df_grouped['EU_Sales'], label='EU Sales', marker='o')
    plt.plot(df_grouped['Year'], df_grouped['JP_Sales'], label='JP Sales', marker='o')
    plt.plot(df_grouped['Year'], df_grouped['Other_Sales'], label='Other Sales', marker='o')
    plt.plot(df_grouped['Year'], df_grouped['Global_Sales'], label='Global Sales', marker='o')
    
    plt.xlabel('Year')
    plt.ylabel('Sales (in millions)')
    plt.title('Video Game Sales by Year')
    plt.legend()
    plt.grid(True)
    plt.xlim(1984, 2015)
    plt.xticks(range(1984, 2016, 5))
    plt.ylim(0, 100)
    plt.yticks(range(0, 900, 100))
    
    plt.tight_layout()

    plt.show()
    
except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals():
        conn.close()
