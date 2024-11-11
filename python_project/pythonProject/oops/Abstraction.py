#Absrtraction: Abstraction is the concept of hiding the complex implementation details and showing only necessary features
#Abstract class can have both abstract and non - abstract methods.

from abc import ABC,  abstractmethod


class Vehcile(ABC):
    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_chasis(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def install_tires(self):
        pass

class Car(Vehcile):

    def build_engine(self):
        print("building car engine")

    def build_chasis(self):
        print("building car chasis")

    def build_body(self):
        print("building car body")

    def install_tires(self):
        print("installing car tires")
