#filename:Phone.py
#function: yellow phone book using the dict in chapt 8

import sys
yellowbook = {'Edward Huang':29862211, \
'Emily Chou':3325566, 'Chany Yu':3356666, 'Darren Chen':2128865}

yellowitems =yellowbook.items()

# Loop and display tuple items.
phoneitem='Edward Huang'
for yellowitem in yellowitems:
   if phoneitem==yellowitem[0]:
     print("name:", yellowitem[0])
     print("His Phone No:", yellowitem[1])
     sys.exit(0)

print("his no not included")     

    

