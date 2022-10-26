class Bird:

    maxHeight = None
    position = None
    body = ['o','>']

    def __init__(self, N):
        self.position=N/2
        self.maxHeight=N

    def jump(self):
        if self.position>0:
            self.position = self.position + 1

    def gravity(self):
         if self.position<self.maxHeight:
             self.position = self.position - 1
