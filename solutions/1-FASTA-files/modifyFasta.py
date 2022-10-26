from Bio import SeqIO

original_file = "reads.fasta"

output_handle = open(original_file, "r+")
for record in SeqIO.parse(original_file, "fasta"):
    opis = record.description
    razmaknuto = opis.split(" ")
    identifikator = razmaknuto[0]
    usmjerenost = razmaknuto[1].split("=")[1].replace(",","")
    start = razmaknuto[2].split("=")[1].replace(",","")
    duljina = len(record.seq)
    novo = str(identifikator) + " strand=" + str(usmjerenost) + ", " + "start=" + str(start) + ", " + "length=" + str(duljina)
    record.description = novo
    SeqIO.write(record, output_handle, "fasta")
output_handle.close()

