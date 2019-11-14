from time import sleep
from random import randint
from ball import Ball

from thread_ws import Thread_WS

ball = Ball()

class Player(Thread_WS):
    def __init__(self, name):
        Thread_WS.__init__(self, name)

    def try_get_ball(self):
        global ball 
        ball.adquire(self)


    def release_ball(self):
        global ball 
        ball.release(self)

    def run(self):
        while(True):
            try:
                print("Jogador {0} esta tentando pegar a bola".format(self.name))
                self.try_get_ball()
                print("Jogador {0} pegou a bola".format(self.name))
                # Critical region
                time_sleep = randint(1,2)
                sleep(time_sleep)
                print("Jogador {0} ficou {1} segundo(s) com o bola".format(self.name, time_sleep))
                self.release_ball()
            except Exception as e:
                print(e)
    