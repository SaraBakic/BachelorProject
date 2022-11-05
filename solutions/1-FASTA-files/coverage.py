from Bio import SeqIO

duljina=0
reference = SeqIO.parse('reference.fasta', 'fasta')
for record in reference:
	duljina+=len(record.seq)
print("The length of the reference sequence is: " + str(duljina))

sequences = SeqIO.parse('reads.fasta', 'fasta')
sum = 0
for record in sequences:
	sum+=len(record.seq)
print("The length of combined sequence of the reads is: " + str(sum))

print("The coverage of the given dataset is: " + str(sum/duljina))
