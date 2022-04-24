from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self): ...

class Laptop(Computer):
    def process(self):
        print("Laptop")

laptop = Laptop()
laptop.process()