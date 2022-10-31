from ont_fast5_api.fast5_interface import get_fast5_file
import numpy as np 

# a little function that will be helpful further down the line
def dictionary_comparator(raw_an_base_id,base_an_base_id,keyv):
    dict_raw1=raw_an_base_id[keyv]
    dict_base1=base_an_base_id[keyv]
    same=True
    dict_raw1_keys=raw_an_base_id[keyv].keys()
    dict_base1_keys=base_an_base_id[keyv].keys()
    
    same=True
    if(dict_raw1_keys==dict_base1_keys):
        print(keyv," They have same keys")
        for key in dict_raw1_keys:
            if(dict_raw1[key]!=dict_base1[key]):
                print("They are different in ",key," parameter")
                same=False
        if(same):
            print(keyv," Dictionaries are same")
    else:
        print(keyv," They dont have same keys, therefore, they are not the same dictionaries")
    
def store_differences(list,analyses,raw_an_base_id,base_an_base_id,keyv):
    dict_raw1=raw_an_base_id[keyv]
    dict_base1=base_an_base_id[keyv]
    for key in dict_raw1.keys():# shared key, different value 
        if key in dict_base1:
            if dict_raw1[key]!=dict_base1[key]:
                string="Analyses: "+str(analyses)+"| dictionary key: "+keyv+"| Parameter of difference=>  "+key+": "+dict_base1[key]
                list.append(string)
    for key in dict_base1.keys(): #keys exclusive to basecalled reads
        if key not in dict_raw1:
                string="Analyses: "+str(analyses)+"| dictionary key: "+keyv+"| Parameter of difference=> "+key+": "+dict_base1[key]
                list.append(string)
            

#after reading the source code of the ont-fast5-api library, I have decided to use list_analyses() and read_summary_data() to find out
#which additional information basecalling provides

#I will use two reads to find this, one raw, and its basecalled counterpart
#I am using GXB01103_20180501_FAH86018_GA30000_mux_scan_CHM13_1_36685_read_11_ch_252_strand read, but have renamed it as base and raw for the sake of simplicity


base_str = "base.fast5" 
raw_str="raw.fast5"

base_f5=get_fast5_file(base_str, mode="r")
raw_f5=get_fast5_file(raw_str, mode="r")

#since there are 3 main branches in FAST5 format: Raw, Analyses, UniqueGlobalKey, and the functions I have mentioned in first comment line only analyse Analyses branch,
#before I start, I have to check for differences in Raw and UniqueGlobalKey branches

#unfortunately, looking through the source code of ont-fast5-api, I havent been able to find(or recognize :) ) functions 
#that analyze UniqueGlobalKey branch, so I used h5dump -A -g "/UniqueGlobalKey" base.fast5 and
#h5dump -A -g "/UniqueGlobalKey" raw.fast5 commands on karla server, got the outputs,
#and inserted them in online text comparators to check for differences, which there were none
#so I have concluded that basecalling doesnt alter the UniqueGlobalKey branch of the fast5 format
#one down, two to go
print("Basecalled signal and raw signal fast5 file has same UniqueGlobalKey")

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

#in this list I will store all differences and additional information I find, it is the most important data structure of this analysis
list=[]
#firstly, lets find out which analyes both files have

raw_analyses=raw_f5.list_analyses()
base_analyses=base_f5.list_analyses()
print(raw_analyses)
print(base_analyses)

#here we find out that raw fast5 only branches to ('basecall_1d', 'Basecall_1D_000') analyses
#we find out that base fast5 branches to ('basecall_1d', 'Basecall_1D_000'), ('basecall_1d', 'Basecall_1D_001'), ('segmentation', 'Segmentation_000') analyses

#lets first compare the analyses branch that they both have,basecall_1d
#you may ask yourself why I check almost everything manually, writing code for every branch separately,
#instead of coming up with some comparation algorithm, thats because prior to this task I have never seen
#a fast5 format in my life, so I had little idea about the datatypes or any knowledge what to expect,
#so I just started manualy checking key by key 
print("basecall_1d analyses")
#analyses basecall_1d

raw_an_base_id=raw_f5.read_summary_data(raw_str,'basecall_1d') #this is a dictionary, found out using type()
base_an_base_id=base_f5.read_summary_data(base_str,'basecall_1d')

#lets find out their dict keys
raw_keys=raw_an_base_id.keys()
base_keys=base_an_base_id.keys()
print(raw_keys)
print(base_keys)

#they have same dictionary keys
#dict_keys(['tracking_id', 'channel_id', 'reads', 'software', 'data', 'filename'])
print("Raw and basecalled signals have same keys in analyses dictionary")

#well, lets check the differences for every key-value pair

for key in raw_keys:
    print(type(raw_an_base_id[key]))
    print(type(base_an_base_id[key]))
#it seems there are dictionaries inside our main dictionary, so we will have to go deeper
#<class 'dict'> <class 'dict'> <class 'list'> <class 'dict'> <class 'NoneType'> <class 'str'>- type of values of raw
#<class 'dict'> <class 'dict'> <class 'list'> <class 'dict'> <class 'dict'>    <class 'str'> -corresponding basecalled values



#I will go key by key
#key no.1 'tracking_id'

dictionary_comparator(raw_an_base_id,base_an_base_id,'tracking_id')
#NO DIFFERENCES FOUND

#key no.2 'channel_id'
dictionary_comparator(raw_an_base_id,base_an_base_id,'channel_id')
#NO DIFFERENCES FOUND

#for reads I already know from Raw branch that everything is same

#key no.4 'software'
dictionary_comparator(raw_an_base_id,base_an_base_id,'software')
#they dont share the same keys
store_differences(list,'basecall_1d',raw_an_base_id,base_an_base_id,'software')

#key no.5 'data'
#raw data has None for this, so everything is added to differences
for key in base_an_base_id['data'].keys():
    string="Analyses: "+str('basecall_1d')+"| dictionary key: "+"data"+"| Parameter of difference=> "+key+": "+str(base_an_base_id['data'][key])
    list.append(string)
#key no.6 'file'
#its logical that they are not the same in filename


#analyses segmentation
#raw_reads have no segmentation analyses, but I will have to compare it to dictionary of basecall_1d analyses of basecalled signals,
#because some information duplicates between segmentation and basecall_1d analyses
#the keys are same as before
print("Segmentation analyses: ")
segmentation_dict=base_f5.read_summary_data(base_str,'segmentation')

base_an_base_id=base_f5.read_summary_data(base_str,'basecall_1d')

#I will go key by key
#key no.1 'tracking_id'

dictionary_comparator(segmentation_dict,base_an_base_id,'tracking_id')
#NO DIFFERENCES FOUND

#key no.2 'channel_id'
dictionary_comparator(segmentation_dict,base_an_base_id,'channel_id')
#NO DIFFERENCES FOUND

#for reads I already know from Raw branch that everything is same

#key no.4 'software'
dictionary_comparator(segmentation_dict,base_an_base_id,'software')
#they have differenes
store_differences(list,"segmentation",segmentation_dict,base_an_base_id,'software')

if(not segmentation_dict['data']==base_an_base_id['data']):
    print("They dont have same data "+"\n")
#they have different data

#add difference in data
string="Analyses: "+"segmentation"+"| dictionary key: "+"data"+"| Parameter of difference=> "+key+": "+str(segmentation_dict['data'])
list.append(string)

print("EVERY DIFFERENCE AND ADDITIONAL INFORMATION IN BASECALLED FAST5 FILES:"+"\n"+"\n")
#lets print out every difference and additional informaton
for i in range(len(list)):
    print(list[i]+"\n")