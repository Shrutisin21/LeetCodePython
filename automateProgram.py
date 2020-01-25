f = open('inputFile.txt', 'r')
passLine = open('PassLine.txt','w')
failFile = open('FailFile.txt' ,'w')
#print(f.read())
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passLine.write(line)
    else:
        failFile.write(line)

f.close()
passLine.close()
failFile.close()