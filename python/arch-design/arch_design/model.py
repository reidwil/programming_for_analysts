from typing import List
from batches import Batch, Orderline

def allocate(line: Orderline, batches: List[Batch]) -> str:
    batch = next(
        b for b in sorted(batches) if b.can_allocate(line)
    )
    batch.allocate(line)
    return batch.reference