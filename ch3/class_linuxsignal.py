#filename:class_linuxsignal
#function: test the _init_
class Linuxsignal:
    process_counter = 0
    
    def __init__(self):
        print("Class object is inited now")
        type(self).process_counter += 1
        
    def linuxInstances(self):
        return Linuxsignal.process_counter
        

if __name__ == "__main__":
    
    x = Linuxsignal()
    print(x.linuxInstances())
    y = Linuxsignal()
    print(x.linuxInstances())
