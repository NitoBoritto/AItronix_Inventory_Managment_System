"""Custom exceptions used by the Samsung inventory manager."""

# Base exception for errors related to Samsung inventory operations.
class InventoryError(Exception):
    """Base exception for all inventory errors."""
    pass

# Base exception for errors related to Samsung shop operations.
class ShopError(Exception):
    """Base exception for all shop errors."""
    pass


# Raised when a quantity or product value is below zero.
class NegativeNumberError(InventoryError):
    """Raised when a numeric value is negative."""
    
# Raised when code requests a product that is not stored.
class ProductNotFound(InventoryError):
    """Raised when a product ID does not exist."""
    
# Raised when adding a duplicate product to a warehouse.
class ProductAlreadyExists(InventoryError):
    """Raised when a product already exists."""
    
# Raised when a showroom already displays the requested product.
class CurrentlyOnDisplay(ShopError):
    """Raised when a product is already in a showroom."""
    
# Raised when a requested quantity is greater than available stock.
class OverDraft(InventoryError):
    """Raised when a requested quantity exceeds available stock."""