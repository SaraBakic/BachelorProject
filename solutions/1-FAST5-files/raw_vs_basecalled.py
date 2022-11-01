from ont_fast5_api.fast5_interface import get_fast5_file
from ont_fast5_api.analysis_tools.base_tool import BaseTool
from ont_fast5_api.analysis_tools.basecall_1d import Basecall1DTools
from ont_fast5_api.analysis_tools.segmentation import SegmentationTools
import numpy as np 

#here we will store all aditional info
add_inf_list=[]

#In order to see what additional information basecalling provides, I will use two reads
# , one raw, and its basecalled counterpart
#I am using GXB01103_20180501_FAH86018_GA30000_mux_scan_CHM13_1_36685_read_11_ch_252_strand read, 
# but have renamed it as base and raw for the sake of simplicity

base_str ="base.fast5" 
raw_str="raw.fast5"

base_f5=get_fast5_file(base_str, mode="r+")
raw_f5=get_fast5_file(raw_str, mode="r+")

#since there are 3 main branches in FAST5 format: Raw, Analyses, UniqueGlobalKey, 
#and ont-fast5-api functions are heavily focused on Analyses branch
#I will check for differences in Raw and UniqueGlobalKey branches before Analyses

#unfortunately, looking through the source code of ont-fast5-api, I havent been able to find(or recognize :) ) functions 
#that analyze UniqueGlobalKey branch, so I used h5dump -A -g "/UniqueGlobalKey" base.fast5 and
#h5dump -A -g "/UniqueGlobalKey" raw.fast5 commands on karla server, got the outputs,
#and inserted them in online text comparators to check for differences, which there were none
#so I have concluded that basecalling doesnt alter the UniqueGlobalKey branch of the fast5 format
#one down, two to go

print("Basecalled signal and raw signal fast5 file has same UniqueGlobalKey branch")

#speaking from my small knowledge of fast5 format, I doubt there are differences in Raw branches of the files,
#but "assumptions are made and most assumptions are wrong", at least according to Einstein, so I used
#some functions I found from ont-fast5-api and checked it

base_raw_data=base_f5.get_raw_data()
raw_raw_data=raw_f5.get_raw_data()

if(len(base_raw_data)==len(raw_raw_data)):
    print("Basecalled raw signal data and raw signal data length are the same")

#this if gave us the answer that the length is same, lets continue checking
same=True
for i in range(len(base_raw_data)):
    if(base_raw_data[i]!=raw_raw_data[i]):
        same=False
if(same):
    print("They have same raw data!")
else:
    print("They dont have same raw data!")

#here I found out both reads have same raw data, which means Raw branch is also same with raw and basecalled signals
#time for the Analyses branch

#firstly, lets find out which analyes both files have

raw_analyses=raw_f5.list_analyses()
base_analyses=base_f5.list_analyses()
print("Raw analyses: ",raw_analyses)
print("Base analyses: ",base_analyses)

#here we find out that raw fast5 only branches to ('basecall_1d', 'Basecall_1D_000') analyses
#we find out that base fast5 branches to ('basecall_1d', 'Basecall_1D_000'), ('basecall_1d', 'Basecall_1D_001'), ('segmentation', 'Segmentation_000') analyses
#well, lets compare their analyses

#lets start with Basecall_1D_000

#we will use function get_summary_data() and basecall_1d tools

print(raw_f5.get_summary_data("Basecall_1d_000"))
print(base_f5.get_summary_data("Basecall_1d_000"))

#both dont have any data in here, but I went to manually check with h5dump and it seems that there is a 
#fastq hidden inside, lets check

raw_tool=Basecall1DTools(raw_str,mode="r+",group_name="Basecall_1D_000")
raw_seq=str(raw_tool.get_called_sequence("template", fastq=False))
print(raw_seq)
base_tool=Basecall1DTools(base_str,mode="r+",group_name="Basecall_1D_000")
base_seq=str(base_tool.get_called_sequence("template", fastq=False))
print(base_seq)
if(raw_seq==base_seq):
    print("They have the same sequence!")

#here I was a bit surprised, because it seems that even a raw signal has a fastq stored inside it, which is equal to a basecalled signal
#is it possible somehow that the raw signal was also basecalled once?
#could that be why we have basecall_1D_000 in both and basecall_1D_001 in both, because basecalled signals get additional basecalling?

#now lets analyse BASECALL_1D_001 branch of analyses
print(raw_f5.get_summary_data("Basecall_1D_001"))
print(base_f5.get_summary_data("Basecall_1D_001"))

#raw doesnt have anything
#so everything here is additional information
#lets add it
add_inf_list.append(str(base_f5.get_summary_data("Basecall_1D_001")))

#lets check for fastq files hidden inside
base_tool1=Basecall1DTools(base_str,mode="r+",group_name="Basecall_1D_001")
base_seq1=str(base_tool.get_called_sequence("template", fastq=False))
print(base_seq1)
#this is also an additional information
add_inf_list.append("Additional FASTQ file: "+base_seq1)

#now, lets check the last analyses, Segmentation_000
print(base_f5.get_summary_data("Segmentation_000"))
#everything here is also additional information
add_inf_list.append(str(base_f5.get_summary_data("Segmentation_000")))

seg_tool=SegmentationTools(base_str,mode="r+",group_name="Segmentation_000")

#that wraps it up
#now I will write all differences I found in a file

f=open("differences.txt","w")
f.write("Additional information stored in basecalled fast5 files\n")
for line in add_inf_list:
    f.write(line)
    f.write("\n \n \n")
f.close()