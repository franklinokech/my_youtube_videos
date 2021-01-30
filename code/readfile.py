objRead = open('airports.txt', 'r')

txtContent = objRead.read()

print('The content of the file '+ txtContent)

objRead.close()