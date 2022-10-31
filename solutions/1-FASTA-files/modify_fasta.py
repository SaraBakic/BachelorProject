from Bio import SeqIO

output=open("reads.fasta","r+")
for record in SeqIO.parse("reads.fasta","fasta"):
    record_desc_list=record.description.split(", ")
    record_desc_list[2]="length="+str(len(record.seq))
    record.description=record_desc_list[0]+", "+record_desc_list[1]+", "+record_desc_list[2]
    SeqIO.write(record,output,"fasta")
output.close()