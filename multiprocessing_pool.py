# -*-coding:utf8-*-
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 启动大量的子进程，可以用进程池的方式批量创建子进程
    # 这里设置pool最多同时执行4个进程
    # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到等待效果
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # 函数的参数以元组的方式传入
    print('Waiting for all subprocesses done...')
    p.close()  # close()之后不能添加新的process了
    p.join()  # 等待所有子进程执行完毕;必须先调用close()
    print('All subprocesses done.')