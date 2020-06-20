from abc import ABCMeta,abstractmethod


class PypotClient(metaclass=ABCMeta):
    
    MOTOR = "motor"
    REGISTER = "register"
    
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def get_motors(self):
        pass
    