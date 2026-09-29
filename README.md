# AItronix Inventory Management System

A small object-oriented inventory system for a Samsung-style electronics
retailer: one central warehouse ships products out to two kinds of shops,
which sell to customers. Built as a scholarship project to practice
encapsulation, inheritance, composition, and custom exceptions in Python.

## Structure

```
product.py           Product hierarchy (Electronic base, Phone/Tv/Watch/Fridge)
stock.py              StockEntry (one product's quantity at one location) and
                       StockHolder (base class for anything that holds stock)
retail_supplier.py    Shop, TraditionalShop, ShowroomShop
inventory.py          Warehouse
exceptions.py         Custom exception hierarchy
main.py               End-to-end demo / smoke test
```

## Design

- **`StockEntry`** owns one product's quantity and is the only thing allowed
  to change it, through `add()` and `remove()`. Both validate the quantity
  before mutating anything, so the count can never go negative or be set to
  an arbitrary value from outside the class.
- **`StockHolder`** is a shared base class for anything that holds stock
  (a warehouse or a shop). It stores entries keyed by product ID and
  implements `__len__`, `__contains__`, and `__getitem__` once, instead of
  duplicating that logic in `Warehouse` and `Shop`.
- **`Warehouse`** and **`Shop`** inherit from `StockHolder` rather than
  wrapping it, so `warehouse["S24-ULT"]` returns the `StockEntry` directly.
- **`ShowroomShop`** overrides shipment handling to accept exactly one unit
  of a product and refuses a second unit while the first is still on
  display.
- **Composition over inheritance where it fits**: `ScreenQuality` is a
  separate class held by `Phone` and `Tv`, rather than duplicated or forced
  into the inheritance chain.
- **Custom exceptions** (`NegativeNumberError`, `OverDraft`,
  `ProductNotFound`, `ProductAlreadyExists`, `CurrentlyOnDisplay`) group
  under `InventoryError` / `ShopError` so calling code can catch broadly or
  narrowly.


## Running it

```bash
python3 main.py
```

`main.py` creates a warehouse and two shops, stocks products, ships and
sells units, and exercises each custom exception (overdraft on the
warehouse, overdraft on a shop, and shipping twice to a showroom).
