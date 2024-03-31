import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregar os dados preparados
dados_preparados = pd.read_csv("enderecos_formatados.csv")

# Inicializar o vetorizador TF-IDF
tfidf_vectorizer = TfidfVectorizer()

# Ajustar e transformar os dados para vetor TF-IDF
tfidf_matrix = tfidf_vectorizer.fit_transform(dados_preparados["Endereço"])

# Calcular a similaridade de cosseno entre os endereços
similaridade = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Exemplo de recomendação simples
endereco_query = "Rua Direita, Diamantina MG CEP 39100-000"  # Endereço de exemplo para recomendação
indice_query = dados_preparados[dados_preparados["Endereço"] == endereco_query].index[0]
similaridades_query = similaridade[indice_query]
indices_recomendados = similaridades_query.argsort()[-5:-1]  # Índices dos 4 endereços mais similares (excluindo o próprio)

# Imprimir os endereços recomendados
print("Endereços recomendados:")
for indice in indices_recomendados:
    print(dados_preparados.loc[indice, "Endereço"])
