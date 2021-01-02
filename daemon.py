import socket
from time import sleep, strftime, time
import argparse


def args_manage():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--timeout",
        default=5,
        type=int,
        help="Timeout in secondi del tentativo di connessione"
        )
    parser.add_argument(
        "--delay",
        default=5,
        type=int,
        help="Tempo in secondi che intercorre fra un controllo della connessione e l'altro"
        )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Mostra i risulatati dei controlli in tempo reale"
        )
    return parser.parse_args()


def check(host="8.8.8.8", port=53, timeout=10):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as err:
        return False


def write(start_day, start_time, stop_time, delta_time, verbose_mode):
    file_path = f"{start_day}.log"
    f = open(file_path, "a+")
    report_text = f"{start_time} - {stop_time} | {delta_time} sec\n"
    f.write(report_text)
    f.close()
    if verbose_mode: print(report_text)


args = args_manage()

while True:
    sleep(args.delay)

    status = check(timeout=args.timeout)
    if status is False:
        start_day = strftime("%m-%d-%Y")
        start_time = strftime("%H:%M:%S")
        start = time()
    
        while status is False:
            sleep(args.delay)
            status = check(timeout=args.timeout)

        stop_time = strftime("%H:%M:%S")
        stop = time()
        delta_time = round(stop - start, 1)

        write(start_day, start_time, stop_time, delta_time, args.verbose)