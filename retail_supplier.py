"""Samsung Stores and Shipping"""
from exceptions import NoShipment, CurrentlyOnDisplay


# Base Shop
class Shop:
    def __init__(self, id: str, city: str):
        self._shop_id = id
        self.city = city
        self._inventory = {}
        
    @property
    def shop_id(self) -> str:
        return self._shop_id

    @property
    def inventory(self) -> dict:
        return self._inventory
    
    def recieve_shipment(self, product, quantity: int):
        if quantity <= 0:
            raise NoShipment("Unable to Ship 0 or Negative Values")
        
        if product.id not in self._inventory:
            self._inventory[product.id] = {"Item": product,
                                           "Available": quantity}
        else:
            self._inventory[product.id]["Available"] += quantity

# Shop Types
class ShowroomShop(Shop):
    def __init__(self, id: str, city: str):
        """Only Has 1 of Each Product For Showcasing"""
        super().__init__(id, city)

    def recieve_shipment(self, product, quantity: int = 1):
        if product.id in self._inventory and self.inventory[product.id]["Available"] >= 1:
            raise CurrentlyOnDisplay("ShowRoom Currently Has This Product On Display")
        
        self._inventory[product.id] = {"Item": product,
                                       "Available": 1}

class TraditionalShop(Shop):
    def __init__(self, id: str, city: str):
        """Has Storeroom For Storing Products For Selling"""
        super().__init__(id, city)
        