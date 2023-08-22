import pandas as pd
import ast


df_muts = pd.read_csv("mutacoes_clade.tsv",sep="\t")
dic_clade_mut = {}

for idx, linha in df_muts.iterrows():

    temp_dic = ast.literal_eval(linha.mutations)
    dic_clade_mut[linha.clade] = (temp_dic, linha.n_samples)

dic_clade_del = {}
temp_dic_dic = {}
# print(dic_clade_mut)
# exit()

for linhagem, lista_mut_freq in dic_clade_mut.items():

    temp_list = []
    temp_dic_dic = {}
    for mut in lista_mut_freq[0]:

        if mut.split("_")[-1] == '-':
            pos_mut = int(mut.split('_')[1])
            freq_mut = float(lista_mut_freq[0][mut])
            if temp_list == []:
                temp_list.append([pos_mut, freq_mut])
            else:
                if temp_list[-1][0] + 1 == pos_mut:
                    temp_list.append([pos_mut, freq_mut])
                else:
                    temp_dic_dic[f'del_{temp_list[0][0]}_{temp_list[-1][0]}'] = sum([freq[-1] for freq in temp_list])/len(temp_list)
                    # temp_list_list.append([temp_list[0][0], temp_list[-1][0], sum([freq[-1] for freq in temp_list])/len(temp_list)])
                    # temp_list = [[pos_mut, freq_mut]]
        else:
            if temp_list != []:
                temp_dic_dic[f'del_{temp_list[0][0]}_{temp_list[-1][0]}'] = sum([freq[-1] for freq in temp_list])/len(temp_list)
                temp_list = []
            temp_dic_dic[mut] = lista_mut_freq[0][mut]
    dic_clade_del[linhagem] = temp_dic_dic

#print(dic_clade_del)
df_muts = pd.DataFrame([[chave, valor] for chave, valor in dic_clade_del.items()], columns=["clade", "mutations"])

df_muts.to_csv("mutacoes_del_clade.tsv",sep="\t", index=False)
