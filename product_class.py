from dataclasses import dataclass

@dataclass
class Product:
    name: str = 'unknown'
    brand: str = 'unknown'
    price: float = 0.0
    rating: float = 0.0