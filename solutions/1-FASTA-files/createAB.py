from Bio import SeqIO

original_file = "reads.fasta"
A_file = "A.fasta"
B_file = "B.fasta"

output_handle1 = open(A_file, "w")
output_handle2 = open(B_file, "w")

identifikatorA = 1
identifikatorB = 1

for record in SeqIO.parse(original_file, "fasta"):
	opis = record.description
	razmaknuto = opis.split(" ")
	start1 = razmaknuto[2].split("=")
	start2 = start1[1]
	start2 = start2.replace(",", "")
	if int(start2) >= 500000 and int(start2) <= 600000:
		rekordA = record.id
		if rekordA != identifikatorA:
			rekordA = str(identifikatorA)
		record.id = rekordA	
		record.description = razmaknuto[1] + " " + razmaknuto[2] + " " + razmaknuto[3]
		SeqIO.write(record, output_handle1, "fasta")
		identifikatorA+=1
	elif int(start2) >= 1500000 and int(start2) <= 1600000:
		rekordB = record.id
		if rekordB != identifikatorB:
			rekordB = str(identifikatorB)
		record.id = rekordB	
		record.description = razmaknuto[1] + " " + razmaknuto[2] + " " + razmaknuto[3]
		SeqIO.write(record, output_handle2, "fasta")
		identifikatorB+=1
output_handle1.close()
output_handle2.close()	

duljina=0
reference = SeqIO.parse('reference.fasta', 'fasta')
for record in reference:
	duljina+=len(record.seq)
	
sequences = SeqIO.parse('A.fasta', 'fasta')
sumA = 0
for record in sequences:
	sumA+=len(record.seq)

sequences = SeqIO.parse('B.fasta', 'fasta')
sumB = 0
for record in sequences:
	sumB+=len(record.seq)
	
print("The coverage of set A is: " + str(sumA/duljina))
print("The coverage of set B is: " + str(sumB/duljina))

print("They are almost the same.")










