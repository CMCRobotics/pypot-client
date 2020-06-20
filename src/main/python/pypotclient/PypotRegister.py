
class PypotRegister:
  def __init__(self, client, motor, name, current_value = 0):
    self.name = name
    self.motor = motor
    self.client = client
    self.current_value = current_value
  
    
  def set(self, new_value):
    self.current_value = self.client._set(self.motor, self.name, new_value)
  
  def get(self):
    self.current_value = self.client._get(self.motor, self.name)
    return self.current_value