# Простые тесты для калькулятора

from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("✓ add() tests passed")

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    print("✓ divide() tests passed")

if __name__ == "__main__":
    test_add()
    test_divide()
    print("All tests passed!")
