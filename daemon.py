import socket
from time import sleep, strftime, time
from argparse import ArgumentParser
from pathlib import Path
import csv


def args_manage():
    parser = ArgumentParser()
    parser.add_argument(
        "--directory",
        default=Path('.'),
        type=Path,
        help="Directory dove salvare i file di log"
        )
    parser.add_argument(
        "--host",
        default="8.8.8.8",
        type=str,
        help="IP address dell'host che si contatta"
        )
    parser.add_argument(
        "--port",
        default=53,
        type=int,
        help="Porta dell'host alla quale ci si connette"
        )
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
    parser.add_argument(
        "--csv",
        action="store_true",
        help="Scrive i risultati in un file csv"
        )
    return parser.parse_args()


def check(host, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True

    except socket.error as err:
        return False


def write(directory_path, start_day, start_time, stop_time, delta_time, verbose_mode, csv_mode):
    file_path = directory_path / f"{start_day}"
    report_text = f"{start_time} - {stop_time} | {delta_time} sec\n"


    if verbose_mode:
        print(report_text)

    if csv_mode:
        f = open(directory_path / f"{start_day}.csv", "a+")
        writer = csv.writer(f, delimiter=",")
        writer.writerow([start_time, stop_time, delta_time])
        f.close()

    else:
        f = open(directory_path / f"{start_day}.txt", "a+")
        f.write(report_text)
        f.close()


args = args_manage()

while True:
    sleep(args.delay)

    status = check(args.host, args.port, args.timeout)
    if status is False:
        start_day = strftime("%m-%d-%Y")
        start_time = strftime("%H:%M:%S")
        start = time()
    
        while status is False:
            sleep(args.delay)
            status = check(args.host, args.port, args.timeout)

        stop_time = strftime("%H:%M:%S")
        stop = time()
        delta_time = round(stop - start, 1)

        write(args.directory, start_day, start_time, stop_time, delta_time, args.verbose, args.csv)
