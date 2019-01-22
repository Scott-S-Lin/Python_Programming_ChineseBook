#filename:star_para.py
#function: the subroutine use the *para

def Subroutine(score, *score_all):
    total=0
    print ("\nscore is:", score)
    total += score
    for n in score_all:
         print( "score:", n,end=" ")
         total += n
    
    return total

NTHU=Subroutine(70, 72, 68, 82, 86,68,82)
NCTU=Subroutine(70, 72, 68, 82, 76,68,82)
print("\nresult=",NTHU,NCTU)

#print("total=", total)
