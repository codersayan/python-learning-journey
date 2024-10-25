import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

thread = threading.Thread(target=print_numbers)
thread.start()
