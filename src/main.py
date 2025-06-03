import chrono
import io_handler

def __init__():
    input_parser = io_handler.IOHandler()
    
    time = input("Waiting for a time input...\nFormat: SS.MM.HH : ")
    time = input_parser.parse_input(time)
    
    chrono_obj = chrono.Chronometer(time)
    chrono_obj.run_chrono()

    print("Time ran out!")
    
    return


__init__()

