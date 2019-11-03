from multiprocessing import Pool
import os
import time
import random


def test(i):
    for s in range(5):
        print("----pid:%d;s:%d;i:%d----"% (os.getpid(),s,i))
        time.sleep(1)
    # print("----i:%d----"% i)


def main():
    p = Pool(3)

    for i in range(10):
        print(i)
        p.apply_async(test, (i, ))

    p.close() # 关闭进程池，相当于不能再添加新任务了。
    p.join()  # 默认主进程不会等待子进程执行完才结束，程序需要设置主进程等待子进程。


if __name__ == "__main__":
    main()