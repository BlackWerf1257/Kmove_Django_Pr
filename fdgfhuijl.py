inFile, outFile = None, None
outStr=''
lineNum=1

inFile=open('normal.txt','r',encoding='UTF-8')
outFile=open('normal_line.txt','w')

while True:
    inStr=inFile.readline()
    if inStr=='':
        break

inList=inFile.readlines()
for inStr in inList :
    outFile.writelines(inStr)


lineNum+=1


inFile.close()
outFile.close()
