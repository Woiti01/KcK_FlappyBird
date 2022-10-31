class Bird:

    maxHeight = None
    position = 0
    body = ['o','>']
    body_0 = ['o','>']
    body_1 = ['=','D']
    body_2 = ['(',')','*']
    body_3 = ('8','=','=','D')
    bodies = [body_0,body_1,body_2,body_3]
    diff = 1
    def __init__(self, N):
        self.position=N/2
        self.maxHeight=N

    def jump(self):
        if self.position>0:
            self.position = self.position - 1

    def gravity(self):
         if self.position<self.maxHeight-1:
             self.position = self.position + 1
    def changeSkin(self, id):
        self.body = self.bodies[id%len(self.bodies)]

    def changeDiff(self, id):
        self.diff = id

