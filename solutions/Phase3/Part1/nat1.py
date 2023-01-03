import re
_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

file_name = "bedGraph_CpG_nat1.bedGraph"
file = open(file_name, "r")
lines = file.readlines()
countSum = 0
countLines = 0
countNonM = 0
countM = 0
for line in lines:
	if countLines==0:
		countLines+=1
	else:
		line = _RE_COMBINE_WHITESPACE.sub(" ", line).strip()
		parsed = line.split(' ')
		if int(parsed[3])==0:
			countNonM+=1
		if int(parsed[3])==100:
			countM+=1
		countLines+=1
		countSum += int(parsed[3])
file.close()

percentage = countSum/countLines

print("Total number of 0% methylation CpG sites: " + str(countNonM))
print("Total number of 100% methylation CpG sites: " + str(countM))
print("Total number of CpG sites: " + str(countLines))
print("Average percentage of methylation CpG sites: " + str(round(percentage,4)) + "%")
