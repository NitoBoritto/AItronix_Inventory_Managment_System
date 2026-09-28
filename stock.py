"""Stock records for Samsung products in warehouses and shops."""

from exceptions import NegativeNumberError, OverDraft, ProductNotFound
from product import Electronic

class StockEntry:
    """Track one Samsung product and its currently available quantity."""

    def __init__(self, product: Electronic, available: int  = 0):
        # Store the product and start with zero before validating the opening quantity.
        self._product = product
        self._available = 0
        self.add(available)
        
    @property
    def product(self):
        return self._product
        
    @property
    def available(self):
        return self._available
    
    def add(self, qty: int):
        # Stock can only be increased by a non-negative amount.
        if qty < 0:
            raise NegativeNumberError("Added Quantity Can't Be Negative")
        self._available += qty

    def remove(self, qty: int):
        # Validate the quantity before changing the stored stock.
        if qty < 0:
            raise NegativeNumberError("Removed Quantity Can't Be Negative")
        
        elif qty > self._available:
            raise OverDraft("Not Enough Stock")
        
        self._available -= qty
        

class StockHolder:
    """Base class for Samsung warehouses and shops that own stock entries."""

    def __init__(self):
        # The product ID is the key so stock can be retrieved quickly.
        self._stock = {}
    
    def _get_or_create_entry(self, product: Electronic) -> StockEntry:
        # Create an empty entry when a product is first encountered.
        if product.id not in self._stock:
            self._stock[product.id] = StockEntry(product, available = 0)
            
            return self._stock[product.id]
        
    # These magic methods make the holder behave like a small collection.
    def __len__(self) -> int:
        return len(self._stock)
    
    def __contains__(self, product_id) -> bool:
        return product_id in self._stock
    
    def __getitem__(self, product_id) -> StockEntry:
        if product_id not in self._stock:
            raise ProductNotFound(f"Product {product_id} Doesn't Exist in Warehouse")
        
        return self._stock[product_id]
    