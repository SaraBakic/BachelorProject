import os
from ont_fast5_api.fast5_interface import get_fast5_file
import numpy as np
import matplotlib.pyplot as plt

def get_raw(filename):
    fast5_filepath = filename 
    with get_fast5_file(fast5_filepath, mode="r") as f5:
        for read in f5.get_reads():
            raw_data = read.get_raw_data()
            
    return raw_data



directory="C:\\Users\\Matija\\Desktop\\BachelorProject\\Phase1\\raw_signals"


plt.figure(1,[100,10])
for filename in os.listdir(directory):
    f=os.path.join(directory,filename)
    
    
    if os.path.isfile(f):
        raw_data=get_raw(directory+"\\"+filename)
        plt.figure(1,[20,5])
        plt.plot(raw_data)
        plt.title("Name: "+ filename+"\n"+" Read length: "+str(len(raw_data))+"\n"+"Mean: "+str(np.mean(raw_data)))
        plt.show()

plt.show()


            
        

