from ont_fast5_api.fast5_interface import get_fast5_file
from ont_fast5_api.analysis_tools.base_tool import BaseTool
from ont_fast5_api.analysis_tools.basecall_1d import Basecall1DTools
from ont_fast5_api.analysis_tools.segmentation import SegmentationTools
from Bio import SeqIO
import os
import numpy as np

#the output of guppy basecaller was two fastq files which contain total of 10 reads
#one log and js files and a sequencing summary.txt

path_guppy_out1="/home/mpintaric/BachelorProject/Phase1/Fast5Task/guppy_output/fastq1.fastq"
path_guppy_out2="/home/mpintaric/BachelorProject/Phase1/Fast5Task/guppy_output/fastq2.fastq"

guppy_sequences={}
#lets store basecalled sequences from guppyed raw signals
#first file
for record in SeqIO.parse(path_guppy_out1,"fastq"):
    guppy_sequences[record.id]=record.seq
#second file

for record in SeqIO.parse(path_guppy_out2,"fastq"):
    guppy_sequences[record.id]=record.seq

#now lets extract sequences from already basecalled signals
basecalled_sequences={}
directory_path="/home/mpintaric/BachelorProject/Phase1/Fast5Task/basecalled_signals"
for filename in os.listdir(directory_path):
    f=os.path.join(directory_path,filename)
    
    
    if os.path.isfile(f):
        f5=get_fast5_file(directory_path+"/"+filename,mode="r+")
        base_tool=Basecall1DTools(directory_path+"/"+filename,mode="r+",group_name="Basecall_1D_001")
        basecalled_sequences[f5.get_read_id()]=base_tool.get_called_sequence("template", fastq=False)[1]

dictionary_differences={}#here I will store all diferences
list_of_diff=[]
percentage_list_empty=[]
percentage_list_no_empty=[] #I will use this list to calculate the average percent of bases that are different
#I will have two lists, in one I will count all the differences, including positions where one sequence has bases
#and the other has *, and one list where I count the differences only where there are bases in both
#for every mismatch, I will add a tuple of 3 elements, first element=base from alreadye basecalled
#2 element=base from guppy basecalled, 3 element=position of mismatch, * means no Base at that position

for key in basecalled_sequences.keys(): #they have same keys
    
    seq_base=str(basecalled_sequences[key])
    seq_guppy=str(guppy_sequences[key])
    str_addition=""
    

    #percentage of mistakes calculation, without empty places
    differences=0
    for i in range(min(len(seq_base),len(seq_guppy))):
        if(seq_base[i]!=seq_guppy[i]):
            differences+=1
    percentage_list_no_empty.append(differences/min(len(seq_base),len(seq_guppy)))
    

    #fill shorter sequence with * at the end
    for i in range(min(len(seq_base),len(seq_guppy)),max(len(seq_base),len(seq_guppy))):
        str_addition+="*"
    if(len(seq_base)<len(seq_guppy)):
        seq_base+=str_addition
    elif(len(seq_guppy)<len(seq_base)):
        seq_guppy+=str_addition
    #they are the same now
    differences=0
    for i in range(len(seq_base)):
        if(seq_base[i]!=seq_guppy[i]):
            tuple_diff=(seq_base[i],seq_guppy[i],i)
            list_of_diff.append(tuple_diff)
        #percentage of mistakes, with empty places
            differences+=1
    percentage_list_empty.append(differences/len(seq_base))
    
        
    dictionary_differences[key]=list_of_diff
    list_of_diff=[]
print(dictionary_differences)


print("Average percent of different bases counting empty spaces: ",np.mean(percentage_list_empty)*100,"%")
print("Average percent of different bases not counting empty spaces: ",np.mean(percentage_list_no_empty)*100,"%")

#I will output this to txt file