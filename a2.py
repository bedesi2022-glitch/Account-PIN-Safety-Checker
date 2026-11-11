class Computer:
  def __init__(self):
    self.__PIN = 7773
  def PIN(self):
    print("PIN: {}".format(self.__PIN))
  def setPIN(self,MaxPIN):
    self.__PIN = MaxPIN
c = Computer()
c.PIN()
c.__PIN = 10000
c.PIN()
c.setPIN(10000)
c.PIN()