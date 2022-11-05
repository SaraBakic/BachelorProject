import os
from ont_fast5_api.fast5_interface import get_fast5_file
import matplotlib.pyplot as plt
import numpy as np

directory = "/home/ivan/BachelorProject/1-FAST5-files/raw_signals"

count=0

for filename in os.listdir(directory):
	count+=1
	path = os.path.join(directory, filename)
	fast5File = get_fast5_file(path, mode='r', driver=None)
	data = fast5File.get_raw_data()
	plt.plot(data)
	plt.title(str(count) + ". " + str(path.replace(directory + "/", "")))
	plt.show()
	print(str(count) + ". signal")
	print("Length of raw data: " + str(len(data)))
	print("Mean of raw data: " + str(np.mean(data)) + "\n")


