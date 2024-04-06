# menambahkan fungsi percepatan pada class mobil
class car:
    def __init__(self, color, speed):
      self.color = color
      self.speed = speed
      
    def tambah_speed(self):
      self.speed = self.speed * 2
    
    def ubah_speed(self, speed):
       self.speed = speed
    
    def print_speed(self):
       print(self.speed)
    
    def change_color(self, color):
       self.color = color
    
lambo = car("merah", 100)
lambo.ubah_speed(10000)
print(lambo.color, lambo.speed)


lambo.change_color("pink")
print(lambo.color, lambo.speed)

lambo.tambah_speed()
print(lambo.color, lambo.speed)

lambo.tambah_speed()
print(lambo.color, lambo.speed)

g_class = car('silver', 200)
print(g_class.color, g_class.speed)


print(f'the color of this car is {lambo.color} and speed {lambo.speed}') 
print(f'the color of this car is {g_class.color} with speed {g_class.speed}')