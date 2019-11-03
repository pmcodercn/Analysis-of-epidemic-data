from multiprocessing import Process
import time
import os


class myProcess(Process):

    def __init__(self, name, age):
        Process.__init__(self)
        self.name = name
        self.age = age

    def run(self):
        pass
        for i in range(10):
            print("-----test:%d-----"%i)
            print("name:%s;age:%d"%(self.name, self.age))
            print("pid:%d;ppid:%d"% ( os.getpid(), os.getppid()))
            time.sleep(1)



if __name__ == "__main__":
    print("-----main:start-----")
    p = myProcess("田海龙", 32)
    p.start()
    p.join(6)

    for i in range(10):
            print("-----main:%d-----"%i)
            time.sleep(1)