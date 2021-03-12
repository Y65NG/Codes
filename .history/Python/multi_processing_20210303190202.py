import os

print(f'Process ({os.getppid()}) start...')
pid = os.fork()
print(pid)
if pid == 0:
    