# Prática com Pandas - leitura e filtros de dados

import pandas as pd

arquivo = pd.read_excel("base_treinamento_seguros_python.xlsx")


# Filtro por status Pendente

pendentes = arquivo[arquivo["Status"] == "Pendente"]

print(pendentes)
print(arquivo["Status"])


# Identificação dos diferentes status

print(arquivo["Status"].unique())


# Filtro por status Em análise

em_analise = arquivo[arquivo["Status"] == "Em análise"]

print(em_analise)


# Filtro por status Aguardando documento

aguardando_documento = arquivo[arquivo["Status"] == "Aguardando documento"]

print(aguardando_documento.head())

quantidade_aguardando = len(aguardando_documento)

print(quantidade_aguardando)


# Filtro de registros diferentes de Aguardando documento

documento_observacao = arquivo[arquivo["Status"] != "Aguardando documento"]

print(documento_observacao.head())

print(len(documento_observacao))

print(documento_observacao["Status"].unique())