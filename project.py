import os
import pandas as pd  # Biblioteca p/ trabalhar com base de dados.
import plotly.express as px  # Biblioteca p/ plotar gráficos.

"""Array c/ nome de todos os arquivos dentro de um diretório."""
files_list = os.listdir("./Vendas")
consolidated_table = pd.DataFrame()  # Tabela vazia.

for file in files_list:
    if "vendas" in file.lower():  # Passa o nome dos arquivos para lowercase.
        single_table = pd.read_csv(f"./Vendas/{file}")  # Lê arquivos CSV
        consolidated_table = consolidated_table.append(
            single_table
        )  # União de tabelas

# Seleciona apenas 3 colunas da tabela consolidada.
consolidated_table_clean = consolidated_table[
    ["Produto", "Quantidade Vendida", "Preco Unitario"]
]

#  Criando a coluna "Faturamento":
consolidated_table_clean["Faturamento"] = (
    consolidated_table_clean["Quantidade Vendida"]
    * consolidated_table_clean["Preco Unitario"]
)

#  Criando a Tabela "Faturamento por Produto":
revenue_by_class_of_product = (
    consolidated_table_clean.groupby("Produto")
    .sum()[["Faturamento"]]
    .sort_values(by="Faturamento", ascending=False)
)

# Gráfico "Faturamento por Produto":
chart = px.bar(
    x=consolidated_table_clean["Produto"],
    y=consolidated_table_clean["Faturamento"],
    title="Faturamento por Produto",
)
chart.write_html("revenue.html", auto_open=True)
