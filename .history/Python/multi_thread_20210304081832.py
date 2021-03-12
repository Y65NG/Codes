import time, threading

def loop():
    print(f'thread {threading.currentThread().name} is running...')
    n = 0
    while n < 5:
        n += 1
        print(f'thread {threading.current_thread().name} >>> {n}')
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print(f'thread {threading.current_thread().name} is running...')
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
