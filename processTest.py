from multiprocessing import Process
import time


def test():
    for i in range(10):
        print("-----test:%d-----"%i)
        time.sleep(1)

if __name__ == "__main__":
    print("-----main:start-----")
    p = Process(target=test)
    p.start()
    p.join(6)

    for i in range(10):
            print("-----main:%d-----"%i)
            time.sleep(1)