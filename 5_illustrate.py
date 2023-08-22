import pandas as pd
import subprocess
import time
import ast
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
from datetime import datetime

start_time = time.time()

df_muts = pd.read_csv("mutacoes_clade.tsv",sep="\t")


dic_clade_mut = {}
# print(df_muts)
for idx, linha in df_muts.iterrows():

    temp_dic = ast.literal_eval(linha.mutations)
    dic_clade_mut[linha.clade] = (temp_dic, linha.n_samples)



lista_mutacoes = set([v for valor in dic_clade_mut.values() for v in valor[0].keys()])
lista_clade = [clade+f" ({mut_num[1]})" for clade, mut_num in dic_clade_mut.items()]
# lista_meses.sort(key=lambda x: x.split(' ')[0])
# print(lista_meses)
lista_mutacoes = sorted(lista_mutacoes, key=lambda mut: int(mut.split('_')[1]))

input_heatmap = []
for mes, mutacao in dic_clade_mut.items():
    temp_list = []
    for mut in lista_mutacoes:
        if mut in mutacao[0].keys():
            temp_list.append(float(mutacao[0][mut]))
        else:
            temp_list.append(0)
    input_heatmap.append(temp_list)

df_heatmap = pd.DataFrame(input_heatmap, index=lista_clade,columns=lista_mutacoes)
print(df_heatmap)
df = df_heatmap.loc[:, df_heatmap.mean() < 0.95]

df = df.loc[:, df.mean() > 0.30]

#new_order = sorted(lista_clade, key=lambda m: datetime.strptime(m.split(' ')[0], "%b-%Y"))
#Talvez no futuro ordenar por algo

#df = df.reindex(new_order, axis=0)


# G3328T:"Q1021H"
# C4795T
# C6267T:"A2001V"
# C10376T:"P3371S"
# orf1a
# G21123T
# ORF1b
# T22032C:F157S
# S
# C28498T:ORF9a:"T72I"

# dic_conversao_manual ={
# "C1931A":'ORF1a:Q556K',
# 'C2790T':'ORF1a:T842I',
# 'C11750T':'ORF1a:L3829F',
# 'T14257C':'ORF1b:Y264H',
# 'G16935A':'ORF1b:M1156I',
# 'A17039G':'ORF1b:N1191S',
# 'C22674T':'S:S371F',
# 'T22882G':'S:N440K',
# 'A22893C':'S:K444T',
# 'T22942A':'S:N460K',
# '26270T':'E:T9IC',
# 'C28312T':'N:P13L',
# 'G28681T':'N:E136D',
# 'C26270T':'E:T9I',
# 'T28693C':'N:T28693C',
# 'del515520':'ORF1a:del84/85',
# 'del2199221994':'S:del144',
# 'del2750827750':'ORF7a:del39/119'
# }
# # print(df)
# novas_colunas = []
# for coluna in df.columns:
#     if 'del' in coluna:
#         if ''.join(coluna.split("_")) in dic_conversao_manual:
#             novas_colunas.append(dic_conversao_manual[''.join(coluna.split("_"))])
#         else:

#             novas_colunas.append(f'del{coluna.split("_")[1]}/{coluna.split("_")[2]}')
#     else:
#         if ''.join(coluna.split("_")) in dic_conversao_manual:
#             novas_colunas.append(dic_conversao_manual[''.join(coluna.split("_"))])
#         else:
#             novas_colunas.append(''.join(coluna.split("_")))

# df.columns = novas_colunas

#df.to_csv("evolucao_mutacoes.tsv",sep='\t')

# print(df)
# exit(0)
ax = sns.heatmap(df,xticklabels=True, vmax = 1,vmin = 0, cbar_kws={"orientation": "horizontal"}, linewidths=.001, linecolor="black", cmap="Blues")
plt.xticks(rotation=90)
plt.tick_params(axis="x", which='major', labelsize=7.8)
plt.show()

print("--- %s seconds ---" % (time.time() - start_time))