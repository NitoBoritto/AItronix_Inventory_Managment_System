"""Samsung warehouse inventory and product shipment operations."""

from exceptions import ProductAlreadyExists
from retail_supplier import Shop
from product import Electronic
from stock import StockHolder, StockEntry

class Warehouse(StockHolder):
    """Stores Samsung products centrally and ships them to retail shops."""

    def __init__(self, id: str, city: str):
        super().__init__()
        self._warehouse_id = id
        self._city = city
    
    @property
    def warehouse_id(self):
        """ID Getter"""
        return self._warehouse_id
    
    @property
    def city(self):
        """City Getter"""
        return self._city
        
    def add_product(self, product: Electronic, qty: int = 0):
        # A warehouse may register a product only once.
        if product.id in self:
            raise ProductAlreadyExists(f"Product ID {product.id} Already Exists in Warehouse")
            
        self._stock[product.id] = StockEntry(product, qty)

            
    def check_stock(self, product_id: str):
        # Indexing through StockHolder also validates that the product exists.
        available_stock = self[product_id].available
        print(f'Current Available Stock For "{product_id}": {available_stock}')


    def add_stock(self, product_id : str, qty: int = 1):
        # Delegate quantity validation to the StockEntry object.
        self[product_id].add(qty)
        print(f"Value Added to {product_id} Successfully")
        
    
    def ship_to_shops(self, shop: Shop, qty: int, product: Electronic):
        # Remove stock first; failed removals prevent an incomplete shipment.
        self[product.id].remove(qty)
        # Each shop decides how it accepts and stores the shipment.
        shop._recieve_shipment(product, qty)
