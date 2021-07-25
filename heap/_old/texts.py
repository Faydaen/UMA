import sys



file = open('modules.txt', 'w') #write to file
for line in sys.modules:
     file.write(line)
file.close()