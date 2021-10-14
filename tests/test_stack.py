import pytest

from rpn.stack import Operand, Stack, StackTooShort


def test_new_stack_has_no_values() -> None:
    stack = Stack()
    assert stack.values == []


def test_push_one_number() -> None:
    stack = Stack()
    stack.push(10)

    assert stack.values == [10]


def test_compute_addition() -> None:
    stack = Stack()
    stack.push(2)
    stack.push(5)
    stack.apply_operand(Operand.ADD)

    assert stack.values == [7]


def test_compute_subtraction() -> None:
    stack = Stack()
    stack.push(4)
    stack.push(1)
    stack.apply_operand(Operand.SUBTRACT)

    assert stack.values == [3]


def test_compute_multiplication() -> None:
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.apply_operand(Operand.MULTIPLY)

    assert stack.values == [6]


def test_compute_division() -> None:
    stack = Stack()
    stack.push(6)
    stack.push(2)
    stack.apply_operand(Operand.DIVIDE)

    assert stack.values == [3]


def test_on_stack_too_short() -> None:
    stack = Stack()
    stack.push(3)
    with pytest.raises(StackTooShort):
        stack.apply_operand(Operand.DIVIDE)


def test_clean() -> None:
    stack = Stack()
    stack.push(3)

    stack.clean()
    assert stack.values == []
