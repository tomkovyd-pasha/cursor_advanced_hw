import pytest
from functions_to_test import Calculator


def test_add() -> None:
    assert Calculator.add(1, 5) == 6
    assert Calculator.add(1.2446, 5.2884) == 6.533
    assert Calculator.add([1, 2, 4], [2, 5, 7]) == [1, 2, 4, 2, 5, 7]
    assert Calculator.add((1, 2, 4), (2, 5, 7)) == (1, 2, 4, 2, 5, 7)
    assert Calculator.add("tex1_1", "text_2") == "tex1_1text_2"
    with pytest.raises(TypeError):
        Calculator.add(1, "5")
        Calculator.add("1", 5)
        Calculator.add(1, "5")
        Calculator.add(None, 5)
        Calculator.add(5, None)
        Calculator.add(None, None)
        Calculator.add({1, 2, 4}, {2, 5, 7})
        Calculator.add([1, 2, 4], {2, 5, 7})
        Calculator.add({1, 2, 4}, [2, 5, 7])
        Calculator.add({"a": 2, "b": 1}, {"a": 2, "b": 1})


def test_subtract() -> None:
    assert Calculator.subtract(1, 5) == -4
    assert Calculator.subtract(1.2446, 5.2884) == -4.0438
    assert Calculator.subtract({1, 2, 4}, {2, 5, 7}) == {1, 4}
    assert Calculator.subtract({2, 5, 7}, {1, 2, 4}) == {5, 7}
    with pytest.raises(TypeError):
        Calculator.subtract("tex1_1", "text_2")
        Calculator.subtract(1, "5")
        Calculator.subtract("1", 5)
        Calculator.subtract(1, "5")
        Calculator.subtract(None, 5)
        Calculator.subtract(5, None)
        Calculator.subtract(None, None)
        Calculator.subtract({1, 2, 4}, [2, 5, 7])
        Calculator.subtract([1, 2, 4], [2, 5, 7])
        Calculator.subtract({"a": 2, "b": 1}, {"a": 2, "b": 1})


def test_multiply() -> None:
    assert Calculator.multiply(1, 5) == 5
    assert Calculator.multiply(1.2446, 5.2884) == 6.58194264
    assert Calculator.multiply("a", 4) == "aaaa"
    assert Calculator.multiply([1, 2], 2) == [1, 2, 1, 2]
    assert Calculator.multiply((1, 2), 2) == (1, 2, 1, 2)
    with pytest.raises(TypeError):
        Calculator.multiply("a", 4.532)
        Calculator.multiply(4.532, "a")
        Calculator.multiply({1, 2}, 2)
        Calculator.multiply({1, 2}, None)
        Calculator.multiply([1, 2], None)
        Calculator.multiply({"a": 2, "b": 1}, 2)
        Calculator.multiply(None, None)


def test_divide() -> None:
    assert Calculator.divide(1, 5) == 0.2
    assert Calculator.divide(0, 5) == 0
    assert Calculator.divide(1.2446, 5.2884) == 0.23534528401785038
    with pytest.raises(TypeError):
        Calculator.divide([1, 2], 7)
        Calculator.divide("[1, 2]", 7)
        Calculator.divide(7, None)
        Calculator.divide(None, 7)
    with pytest.raises(ValueError):
        Calculator.divide(7, 0)
        Calculator.divide("[1, 2]", 0)
        Calculator.divide([1, 2], 0)


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
