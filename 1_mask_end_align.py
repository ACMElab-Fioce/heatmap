from Bio import SeqIO


samples_seq = 'RSV_A_nextclade_align.fasta'

with open(samples_seq) as seqs_samples:
    dic_samples = {record.id:record.seq for record in SeqIO.parse(seqs_samples,'fasta')}

with open("masked_"+samples_seq,'w') as file:

    for nome, sequencia in dic_samples.items():
        sequencia = str(sequencia)
        pos_init = 0
        pos_final = len(sequencia)
        temp_seq = ""
        for nuc in sequencia:
            if nuc not in ["A","T","G","C"]:
                pos_init += 1
            else:
                break
        for nuc in sequencia[::-1]:
            if nuc not in ["A","T","G","C"]:
                pos_final -= 1 
            else:
                break          
        temp_seq = "N"*(pos_init)+sequencia[pos_init:pos_final]+"N"*(len(sequencia)-pos_final)
        file.write(">"+nome+'\n')
        file.write(temp_seq+'\n')

        