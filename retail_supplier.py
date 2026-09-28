"""Samsung retail shop types and their shipment rules."""

from exceptions import CurrentlyOnDisplay
from stock import StockHolder, StockEntry
from product import Electronic

# Base Shop
class Shop(StockHolder):
    """Base Samsung shop that receives and stores electronic products."""

    def __init__(self, id: str, city: str):
        super().__init__()
        self._shop_id = id
        self.city = city
        
    @property
    def shop_id(self) -> str:
        return self._shop_id

    def _recieve_shipment(self, product: Electronic, qty: int):
        # Add to an existing entry or create the first entry for this product.
        if product.id not in self:
            self._stock[product.id] = StockEntry(product, qty)
            
        else:
            self[product.id].add(qty)

# Shop Types
class ShowroomShop(Shop):
    """Samsung showroom that displays at most one unit of each product."""

    def __init__(self, id: str, city: str):
        super().__init__(id, city)

    def _recieve_shipment(self, product: Electronic, qty: int = 1):
        # A product already on display cannot be shipped to this showroom again.
        if product.id in self and self[product.id].available >= 1:
            raise CurrentlyOnDisplay("ShowRoom Currently Has This Product On Display")
        
        # Showrooms keep exactly one display unit, regardless of shipment quantity.
        self._stock[product.id] = StockEntry(product.id, available = 1)

class TraditionalShop(Shop):
    """Samsung retail shop that stores products and sells units to customers."""

    def __init__(self, id: str, city: str):
        super().__init__(id, city)
    
    def sell(self, product_id: str, qty: int = 1):
        # StockEntry validates both negative quantities and insufficient stock.
        self[product_id].remove(qty)
        print(f"Product {product_id} Has been Sold")