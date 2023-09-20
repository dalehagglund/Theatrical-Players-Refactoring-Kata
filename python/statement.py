import math
from dataclasses import dataclass

class Play:
    def __init__(self, id: str, name: str, type: str):
        if type not in ("tragedy", "comedy"):
            raise ValueError(f'unknown type: {type}')
        self._id: str = id
        self._name: str = name
        self._type: str = type
        
    def id(self) -> str: return self._id
    def name(self) -> str: return self._name

    def performance_cost(self, audience: int) -> int:
        if self._type == "tragedy":
            return 40000 + 1000 * max(0, audience - 30)
        elif self._type == "comedy":
            return (
                30000 
                + (300 * audience)
                + (10000 if  audience > 20 else 0)
                + 500 * max(0, audience - 20)
            )
        else:
            raise ValueError(f'unknown type: {self.type}')
            
    def volume_credits(self, audience: int) -> int:
        credits = 0
        credits += max(audience - 30, 0)
        if self._type == "comedy":
            credits += audience // 5
        return credits

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


