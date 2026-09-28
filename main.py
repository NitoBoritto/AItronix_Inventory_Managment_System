from product import Phone, Tv
from inventory import Warehouse
from retail_supplier import TraditionalShop, ShowroomShop
from exceptions import OverDraft, CurrentlyOnDisplay

def main():
    print("--- 1. Initializing Products ---")
    s24 = Phone(id="S24-ULT", name="Galaxy S24 Ultra", battery=5000, ram=12, storage=512, is_oled=True)
    neo_tv = Tv(id="TV-NEO", name="Samsung Neo QLED", wattage=150, smart=True, is_oled=False)
    print(f"Created: {s24.name} and {neo_tv.name}")

    print("\n--- 2. Setting Up Warehouses & Shops ---")
    cairo_warehouse = Warehouse(id = "CET-01", city="Cairo")
    giza_retail = TraditionalShop(id="RET-01", city="Giza")
    alex_showroom = ShowroomShop(id="SHO-01", city="Alexandria")

    # Add initial stock to warehouse
    cairo_warehouse.add_product(s24, qty=50)
    cairo_warehouse.add_product(neo_tv, qty=10)
    print(f"Warehouse Stocked. S24 count: {cairo_warehouse['S24-ULT'].available}")

    print("\n--- 3. Testing Operations ---")
    # Ship 20 phones to the traditional retail store
    cairo_warehouse.ship_to_shops(shop=giza_retail, qty=20, product=s24)
    print(f"Warehouse S24 count after shipping: {cairo_warehouse['S24-ULT'].available}")
    print(f"Giza Retail S24 count: {giza_retail['S24-ULT'].available}")

    # Retail store sells 5 phones
    giza_retail.sell(product_id="S24-ULT", qty=5)
    print(f"Giza Retail S24 count after sale: {giza_retail['S24-ULT'].available}")

    print("\n--- 4. Exception Validation ---")
    
    # Test 1: Try to ship more TVs than the warehouse owns
    print("Attempting to overdraft warehouse TVs...")
    try:
        cairo_warehouse.ship_to_shops(shop=giza_retail, qty=50, product=neo_tv)
    except OverDraft as e:
        print(f"SUCCESS - Caught Expected Error: {e}")

    # Test 2: Try to sell more phones than the retail shop owns
    print("Attempting to overdraft retail phones...")
    try:
        giza_retail.sell(product_id="S24-ULT", qty=100)
    except OverDraft as e:
        print(f"SUCCESS - Caught Expected Error: {e}")

    # Test 3: Try to send multiple items to the Showroom
    print("Attempting to send multiple items to Showroom...")
    try:
        # First shipment (1 item) should succeed if you implemented the showroom logic to accept 1
        cairo_warehouse.ship_to_shops(shop=alex_showroom, qty=1, product=s24)
        print("First showroom shipment successful.")
        
        # Second shipment should fail and trigger CurrentlyOnDisplay
        cairo_warehouse.ship_to_shops(shop=alex_showroom, qty=1, product=s24)
    except CurrentlyOnDisplay as e:
        print(f"SUCCESS - Caught Expected Error: {e}")

if __name__ == "__main__":
    main()