import checker
from time import sleep, strftime

delay = 2

while True:
    sleep(delay)

    status = checker.check()
    if status: print("ONLINE")
    if status is False:
        start_day = strftime("%d-%m-%Y")
        start_time = strftime("%H:%M:%S")
        print("OFFLINE START")
    
        while status is False:
            sleep(delay)
            status = checker.check()
            print("STILL OFFLINE")

        stop_time = strftime("%H:%M:%S")
        print("OFFLINE STOP")
        
        file_path = f"{start_day}.log"
        f = open(file_path, "a+")
        error_text = f"{start_time} -- {stop_time} : OFFLINE\n"
        f.write(error_text)
        f.close()

