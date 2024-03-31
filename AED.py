import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_excel("/enderecos.xlsx")

# Contagem de tipos de remessa
tipo_remessa_counts = df['Tipo'].value_counts()
tipo_remessa_counts.plot(kind='bar', color='skyblue')
plt.title('Contagem de Tipos de Remessa')
plt.xlabel('Tipo de Remessa')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.show()

# Distribuição de remessas por unidade de coleta - Gráfico de Barras
plt.figure(figsize=(15, 8))
df['UNIDADE COLETA'].value_counts().plot(kind='bar', color='lightblue')
plt.title('Distribuição de Remessas por Unidade de Coleta')
plt.xlabel('Unidade de Coleta')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout() 
plt.show()

# Contagem de remessas por região de coleta
regiao_coleta_counts = df['REGIÃO  COLETA'].value_counts()
regiao_coleta_counts.plot(kind='bar', color='lightgreen')
plt.title('Contagem de Remessas por Região de Coleta')
plt.xlabel('Região de Coleta')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.show()

# Exploração dos tipos de cidade de coleta
tipo_cidade_counts = df['TIPO DE CIDADE COLETA'].value_counts()
tipo_cidade_counts.plot(kind='bar', color='lightcoral')
plt.title('Contagem de Tipos de Cidade de Coleta')
plt.xlabel('Tipo de Cidade de Coleta')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.show()

# Verificação da integridade dos endereços de e-mail
# Vamos simplesmente contar o número de endereços de e-mail não nulos
num_emails_validos = df['E-MAIL'].count()
num_emails_invalidos = len(df) - num_emails_validos
print(f"Número de endereços de e-mail válidos: {num_emails_validos}")
print(f"Número de endereços de e-mail inválidos: {num_emails_invalidos}")
