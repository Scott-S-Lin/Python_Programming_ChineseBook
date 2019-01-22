#filename: Std_stream.py
#function: use the stdout and stderr for printing  data
#output to stdout: using sys.stdout.write("data")
#output to stderr: using sys.stderr.write("data")

import sys
while True:
  print ("\n while iteration ...",end=' ')
# reading from sys.stdin (stop with Ctrl-D):
  try:
    indata = input("Enter a number, press CTRL+D if you want to quit: ")
    
  except EOFError:
    print ("\nEOF ,because you keyin Ctrl+D")
    break
  else:
    indata = int(indata)
    if indata == 0:
       sys.stderr.write("to stderr,data is  %d " % (indata)) 
    else:
#output to stdout: 
      sys.stdout.write("data is  %d " % (indata))
