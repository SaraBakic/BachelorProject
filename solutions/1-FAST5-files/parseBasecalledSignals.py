from ont_fast5_api.analysis_tools.base_tool import BaseTool
from ont_fast5_api.fast5_interface import get_fast5_file
from ont_fast5_api.analysis_tools.basecall_1d import Basecall1DTools
import os
import matplotlib.pyplot as plt

directory1 = "/home/ivan/BachelorProject/1-FAST5-files/basecalled_signals"
directory2 = "/home/ivan/BachelorProject/1-FAST5-files/raw_signals"

count=0

for filenameB in os.listdir(directory1):
	basecalled_info = "Additional info:" + "\n"
	count+=1
	provjera = True
	pathB = os.path.join(directory1, filenameB)
	fast5FileB = get_fast5_file(pathB, mode='r', driver=None)
	basecalled = fast5FileB.get_raw_data()
	for filenameR in os.listdir(directory2):
		if filenameR == filenameB:
			pathR = os.path.join(directory2, filenameR)
			fast5FileR = get_fast5_file(pathR, mode='r', driver=None)
			raw = fast5FileR.get_raw_data()
			#for loop is here to check if all the elements in two arrays are the same
			for i in range(len(raw)):
				if raw[i]!=basecalled[i]:
					provjera = False
					break
					
			# Basecall_1D_000 is the same for raw and basecalled	
			groupsR = fast5FileR.list_analyses()
			groupsB = fast5FileB.list_analyses()
			summaryR = fast5FileR.get_summary_data("Basecall_1D_001")
			summaryB = fast5FileB.get_summary_data("Basecall_1D_001")
			if summaryR == None and summaryB != None :
				basecalled_info += str(count) + ". " + str(pathB.replace(directory1 + "/", "") + "\n" + "\n" + str(summaryB) + "\n" + "\n")
				
			segmentationR = fast5FileR.get_summary_data("Segmentation_000")
			segmentationB = fast5FileB.get_summary_data("Segmentation_000")
			if summaryR == None and summaryB != None :
				basecalled_info += str(segmentationB) + "\n" + "\n"
			
			tool = 	Basecall1DTools(fast5FileB, mode="r+", group_name="Basecall_1D_001")
			seq = str(tool.get_called_sequence("template", fastq=False))
			basecalled_info += "Additional sequence in group Basecall_1D_001: "
			basecalled_info += seq + "\n" +"\n"
			print(basecalled_info)
							
			print("Check elements: " + "\n")
			if provjera:
				print("Raw and basecalled are the same length for file: " + filenameB)
			else:
				print("Raw and basecalled are not the same length for file: " + filenameB)	
			print("\n")
			

			break
			
			
