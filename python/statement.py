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

def format_as_text(inv: Invoice) -> str:
    def format_as_dollars(amount):
        return f"${amount:0,.2f}"
    def statement_title(customer):
        return f'Statement for {customer}\n'
    def performance_line(item):
        name = item.play.name()
        cost = item.cost
        audience = item.audience
        return f' {name}: {format_as_dollars(cost/100)} ({audience} seats)\n'

    output_lines = []
    output_lines.append(
        statement_title(inv.customer())
    )
    output_lines.extend(
        performance_line(item)
        for item in inv.line_items()
    )
    output_lines.append(
        f'Amount owed is {format_as_dollars(inv.total_cost()/100)}\n'
    )
    output_lines.append(
        f'You earned {inv.total_credits()} credits\n'
    )
    
    return "".join(output_lines)

def make_invoice(invoice, plays):
    plays = {
        id: Play(id, info["name"], info["type"])        
        for id, info in plays.items()
    }

    inv = Invoice(invoice["customer"])
    for perf in invoice["performances"]:
        inv.add_performance(plays[perf["playID"]], perf["audience"])

    return inv