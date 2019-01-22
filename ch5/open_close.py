#filename:Open-close.py
#function: simply show how to open and clos  file

file_obj = open("employee.txt", "w")
print( "Name of the file: ", file_obj.name)
file_obj.write( "Python is not hard to learn as long as you have a right concept.\n")
file_obj.close()
