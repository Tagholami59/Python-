class car:
  def __init__(self,color, model):
    self.color = color
    self.model = model

pride = car("gray", 141)
print(pride.color)
print(pride.model)
pride = car("black", 111)
print(pride.color)
print(pride.model)
