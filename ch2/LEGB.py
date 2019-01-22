#filename: LEGB.py
#function: search the var using LEGB , built-in function is also the same way
#here we define our len function, which will be used as a higher priority than the built-in function len(..)
 
def len(para1):
    print('called my len() function')
    length = 0
    for i in para1:
        length += 1
    return length
 
def LEGB_func(para1):
    len_para1 = len(para1)
    print('Length of Input variable is\t', len_para1)
 
LEGB_func('Hello Python language!')
