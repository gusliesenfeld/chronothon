import time
import io_handler

class Chronometer:
    def __init__(self,wait_time):
        self.wait_time = wait_time
        self.io_handler_obj = io_handler.IOHandler()
        
        return
    
    
    def run_chrono(self):
        while self.wait_time>=0:
            self.render(self.wait_time)
            time.sleep(1)
            
            self.wait_time-=1
        
        return
    
    
    def render(self,time_ref):
        parsed_time = self.parse_time(time_ref)
        parsed_time.reverse()
        time_scale_strings = ["h","m","s"]
        
        self.io_handler_obj.printclear_line(" ")
        for time_value in range(0,len(parsed_time)):
            self.io_handler_obj.print_line(f"{parsed_time[time_value]}{time_scale_strings[time_value]}"," ")
        
        return parsed_time
    
    
    def parse_time(self,time_seconds):
        time = [time_seconds,0,0]
        
        for time_ref in range(0,len(time)):
            new_parse_calc = self.time_parse_calc(time[time_ref])
            
            time[time_ref] = new_parse_calc[1]
            if time_ref+1<len(time):
                time[time_ref+1] = new_parse_calc[0]
        
        return time
    
    
    def time_parse_calc(self,time_ref):
        time_to_parse = [0,time_ref]
        
        while time_to_parse[1]>=60:
            time_to_parse[0] += 1
            time_to_parse[1] -= 60
        
        return time_to_parse

