#filename:stdout_err.py
#function: show the stdout and stderr
#stdout, stderr does not add carriage returns for you;

for i in range(2):
  print ('Brand Asus, HTC in Taiwan') 

import sys
for showtimes in range(2):
     sys.stdout.write('Brand Samsung, Apple\n')
     
for showtimes in range(2):
     sys.stderr.write('Brand Samsung, Apple\n')

print("you can see the color is different between stdout and stderr")
