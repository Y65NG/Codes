import os

# print(f'Process ({os.getpid()}) start...')
# pid = os.fork()
# # print(pid)
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    
from multiprocessing import Process

def run_proc(name):
    print(f'Run child process {name} ({os.getpid()})...')

if __name__ == '__main__':
    print(f'Parent process {os.getpid()}')
    p = Process(target = run_proc, args = ('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
