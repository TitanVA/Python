import time
from multiprocessing import Process
import os

CNT = 0


def f():
    global CNT
    print(f"Started from", os.getpid())
    time.sleep(3)
    CNT += 2
    print(f"f: {CNT} from", os.getpid())


if __name__ == '__main__':
    p = Process(target=f, args=())
    p_1 = Process(target=f, args=())
    p_2 = Process(target=f, args=())
    p.start()
    p_1.start()
    p_2.start()
    print("Finished")