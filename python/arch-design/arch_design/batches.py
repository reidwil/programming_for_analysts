from dataclasses import dataclass
from lib2to3.pgen2.token import OP
from typing import Optional
from datetime import date

@dataclass(frozen=True)
class Orderline:
    order_id: str
    sku: str
    qty: int

class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: Orderline):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: Orderline):
         if line in self._allocations:
             self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)
    
    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity
    
    def can_allocate(self, line: Orderline) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
