import checker
from time import sleep

delay = 10

while True:
    sleep(delay)

    status = checker.check()
    
