# An abstract class is a class whose instance cannot be created.
# Abstract class must have an abstract method. The child class must define the implementation of abstract method else it will 
# be an abstract class

from abc import ABC, abstractmethod 

class Stream(ABC):
    def __init__(self):
        self.opened = False
    
    @abstractmethod
    def read(self): #abstract method has no implelementation, the child class must define it
        pass

class VideoStream(Stream):
    pass


class NetworkStream(Stream):
    def __init__(self):
        super().__init__()
    
    def read(self):
       return True


network = NetworkStream() # network stream should define an abstract method
print(network.read())

