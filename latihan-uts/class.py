# In[1]:
# Message
# {
#   "phone_number": "",
#   "name": "",
#   "message": "",
#   "is_read": false,
#   "is_send": true,
#   "created_at": "2024-04-01T00:00:00"
# }

class message:
  def __init__(self, phone_number, name):
    self.phone_number = phone_number
    self.name = name
    self.message = ""
    self.is_read = False
    self.is_send = False
    self.created_at = "2024-04-01T00:00:00"
  def __str__(self):
    return f"phone_number: {self.phone_number}\nname: {self.name}\nmessage: {self.message}\nis_read: {self.is_read}\nis_send: {self.is_send}\ncreated_at: {self.created_at}"

# buat function dengan nama send parameternya message. 
# yang dilakukan adalah merubah value send = true, 
# dan mengubah nilai message = message. akan ada print value message.
# panggil function send nya

  def send(self, message):
    self.is_send = True
    self.message = message
    

# buat function read tidak memiliki parameter. 
# yang dilakukan adalah membuat nilai is_read = true dan print message
# panggil function read 
  def read(self):
    self.is_read = True
    print(self.message)

dm = message("90264829", "jola")
dm.send("hi joice, selamat siang")
dm.read()
print(dm)

# %%

# In[2]:



  

  
    
  
