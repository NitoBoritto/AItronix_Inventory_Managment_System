"""Inventory Warehouse"""
from exceptions import NegativeNumberError, ProductAlreadyExists, ProductNotFound, ShipNothing, NoShipment, OverDraft
from retail_supplier import Shop
from product import Electronic

class Warehouse:
    def __init__(self, id: str, city: str):
        self._warehouse_id = id
        self._city = city
        self._stock = {}
    
    @property
    def warehouse_id(self):
        """ID Getter"""
        return self._warehouse_id
    
    @property
    def city(self):
        """City Getter"""
        return self._city
        
    def add_product(self, product: Electronic, quantity: int = 0):
        if quantity < 0:
            raise NegativeNumberError("Stock for a Product Can't Be Negative")
            
        elif product.id in self._stock:
            raise ProductAlreadyExists(f"Product ID {product.id} Already Exists in Warehouse")
            
        self._stock[product.id] = {"Item": product,
                                    "Available": quantity}

            
    def check_stock(self, product_id: str):
        if product_id not in self._stock:
            raise ProductNotFound(f"Product {product_id} Doesn't Exist in Inventory")
            
        print(f'Current Available Stock For "{product_id}": {self._stock[product_id].get("Available")}')


    def add_stock(self, product_id : str, quantity: int = 1):
        if product_id not in self._stock:
            raise ProductNotFound(f"Product {product_id} Doesn't Exist in Warehouse")
        
        elif quantity < 0:
            raise NegativeNumberError("Added Quantity Can't Be Negative")
        
        self._stock[product_id]["Available"] += quantity
        print(f"Value Added to {product_id} Successfully")
        
    
    def ship_to_shops(self, shop: Shop, quantity: int, product: Electronic):
        if product.id not in self._stock:
            raise ProductNotFound(f"Product {product.id} Doesn't Exist in Warehouse")
        
        elif quantity <= 0:
            raise NoShipment("Unable to Ship 0 or Negative Values")
        
        elif quantity > self._stock[product.id]["Available"]:
            raise OverDraft("Quantity in Inventory Not Enough for Shippment")
        
        self._stock[product.id]["Available"] -= quantity
        shop._recieve_shipment(product, quantity)


    # Dunder/Magic Methods
    def __len__(self) -> int:
        return len(self._stock)
    
    def __contains__(self, product_id) -> bool:
        return product_id in self._stock
    
    def __getitem__(self, product_id) -> dict:
        if product_id not in self._stock:
            raise ProductNotFound(f"Product {product_id} Doesn't Exist in Warehouse")
        
        return self._stock[product_id]