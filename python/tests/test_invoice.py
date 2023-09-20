from statement import Invoice, InvoiceLine
from play import Play

hamlet = Play("ham", "Hamlet: Prince of Denmark", "tragedy")

def test_empty_invoice():
    inv = Invoice("customer")
    assert inv.customer() == "customer"
    assert len(list(inv.line_items())) == 0
    assert inv.total_cost() == 0
    assert inv.total_credits() == 0
    
def test_single_performance_has_one_line_item():
    inv = Invoice("customer")
    inv.add_performance(hamlet, 0)
    assert len(list(inv.line_items())) == 1

def test_single_performance_has_correct_totals():
    inv = Invoice("customer")
    inv.add_performance(hamlet, 0)
    assert inv.total_cost() == sum(item.cost for item in inv.line_items())
    assert inv.total_credits() == sum(item.credits for item in inv.line_items())