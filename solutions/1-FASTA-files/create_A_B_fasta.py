from Bio import SeqIO

idA=1
idB=1

fileA=open("A.fasta","w")
fileB=open("B.fasta","w")


for record in SeqIO.parse("reads.fasta","fasta"):
    record_desc_list=record.description.split(", ")
    start=int(record_desc_list[1].split("=")[1])

    if(start>=500000 and start<=600000):
        record_desc_list[0]=str(idA) + " "+record_desc_list[0].split(" ")[1]
        record.id=str(idA)
        record.description=record_desc_list[0]+", "+record_desc_list[1]+", "+record_desc_list[2]
        idA+=1
        SeqIO.write(record,fileA,"fasta")
    elif(start>=1500000 and start <=1600000):
        record_desc_list[0]=str(idB) + " "+record_desc_list[0].split(" ")[1]
        record.id=str(idB)
        record.description=record_desc_list[0]+", "+record_desc_list[1]+", "+record_desc_list[2]
        SeqIO.write(record,fileB,"fasta")
        idB+=1
fileA.close()
fileB.close()

reference_length=0
for record in SeqIO.parse("reference.fasta","fasta"):
    reference_length+=len(record.seq)

lengthA=0
for record in SeqIO.parse("A.fasta","fasta"):
    lengthA+=len(record.seq)

lengthB=0
for record in SeqIO.parse("B.fasta","fasta"):
    lengthB+=len(record.seq)

print("The coverage of A.fasta is: ",lengthA/reference_length)
print("The coverage of B.fasta is: ",lengthB/reference_length)

print("The coverage of A.fasta is barely larger, that could be because a few reads from start positions 500000-600000 could be slightly larger than their 1500000-1600000 counterparts")
    