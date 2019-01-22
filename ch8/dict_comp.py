#filename: dict_comp.py
#function : dict comprehension for junior high school score


#create a dictionary for junior high school English score
English={"chen_fu":70, "wu_mary":95, "yu_wushawn":85, "Lin_jason":83}
      

Good_English={k:v for k,v in English.items() if v >80}
print("Good English student is", Good_English)


