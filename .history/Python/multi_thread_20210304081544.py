import time, threading

def loop():
    print(f'thread {threading.current_thread().name}')
    n = 0
    while n < 5:
        n += 1
        print(f'thread {threading.current_thread().name} >>> {n}')
        time.sleep(1)
    