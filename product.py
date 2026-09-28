"""Samsung Products"""
from exceptions import NegativeNumberError

# Base Classes
class Electronic:
    """Base Class"""
    def __init__(self, id: str, name: str):
        self._id = id
        self.name = name
        
    @property
    def id(self) -> str:
        """ID Getter"""
        return self._id


class ScreenQuality:
    """Composition Class"""
    def __init__(self, is_oled: bool = False):
        self._oled = is_oled

    @property
    def is_oled(self) -> bool:
        """OLED Getter"""
        return self._is_oled


class HomeAppliance(Electronic):
    """2nd Level Class"""
    def __init__(self, id: str, name: str, wattage: int, smart: bool = True):
        super().__init__(id, name)
        self.wattage = wattage
        self.smart = smart

    @property
    def wattage(self) -> int:
        return self._wattage

    @wattage.setter
    def wattage(self, val: int):
        if val < 0:
            raise NegativeNumberError("Wattage Can't be Negative")
        else:
            self._wattage = val


class Portable(Electronic):
    """2nd Level Class"""
    def __init__(self, id: str, name: str, battery: int):
        super().__init__(id, name)
        self.battery = battery
        
    @property
    def battery(self) -> int:
        return self._battery
        
    @battery.setter
    def battery(self, val: int):
        if val < 0:
            raise NegativeNumberError("Battery Can't be Negative")
        else:
            self._battery = val




# Products
class Phone(Portable):
    """Inherits from Portable and ScreenQuality as Compo"""
    def __init__(self, id : str, name : str, battery : int, ram : int, storage : int, is_oled : bool = False):
        super().__init__(id, name, battery)
        self._ram = ram
        self._storage = storage
        self.screen = ScreenQuality(is_oled)

    @property
    def ram(self) -> int:
        return self._ram
    
    @property
    def storage(self) -> int:
        return self._storage


class Tv(HomeAppliance):
    """Inherits from HomeAppliance as main and ScreenQuality as Compo"""
    def __init__(self, id : str, name : str, wattage : int, smart : bool = True, is_oled : bool = False):
        super().__init__(id, name, wattage, smart)
        self.screen = ScreenQuality(is_oled)



class Watch(Portable):
    """Inherits from Portable as main"""
    def __init__(self, id : str, name : str, battery : int, fitnessSensor : bool = True):
        super().__init__(id, name, battery)
        self.fitnessSensor = fitnessSensor



class Fridge(HomeAppliance):
    """Inherits from HomeAppliance as main"""
    def __init__(self, id : str, name : str, wattage : int, smart : bool = True, iceDispenser : bool = False):
        super().__init__(id, name, wattage, smart)
        self.iceDispenser = iceDispenser