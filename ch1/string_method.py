#filenme:string_method.py

text="this is text"
print(len(text))
for ch in text:
    print("char is ",ch)

#text.count('ch') return the count of ch
print(text.count('t'))
#text.find("string") return the index of text
print(text.find("is"))

newtext=" ".join(['Qualcomm','Ceo','Johnny'])
print(newtext)
latesttext=newtext.split(' ')
print(latesttext)


