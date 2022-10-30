import numpy as np

#the idea is to store information  about each line, then go to the next line
#if it is concluded in the next line that it doesnt have the same read-id as previous=not a multiple read, print the data of the previous read
#if it has same read-id, continue gathering data for that read

def print_output_line(readId,startPos,avgQ):
    startPosStr=""
    for i in range(len(startPos)-1):#until second to last startPosition, so as to not add "," after last

        startPosStr+=startPos[i]+", "

    startPosStr+=startPos[len(startPos)-1]#last startPosition
    numMappings=len(startPos)
    avgQfl=np.mean(avgQ)
    print(readId,'\t',numMappings,'\t',startPosStr,'\t',avgQfl)

#read till the end of the file
readId=""
    
startPos=[]
avgQ=[]
refName=""
firstRead=True
while True:
    try:
        
        red=str(input())
        if(red[0])=="@":#skip header lines
            continue
        elif(firstRead):#if first read in file
            firstRead=False
            lista=red.split('\t')
            refName=lista[2]
            if(refName=="*"):#if reference name is invalid
                continue
            readId=lista[0]#readId of new line

            startPos.append(lista[3])#append start positions
            avgQ.append(int(lista[4]))#append avgQual
            

        else:
            lista=red.split('\t')
            refName=lista[2]
            if(refName=="*"):#if reference name is invalid
                continue
            newReadId=lista[0]#readId of new line

            if(newReadId != readId):#if the read is not multiple,or the next read is not the same, print it out, and empty the lists for new read data
                print_output_line(readId,startPos,avgQ)
                startPos=[]
                avgQ=[]
                readId=newReadId
            elif(newReadId == readId):#multiple reads, dont print, continue adding information
                readId=newReadId
            #append after printing to not interfere with previous read data
            startPos.append(lista[3])#append start positions
            avgQ.append(int(lista[4]))#append avgQual
                
    except EOFError:
        print_output_line(readId,startPos,avgQ)#last line, print what we have
        break
