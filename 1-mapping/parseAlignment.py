import re

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

file_name = "alignment.sam"
file1 = open(file_name, "r")

file_name2 = "output.txt"
file2 = open(file_name2, "w")

lines = file1.readlines()

count=0

for line in lines:
    count+=1
    if count<3:
        continue
    else:
        line = _RE_COMBINE_WHITESPACE.sub(" ", line).strip()
        novo = line.split(' ')
        if novo[2]=='*':
            continue
        if count==3:
            numberOfReads = 1
            identifikator = novo[0]
            identifikatorPrije = identifikator
            start = novo[3]
            kvaliteta = novo[4]
            avg = kvaliteta
        else:
            identifikator = novo[0]
            if identifikator == identifikatorPrije:
                numberOfReads +=1
                zbroj += int(novo[4])
                start += ", " + novo[3]
                avg = (zbroj/numberOfReads)
            else:
               	file2.write(identifikatorPrije + "    " + str(numberOfReads) + "    " + start + "    " + str(avg) + "\n")
                start = novo[3]
                kvaliteta = int(novo[4])
                zbroj = kvaliteta
                avg = kvaliteta
                numberOfReads = 1
                if count == 32784:
                    file2.write(identifikator + "    " + str(numberOfReads) + "    " + start + "    " + str(avg) + "\n")
            identifikatorPrije = identifikator
            
file1.close()
file2.close()


