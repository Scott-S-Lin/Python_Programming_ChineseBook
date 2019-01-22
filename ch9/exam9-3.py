#filename: chap9_ex4_index_raise.py
#function: raise exception

Math_Listing=[86,90,78,92,100]
Math_student_name=["Wang Hai","Tsai Cher","Cheng gin-lin","Chang chou sang","Tsai ching-yuan"]

def chk_score(data,indexing):
    if indexing >len(data):
       print("\n****Raise Occurs and will raise IndexError")
       raise IndexError
    else:
        return data[indexing]
    
try:
    print("The Math score is:",Math_Listing)
    index=int(input("Input the index you want:"))
    score=chk_score(Math_Listing,index)
    who=Math_student_name[index]
    
except IndexError as e:
    print("\nexception IndexError after calling subprogram chk_score\n",type(e))
    raise
else:
    print("score=",score, "\tStudent:",who)
finally:
    print("finally statement")
