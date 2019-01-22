#filename:GW_node.py
#function: the program in the package diretcory


class GW:
    def __init__(self):
        '''sensor node constructor'''
        # Create the deafult sensor node id
        self.GW_id = ['NY_Queen', 'NY_Wallstreet']
  
    def printGW(self):
        print("GW name in the NY area")
        print("-------------")
        for GWid in self.GW_id:
            print("\t%s " %GWid)

test=GW()
test.printGW()
