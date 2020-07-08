f = open('Exercise Files/inputFile.txt', 'r')
passFile = open('Exercise Files/PassFile.txt', 'w')
failFile = open('Exercise Files/FailFile.txt', 'w')
for line in f:
    data = line.split()
    if data[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

f.close()
passFile.close()
failFile.close()
