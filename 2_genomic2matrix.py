import pandas as pd
from Bio import SeqIO

arquivo = "masked_RSV_A_nextclade_align.fasta"

with open(arquivo) as align:
    dic_samples = {record.id: record.seq for record in SeqIO.parse(align,'fasta')}


df = pd.DataFrame([[nome.split("|")[0],nome.split("|")[1]]+list(str(sequencia)) for nome, sequencia in dic_samples.items()])

df.columns = ["id","clade"]+[i for i in range(1,len(df.columns)-2+1)]

#df['date'] =  pd.to_datetime(df['date'], format='%Y-%m-%d')

df = df.sort_values(by='clade')

print(df)

df.to_csv("alin_ref_matrix.tsv",sep='\t',index=False)