#filename: chap8_ex_3.py

English={"chen_fu":70, "wu_mary":95, "yu_wushawn":85, "Lin_jason":83}
 
Good_English={k:v for k,v in English.items() if v >80}
print("Good English student is", Good_English)

len1=len(English)
len2=len(Good_English)
if len2==len1:
    print("same dictionary")
else:
    print("diff dict")
