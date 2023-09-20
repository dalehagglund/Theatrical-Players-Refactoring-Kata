import pytest
from play import Play

def test_play_construction():
    p = Play("ado", "Much Ado About Nothing", "comedy")
    assert p._id == "ado"
    assert p._name == "Much Ado About Nothing"
    assert p._type == "comedy"
    
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
    
def test_tragedy_volume_credits():
    p = Play("", "", "tragedy")
    assert p.volume_credits(0) == 0
    assert p.volume_credits(30) == 0
    assert p.volume_credits(31) == 1
    assert p.volume_credits(32) == 2
    
def test_comedy_volume_credits():
    p = Play("", "", "comedy")
    assert p.volume_credits(0) == 0
    assert p.volume_credits(4) == 0
    assert p.volume_credits(5) == 1
    assert p.volume_credits(10) == 2
    assert p.volume_credits(30) == 6
    assert p.volume_credits(31) == 1 + 6
    assert p.volume_credits(35) == 5 + 7