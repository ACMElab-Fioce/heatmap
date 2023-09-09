import pandas as pd
import subprocess
import time
import ast
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
from datetime import datetime

start_time = time.time()

# Lendo conteúdo do arquivo TSV gerado anteriormente
df = pd.read_csv("alin_ref_matrix.tsv", sep='\t')
colunas = [str(i) for i in range(1, len(df.columns) + 1 - 2)]
ref = df.loc[df['id'] == "reference"][colunas]
df = df.loc[df['id'] != "reference"]

# Gerando novos arquivos TSV separando entre referencia e outras
ref.to_csv("temp_df_ref.tsv", sep='\t', index=False)
df.to_csv("temp_df.tsv", sep='\t', index=True)

# Continuação do código...
dic_clados_mut = {}
grupo_clados = df.groupby(by=["clade"])

for idx, grupo in grupo_clados:
    clado_nome = grupo["clade"].tolist()
    clado = clado_nome[0]
    num_amostras = len(clado_nome)   
    count_df = grupo[colunas].apply(pd.Series.value_counts).fillna(0).drop('N').transform(lambda x: x / x.sum()).fillna(0)
    count_df.to_csv(clado +".tsv",sep='\t')
    count_df_transpose = count_df.T
    # continue   
# exit()
    freq_min = 0.10
    nome_colunas = [x for x in count_df_transpose.columns] #ACTG

    temp_list = []
    temp_list_index = []
    mut_e_freq = {}

    for tupla, nuc_ref, pos in zip(count_df_transpose.iterrows(), ref.T[0].tolist(), count_df_transpose.index):
        linha = tupla[1]
        if float(linha[nuc_ref]) <= (1.0 - freq_min):
            for nuc in [nuc for nuc in count_df_transpose.columns if nuc != nuc_ref]:
                if float(linha[nuc]) >= freq_min:
                    mut_e_freq[nuc_ref+"_"+str(pos)+"_"+nuc] = str(linha[nuc])
                    temp_list.append([linha[x] for x in nome_colunas])
                    temp_list_index.append(pos)
    dic_clados_mut[clado] = (mut_e_freq, num_amostras)
# exit(0)
df_muts = pd.DataFrame([[chave, valor[0], valor[1]] for chave, valor in dic_clados_mut.items()], columns=["clade", "mutations","n_samples"])

df_muts.to_csv("mutacoes_clade.tsv",sep="\t", index=False)

print("--- %s seconds ---" % (time.time() - start_time))







