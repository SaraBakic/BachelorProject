from Bio import SeqIO

i=0
total_length=0
num_of_reads=0
shortest_read=0
for record in SeqIO.parse("A.fasta","fasta"):
    if(i==0):
        shortest_read=len(record.seq)
        i+=1
    num_of_reads+=1
    total_length+=len(record.seq)
    if(len(record.seq)<shortest_read):
        shortest_read=len(record.seq)
    
print("Length of the shortest read is ",shortest_read)
print("There are ",num_of_reads,"reads in file")
print("Average length of a read is ",total_length/num_of_reads)