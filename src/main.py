import chrono

def __init__():
    time = parse_input(input(('awaiting time...')))
    
    chrono_obj = chrono.Chronometer(time)
    chrono_obj.run_chrono()
    
    return

def parse_input(string_ref):
    time_target=[0,0,0]
    
    string_ref = string_ref.split('.')

    for c in range(0,len(time_target)):
        time_target[c]=int(string_ref[c])
    
    time_target[0]+=time_target[1]*60
    time_target[0]+=time_target[2]*3600
    
    return time_target[0] 
    

__init__()

