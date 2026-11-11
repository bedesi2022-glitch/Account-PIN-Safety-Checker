class PIN:
    def __init__(self,x=7773,y=10000):
        self.x = x
        self.y = y
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)
p1 = PIN(7753,3775)
print(p1)
print("Using this you can change your PINS for security purposes")
print("===Account PIN Safety Checker!===")