from semaphore import Semaphore

class Ball(Semaphore):

    def __init__(self):
        Semaphore.__init__(self, 1)
        self.player = None

    def adquire(self, player):
        super().adquire(player)
        self.player = player

    def release(self, player):
        super().release(player)
        self.player = None
        
    
  