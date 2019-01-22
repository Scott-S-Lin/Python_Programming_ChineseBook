#filename:local-global.py 
#function : use the rule of Local -> Enclosed -> Global -> Built-in,

Taipei_high_school = 98
 
def in_TPE_func():
    Taipei_high_school = 108
    print(Taipei_high_school, 'in local in_func()')

print('global data=',Taipei_high_school)

in_TPE_func()
