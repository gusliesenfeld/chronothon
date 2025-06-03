class IOHandler:
    last_line_length=0
    
    def __init__(self):
        return
    
    
    def print_line(self,print_value="",end_value=""):
        print(print_value,end=end_value)
        self.last_line_length+=len(print_value)+len(end_value)
        
        return
    
    
    def printclear_line(self,print_value="",end_value=""):
        print(' '*self.last_line_length,end='\r')
        self.last_line_length=0;
        
        self.print_line(print_value,end_value)
        
        return
    
    
    def parse_input(self,string_ref=""):
        time_target=[0,0,0]
        
        string_ref = string_ref.split(".")
        
        for c in range(0,len(string_ref)):
            time_target[c]=int(string_ref[c])
        
        time_target[0]+=time_target[1]*60
        time_target[0]+=time_target[2]*3600
        
        return time_target[0] 

