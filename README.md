# Construção do Heatmap

## Script 1 (masked_end_align:
- Input: Sequência FASTA alinhada contra uma referência.
- Output: FASTA sem Gaps "-", substituido por "N"
- OBS1: A referência precisa estar escrita como "reference"
- OBS2: O código de ambas as amostras deve estar separado por "|" de acordo com o padrão estipulado
![image](https://github.com/ACMElab-Fioce/heatmap/assets/98467661/9eb2e5f2-5a17-425b-9537-9b9a0ccd0b25)


## Script 2 (genomic2matrix):
- Input: FASTA sem Gaps "-", substituido por "N"
- Output: Arquivo TSV onde a primeira coluna é o nome da sequência, a segunda coluna é a acaracterística separada por "|"
e o restante das colunas o nucleotídeo referente à sequência alinhada com a referência (A, C, T, G, N)
- OBS: A linhado arquivo tsv contendo a referência deve estar na primeira posição para dar continuidade, caso não
esteja é necessário que o usuário faça a alteração manualmente.
![image](https://github.com/ACMElab-Fioce/heatmap/assets/98467661/120c5784-f2fc-4ede-bf00-eeb465a5a140)


## Script 3 (align_sequences):
- Input: Arquivo TSV
- Output: Arquivo TSV com os valores em porcentagem da presença de mutações, separado por característica
![image](https://github.com/ACMElab-Fioce/heatmap/assets/98467661/9b926dd6-37a6-4285-892a-df15fbb6af30)

