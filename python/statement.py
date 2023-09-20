import math
from dataclasses import dataclass
from play import Play
from typing import Protocol, Iterator

class InvoiceFormatter(Protocol):
    pass
    
class TextFormatter(InvoiceFormatter):
    def __init__(self, customer):
        self._customer: str = customer

@dataclass
class InvoiceLine:
    play: Play
    audience: int
    cost: int
    credits: int

class Invoice:
    def __init__(self, customer):
        self._customer = customer
        self._total_cost = 0
        self._total_credits = 0
        self._lines: list[InvoiceLine] = []
    def add_performance(self, play, audience):
        cost = play.performance_cost(audience)
        credits = play.volume_credits(audience)
        self._lines.append(
            InvoiceLine(
                play,
                audience,
                cost,
                credits
            )
        )
        self._total_cost += cost
        self._total_credits += credits
    def line_items(self) -> Iterator[InvoiceLine]: return iter(self._lines)
    def customer(self) -> str: return self._customer
    def total_cost(self) -> int: return self._total_cost
    def total_credits(self) -> int: return self._total_credits

def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'
    
    plays = {
        id: Play(id, info["name"], info["type"])        
        for id, info in plays.items()
    }

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        
        this_amount = play.performance_cost(perf['audience'])
        volume_credits += play.volume_credits(perf['audience'])

        result += f' {play.name()}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


