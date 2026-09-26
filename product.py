"""Samsung Products"""

class Electronic:
    def __init__(self, id: str, name: str):
        self._id = id
        self.name = name
        
    @property
    def id(self) -> str:
        """ID Getter"""
        return self._id
        
        

class ScreenQuality:
    def __init__(self, is_oled: bool = False):
        self._oled = is_oled

    @property
    def is_oled(self) -> bool:
        """OLED Getter"""
        return self._is_oled

class HomeAppliance(Electronic):
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
            raise ValueError("Wattage Can't be Negative!")
        else:
            self._wattage = val


class Portable(Electronic):
    def __init__(self, id: str, name: str, battery: int):
        super().__init__(id, name)
        self.battery = battery
        
    @property
    def battery(self) -> int:
        return self._battery
        
    @battery.setter
    def battery(self, val: int):
        if val < 0:
            raise ValueError("Battery Can't be Negative!")
        else:
            self._battery = val



        
class Phone(Portable):
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
    def __init__(self, id : str, name : str, wattage : int, smart : bool = True, is_oled : bool = False):
        super().__init__(id, name, wattage, smart)
        self.screen = ScreenQuality(is_oled)



class Watch(Portable):
    def __init__(self, id : str, name : str, battery : int, fitnessSensor : bool = True):
        super().__init__(id, name, battery)
        self.fitnessSensor = fitnessSensor



class Fridge(HomeAppliance):
    def __init__(self, id : str, name : str, wattage : int, smart : bool = True, iceDispenser : bool = False):
        super().__init__(id, name, wattage, smart)
        self.iceDispenser = iceDispenser