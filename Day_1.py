#%% 
# O seu primeiro passo é unificar em um único Dataframe todos os dados pertinentes para a análise.
# Comece pelos empréstimos e você terá os dados das transações.
# Depois, mescle com os dados do acervo, para que você possa entender, por exemplo, de qual biblioteca era o material emprestado ou a qual tema ele se referia.
# Elas se relacionam pela coluna de código de barras de cada material.

#%% Lendo Arquivo csv
import pandas as pd

emprestimos = pd.read_csv(r"D:\OneDrive\MIGUEL\Programação\Python\7DaysOfCode-Alura\7_Days_of_Code_Alura-Python-Pandas\Dia_1-Importando_dados\Datasets\dados_emprestimos\emprestimos-20101.csv")

# %% Lendo um conjunto de arquivos csv
# Para ler vários arquivos csv de uma vez, em ambiente local
# é possível você usar a biblioteca 'glob' e 'os' para localizar os arquivos
# e 'pandas' usando de um laço (no caso 'for') para ler e concatenar os dados.
import pandas as pd
import os
import glob

path_emprestimos = r"D:\OneDrive\MIGUEL\Programação\Python\7DaysOfCode-Alura\7_Days_of_Code_Alura-Python-Pandas\Dia_1-Importando_dados\Datasets\dados_emprestimos"
arquivo_emprestimos = glob.glob((os.path.join(r"D:\OneDrive\MIGUEL\Programação\Python\7DaysOfCode-Alura\7_Days_of_Code_Alura-Python-Pandas\Dia_1-Importando_dados\Datasets\dados_emprestimos","*csv")))

emprestimos = pd.concat([pd.read_csv(arquivo) for arquivo in arquivo_emprestimos],ignore_index=True)
#%% Lendo arquivo parquet
# O arquivo parquet é um formato de arquivo colunar, similar a um RDBMS,
# que permite uma leitura mais eficiente de grandes volumes de dados.
transações = pd.read_parquet(r"https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/48684f508c0c9ad1d51975c72091b160dee66db4/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet")

# %% Unindo os dados
# A união dos dados pode ser feita através do método 'merge' do pandas.
dados_biblioteca = pd.merge(emprestimos, transações, on='codigo_barras', how='left')
