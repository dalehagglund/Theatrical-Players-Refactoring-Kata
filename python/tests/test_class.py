import pytest
from statement import Play

def test_play_construction():
    p = Play("ado", "Much Ado About Nothing", "comedy")
    assert p.id == "ado"
    assert p.name == "Much Ado About Nothing"
    assert p.type == "comedy"
    
def test_tragedy_performance_costs():
     p = Play("", "", "tragedy")
     assert p.performance_cost(0) == 40000
     assert p.performance_cost(30) == 40000
     assert p.performance_cost(31) == 41000

def test_comedy_performance_costs():
    p = Play("", "", "comedy")
    assert p.performance_cost(0) == 30000
    assert p.performance_cost(20) == 36000
    assert p.performance_cost(21) == 30000 + (300 * 21) + 10000 + 500