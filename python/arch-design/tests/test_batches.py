from datetime import date
from arch_design.batches import Batch, Orderline

def make_batch_and_line(sku, batch_qty, line_qty):
    return(
        Batch('Order-100', sku, batch_qty, date.today()),
        Orderline('Order-123', sku, line_qty)
    )

print(make_batch_and_line(123,100, 2))