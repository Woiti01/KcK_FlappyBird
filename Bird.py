class Bird:

    maxHeight = None
    position = 0

    body = ['o','>']


    body_0 = ['o','>']
    body_1 = ['=','D']
    body_2 = ['(',')','*']

    bodies = [body_0,body_1,body_2]



    def __init__(self, N, id):
        self.position=N/2
        self.maxHeight=N
        self.body = self.bodies[id]

    def jump(self):
        if self.position>0:
            self.position = self.position - 1

    def gravity(self):
         if self.position<self.maxHeight-1:
             self.position = self.position + 1

    def changeSkin(self):
        id = id+1
        id = id%len(self.bodies)
        self.body = self.bodies[id]
