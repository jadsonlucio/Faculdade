from time import sleep
from threading import Thread

class Thread_WS(Thread):
    def __init__(self, name = "Thread"):
        Thread.__init__(self)
        self.sleeping_state = True
        self.name = name

    @property
    def is_sleeping(self):
        return self.sleeping_state

    def wakeup(self):
        self.sleeping_state = False
        print("Thread {0} wakeup".format(self.name))
    
    def sleep(self):
        self.sleeping_state = True
        print("Thread {0} sleeping".format(self.name))
        while(self.is_sleeping):
            sleep(1)