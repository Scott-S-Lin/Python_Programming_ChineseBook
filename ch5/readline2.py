
#function: using readline() to read data 

file_in = open("employee1.txt",'r')
while True:
    linedata = file_in.readline()
    if not linedata:
        break
    print(linedata, end='')
file_in.close()

file_in = open("employee1.txt",'r')
print("\n using readlines()\n")
for linedata in file_in.readlines():
    print(linedata, end='')
file_in.close()
