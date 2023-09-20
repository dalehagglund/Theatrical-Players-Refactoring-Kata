from statement import TextFormatter

def test_create_formatter():
    assert TextFormatter("sample customer") is not None
    
def test_empty_invoice():
    pass