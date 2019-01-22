#filename :ex-3.py
#function : swap the two var , it is useful for data strcture like Sort,....and so on

def swap(a, b):
   temp = a
   a = b
   b = temp
   return a, b

print("please keyin two no")
a = int(input())
b = int(input())
print ("a = %d  b = %d" % (a, b))
a, b = swap(a, b)
print ("after swap,data is as follow:")
print ("a = %d  b = %d" % (a, b))
