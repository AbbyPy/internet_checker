import checker
from time import sleep, strftime, time

delay = 5

while True:
    sleep(delay)

    status = checker.check()
    if status: print("ONLINE")
    if status is False:
        start_day = strftime("%m-%d-%Y")
        start_time = strftime("%H:%M:%S")
        start = time()
        print("OFFLINE START")
    
        while status is False:
            sleep(delay)
            status = checker.check()
            print("STILL OFFLINE")

        stop_time = strftime("%H:%M:%S")
        stop = time()
        print("OFFLINE STOP")
        
        delta_time = round(stop - start, 1)

        file_path = f"{start_day}.log"
        f = open(file_path, "a+")
        error_text = f"{start_time} -- {stop_time} : OFFLINE per {delta_time} sec\n"
        f.write(error_text)
        f.close()

