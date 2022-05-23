from app.calculations import add,subtract,multiply,divide

def test_add():
    print("testing add function")
    assert add(5,3) == 8
    
def test_subtract():
    assert subtract(9, 4) == 5
    
def test_multiply():
    assert multiply(2, 4) == 8
    
def test_divide():
    assert divide(8, 2) == 4