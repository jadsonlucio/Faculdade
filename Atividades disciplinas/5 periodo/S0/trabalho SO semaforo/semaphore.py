from random import randint

class Semaphore():
    def __init__(self, max_threads):
        self.count_thread = 0
        self.threads_queue = []
        self.current_thread = None
        self.max_threads = max_threads
        self.log_information = True

    def adquire(self, thread):
            self.count_thread += 1
            if self.count_thread > self.max_threads:
                self.threads_queue.append(thread)
                thread.sleep()
    
    def release(self, thread):
        if self.count_thread > 0:
            self.count_thread += -1
            self.wakeup_thread_in_queue()
        else:
            raise Exception("two or more thread released")

    
    def wakeup_thread_in_queue(self):
        if len(self.threads_queue) > 0:
            index_thread = randint(0, len(self.threads_queue) - 1)
            thread_selected = self.threads_queue.pop(randint(0, len(self.threads_queue) - 1))
            thread_selected.wakeup()

    