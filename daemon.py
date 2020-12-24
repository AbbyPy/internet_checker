import checker
from time import sleep, strftime

delay = 10

while True:
    sleep(delay)

    status = checker.check()
    if status: print("ONLINE")
    if status is False:
        start_day = strftime("%d/%m/%Y")
        start_time = strftime("%H:%M:%S")
        while status is False:
            pass
        stop_time = strftime("%H:%M:%S")

        f = open(start_day, "a")
        error_text = f"{start_time} -- {stop_time} : OFFLINE\n"
        f.write(error_text)
        f.close()

