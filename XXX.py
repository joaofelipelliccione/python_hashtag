import os  # Biblioteca p/ trabalhar com File System.
import pandas as pd  # Biblioteca p/ trabalhar com base de dados.

"""Array c/ nome de todos os arquivos dentro de um diretório."""
file_list = os.listdir("./Vendas")
consolidated_table = pd.DataFrame()  # Tabela vazia.

for file in file_list:
    if "vendas" in file.lower():  # Passa o nome dos arquivos para lowercase.
        single_table = pd.read_csv(f"./Vendas/{file}")  # Lê arquivos CSV
        consolidated_table = consolidated_table.append(single_table)


print(consolidated_table)
