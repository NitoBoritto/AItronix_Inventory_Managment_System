"""Exception Handling"""

# Base Errors
class InventoryError(Exception):
    """Base Exception for All Inventory Errors"""
    pass

class ShopError(Exception):
    """Base Exception for All Shop Errors"""
    pass

class ShippingErrors(Exception):
    """Base Exception for All Shipping Errors"""


# Exceptions
class NegativeNumberError(InventoryError):
    """Raised When There's Negative Values"""
    
class ProductNotFound(InventoryError):
    """Raised When Product ID Doesn't Exist"""
    
class ProductAlreadyExists(InventoryError):
    """Raised When Product Already Exists"""
    
class ShopNotFound(ShopError):
    """Raised When Shop Doesn't Exist"""
    
class NoShipment(ShippingErrors):
    """Raised When Quantity Shipped <= 0"""
    
class CurrentlyOnDisplay(InventoryError):
    """Raised When Product Already in a ShowRoom"""
    
class OverDraft(InventoryError):
    """Raised When Quantity Shipped > Quantity in Warehouse"""