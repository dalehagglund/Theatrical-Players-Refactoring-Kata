import json

import pytest
from approvaltests import verify
from approval_utilities.utils import get_adjacent_file

from statement import make_invoice, format_as_text

def test_example_statement():
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
    verify(
        format_as_text(make_invoice(invoice, plays))
    )


def test_statement_with_new_play_types():
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    with pytest.raises(ValueError) as exception_info:
        format_as_text(make_invoice(invoice, plays))
    assert "unknown type" in str(exception_info.value)
