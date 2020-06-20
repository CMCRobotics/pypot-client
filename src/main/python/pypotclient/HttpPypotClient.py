from pypotclient.PypotClient import PypotClient
from pypotclient.PypotMotor import PypotMotor
from pypotclient.PypotRegister import PypotRegister
import logging

import requests

class HttpPythonClient(PypotClient):
    
    JSON_CONTENT_TYPE = "application/json"
    
    def __init__(self, base_url):
        self.initialized = False
        self.base_url = base_url
        self._motors = {}
        self.session = None
    
    def connect(self):
        self.session = requests.Session()
        response = self.session.get(self.base_url)
        
        if response.headers['content-type'].startswith(JSON_CONTENT_TYPE):
            json = response.json()
            for motor in json["motors"]:
                motor_name = motor["name"]
                self.__dict__[motor.name] = PypotMotor(motor_name)
                self._motors[motor_name] = self[motor_name]
                for register in motor["registers"]:
                    if(register != "name") :
                        self[motor.name][register] = PypotRegister(self.session, motor, register, motor[register])
                       
    
    
    def get_motors(self):
        return self._motors
    
    def get(self, *registers):
        response = []
        for register in registers:
            response.append(register.get())
        return response
    
    def set(self, **register_and_values):
        for reg,val in register_and_values.items():
            self.re
    
PypotClient.register(HttpPythonClient)

