# -*-coding:utf8-*-
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())  # 当前进程ID
    p = Process(target=run_proc, args=('test',))  # 声明一个进程对象：传入函数和函数的参数
    print('Child process will start.')
    p.start()  # 启动
    p.join()  # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')
