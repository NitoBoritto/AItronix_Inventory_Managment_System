"""Exception Handling"""

class InventoryError(Exception):
    """Base Exception for All Inventory Errors"""
    pass

class NegativeNumberError(InventoryError):
    """Raised When There's Negative Values"""
    
class ProductNotFound(InventoryError):
    """Raised When Product ID Doesn't Exist"""
    
class ProductAlreadyExists(InventoryError):
    """Raised When Product Already Exists"""
    
class ShopNotFound(InventoryError):
    """Raised When Shop Doesn't Exist"""
    
class NoShipment(InventoryError):
    """Raised When Quantity Shipped <= 0"""
    
class CurrentlyOnDisplay(InventoryError):
    """Raised When Product Already in a ShowRoom"""