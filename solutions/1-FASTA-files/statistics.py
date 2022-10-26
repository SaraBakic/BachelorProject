from Bio import SeqIO

duljina=0
suma=0
shortest_read=-1
for record in SeqIO.parse("A.fasta", "fasta"):
	duljina+=1
	suma+=len(record.seq)
	if len(record.seq) < shortest_read or shortest_read < 0:
		shortest_read = len(record.seq)
	
print("The shortest read in the file is this large: " + str(shortest_read))
print(str(duljina) + " reads are contained in the file")
print("The average length of a file is: " + str(round(suma/duljina)))
