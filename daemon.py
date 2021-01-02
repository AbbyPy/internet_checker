import socket
from time import sleep, strftime, time


def check(host="8.8.8.8", port=53, timeout=10):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as err:
        return False


def write(start_day, start_time, stop_time, delta_time):
    file_path = f"{start_day}.log"
    f = open(file_path, "a+")
    report_text = f"{start_time} - {stop_time} | {delta_time} sec\n"
    f.write(report_text)
    f.close()

delay = 5

while True:
    sleep(delay)

    status = check()
    if status: print("ONLINE")
    if status is False:
        start_day = strftime("%m-%d-%Y")
        start_time = strftime("%H:%M:%S")
        start = time()
        print("OFFLINE START")
    
        while status is False:
            sleep(delay)
            status = check()
            print("STILL OFFLINE")

        stop_time = strftime("%H:%M:%S")
        stop = time()
        print("OFFLINE STOP")
        
        delta_time = round(stop - start, 1)

        write(start_day, start_time, stop_time, delta_time)