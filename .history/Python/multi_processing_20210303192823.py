import os

# print(f'Process ({os.getpid()}) start...')
# pid = os.fork()
# # print(pid)
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    
# from multiprocessing import Process

# def run_proc(name):
#     print(f'Run child process {name} ({os.getpid()})...')

# if __name__ == '__main__':
#     print(f'Parent process {os.getpid()}')
#     p = Process(target = run_proc, args = ('test',))
#     print('Child process will start.')
#     # p.start()
#     # p.join()
#     # print('Child process end.')

from multiprocessing import Pool
import time, random

def task(name):
    print(f'Run task {name} ({os.getpid()})')
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print(f'Task {name} runs {end - start}')

if __name__ == '__main__':
    print(f'Parent process {os.getpid()}')
    p = Pool()
    for i in range(10):
        p.apply_async(task, args = (i,))
    print('Wating for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')