from Bio import SeqIO

reference_length=0
read_sequence_length=0

for record in SeqIO.parse("reference.fasta","fasta"):
    reference_length+=len(record.seq)

for record in SeqIO.parse("reads.fasta","fasta"):
    read_sequence_length+=len(record.seq)

print("The length of reference sequence is ",reference_length)
print("The length of combined sequence of reads is ",read_sequence_length)
print("The coverage is ",read_sequence_length/reference_length)
