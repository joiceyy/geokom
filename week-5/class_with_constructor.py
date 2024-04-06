class car:
  def __init__(self, name, color, speed):
    self.name = name
    self.color = color
    self.speed = speed

lambo = car("Lambo", 'red', 977)
print(lambo.name, lambo.color, lambo.speed)

bmw = car("BMW", 'brown', 210)
print(bmw.name, bmw.color, bmw.speed)


