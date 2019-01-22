#filename: set_comp_example.py
#function : set comprehension


#create a set first and use the set comprehension 
TN_setlist ={40,39,40,38,39,37,39}
TN_Finalsetlist={item for item in TN_setlist if item >=39 }
print("Tainan final setlist =",TN_Finalsetlist)      

KS_setlist ={38,41,40,39,40,40,39}
KS_Finalsetlist={item for item in KS_setlist if item >=39 }
print("Kaoshung final setlist =",KS_Finalsetlist)


Total_Finalsetlist=TN_Finalsetlist.union(KS_Finalsetlist)
print("Total final setlist =",Total_Finalsetlist)


