#filename:encoding.py
#function: the codec encode and decode
# CP950 is Traditional Chinese (繁体中文)

import codecs
import sys

print ("\n System version",sys.version) # version of the system
print ("\n system stdout encoding",sys.stdout.encoding) # encoding of stdout
print ("\n system stdin encoding",sys.stdin.encoding) # encoding of stdin

str=sys.getdefaultencoding()
print("default encoding is ",str)

string1="你好"
bytes=codecs.encode(string1,'big5')
print("the encode data=",codecs.encode(string1,'big5'))
print(codecs.decode(bytes,'big5'))


msg = '番茄菠菜5大防癌食物'
encoded_data = msg.encode('utf-8','strict')
print (encoded_data)

print( codecs.decode(encoded_data,'utf-8'))  

