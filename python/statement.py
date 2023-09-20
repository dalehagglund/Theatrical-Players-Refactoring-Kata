import math
from play import Play
from typing import Protocol

class InvoiceFormatter(Protocol):
    pass
    
class TextFormatter(InvoiceFormatter):
    pass
    
def statement(format: InvoiceFormatter, invoice, plays):
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


