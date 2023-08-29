# Construção do Heatmap

## Script 1:
- Input: Sequência FASTA alinhada contra uma referência.
- Output: FASTA sem Gaps "-", substituido por "N"
OBS1: A referência precisa estar escrita como "reference"
OBS2: O código de ambas as amostras deve estar separado por "|" de acordo com o padrão estipulado
![image](https://github.com/ACMElab-Fioce/heatmap/assets/98467661/9eb2e5f2-5a17-425b-9537-9b9a0ccd0b25)


## Script 2:
- Input: FASTA sem Gaps "-", substituido por "N"
- Output: Arquivo TSV onde a primeira coluna é o nome da sequência, a segunda coluna é a acaracterística separada por "|"
e o restante das colunas o nucleotídeo referente à sequência alinhada com a referência (A, C, T, G, N)
