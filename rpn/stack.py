from collections import deque
from enum import Enum
from typing import Deque, List

from rpn.errors import Error
from typing import Dict
from typing import Any


class EmptyStack(Error):
    pass


class StackTooShort(Error):
    pass


class Operand(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


class Stack:
    def __init__(self) -> None:
        self._values: Deque[int] = deque()

    @property
    def values(self) -> List[int]:
        """This returns a copy of the _values Deque,
        so that users of the stack class have no way
        of messing up the stack
        """
        return list(self._values)

    def push(self, number: int) -> None:
        self._values.append(number)

    def clean(self) -> None:
        self._values.clear()

    def to_json(self) -> Dict[str, Any]:
        return {"values": self.values}

    def apply_operand(self, operand: Operand) -> None:
        # Note: all operands have the same arity : 2
        try:
            x = self._values.pop()
            y = self._values.pop()
        except IndexError:
            raise StackTooShort
        res = None
        if operand == Operand.ADD:
            res = y + x
        elif operand == Operand.SUBTRACT:
            res = y - x
        elif operand == Operand.MULTIPLY:
            res = y * x
        elif operand == Operand.DIVIDE:
            res = y // x
        assert res, f"operand '{operand}' not handled"
        self._values.append(res)
