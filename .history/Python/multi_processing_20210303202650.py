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
    # print(f'Task {name} runs {end - start}')

if __name__ == '__main__':
    print(f'Parent process {os.getpid()}')
    p = Pool(100)
    for i in range(1000):
        # task(i)
        p.apply_async(task, args = (i,))
    print('Wating for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# from multiprocessing import Process
# import os
# import time


# def long_time_task(i):
#     print('子进程: {} - 任务{}'.format(os.getpid(), i))
#     time.sleep(2)
#     print("结果: {}".format(8 ** 20))


# if __name__=='__main__':
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     p1 = Process(target=long_time_task, args=(1,))
#     p2 = Process(target=long_time_task, args=(2,))
#     print('等待所有子进程完成。')
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))
