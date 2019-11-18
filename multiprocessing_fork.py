# -*-coding:utf8-*-
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()  # 复制当前进程（父进程）；会有两个return：一次为父进程内返回子进程ID，一次为子进程内返回0。
# getpid()获取当前进程ID，getppid()获取父进程ID
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))







