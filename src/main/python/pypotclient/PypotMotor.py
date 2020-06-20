
class PypotMotor:
  
  def __init__(self, client, name):
    self.name = name
    self.client = client
    self.registers = []
  