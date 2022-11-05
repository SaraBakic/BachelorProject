from Bio import SeqIO
import os
from ont_fast5_api.fast5_interface import get_fast5_file
from ont_fast5_api.analysis_tools.base_tool import BaseTool
from ont_fast5_api.analysis_tools.basecall_1d import Basecall1DTools
import collections

file1 = "/home/ivan/basecalled/basecallled/fastq_runid_c755b15f8f55d8df50b420a6932c41e787fb781f_0.fastq"
file2 = "/home/ivan/basecalled/basecallled/fastq_runid_c755b15f8f55d8df50b420a6932c41e787fb781f_1.fastq"
folder = "/home/ivan/BachelorProject/1-FAST5-files/basecalled_signals"
output_file = "/home/ivan/Vjezbe/diff.txt"

records_guppy = {}
records_basecalled = {}

for record in SeqIO.parse(file1, "fastq"):
	records_guppy[record.id] = record.seq
for record in SeqIO.parse(file2, "fastq"):
	records_guppy[record.id] = record.seq
	
for file in os.listdir(folder):
	path = os.path.join(folder,file)
	fast5File = get_fast5_file(path, mode="r+")
	tool = Basecall1DTools(path, mode="r+", group_name="Basecall_1D_001")
	key = fast5File.get_read_id()
	seq = tool.get_called_sequence("template", fastq=False)
	records_basecalled[key] = seq[1]
	
f=open("diff.txt", "w")
f.write
	
for key in records_guppy.keys():
	f.write("Sequence id: " + key + "\n")
	guppyValue = str(records_guppy[key])
	basecalledValue = str(records_basecalled[key])	
	g=False
	b=False
	lenG = len(guppyValue)
	lenB = len(basecalledValue)
	diff = abs(lenG - lenB)
	if(lenG == lenB):
		f.write("They are the same length.\n")
	elif (lenG > lenB):
		f.write("Guppy basecalled sequence is " + str(diff) + " nucleotides longer.\n")
		g=True
	else:
		f.write("Basecalled sequence is " + str(diff) + " nucleotides longer.\n")
		b=True
	longer = max(lenG, lenB)
	diff_index = {}
	differences=0
	i=0
	if g:
		while i<lenG:
			if(i>=lenB):
				diff_index[i] = {guppyValue[i], "/"}
				differences+=1
			else:
				if(guppyValue[i] != basecalledValue[i]):
					diff_index[i] = {guppyValue[i], basecalledValue[i]}
					differences+=1
			i+=1
	elif b:
		while i<lenB:
			if(i>=lenG):
				diff_index[i] = {"/", basecalledValue[i]}
				differences+=1
			else:
				if(guppyValue[i] != basecalledValue[i]):
					diff_index[i] = {guppyValue[i], basecalledValue[i]}
					differences+=1
			i+=1
	else:
		while i<lenG:
			if(guppyValue[i] != basecalledValue[i]):
				diff_index[i] = {guppyValue[i], basecalledValue[i]}
				differences+=1
			i+=1
	for kljuc in diff_index.keys():
		f.write("Index on which the difference occurs: " + str(kljuc) + "\n")
		f.write("The difference: " + str((diff_index[kljuc])) + "\n")
	f.write("The total number of differences: " + str(differences))
	f.write("\n \n \n")
f.close()


