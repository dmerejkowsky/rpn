import uuid
from typing import Dict, List

from rpn.errors import Error
from rpn.stack import Stack


class NoSuchStack(Error):
    def __init__(self, id: str) -> None:
        self.id = id


class Repository:
    def __init__(self) -> None:
        self.stacks: Dict[str, Stack] = {}

    def create_stack(self) -> str:
        stack_id = str(uuid.uuid4())
        self.stacks[stack_id] = Stack()
        return stack_id

    def get_stack(self, id: str) -> Stack:
        res = self.stacks.get(id)
        if res is None:
            raise NoSuchStack(id)
        return res

    def get_stack_ids(self) -> List[str]:
        return list(self.stacks.keys())

    def delete_stack(self, id: str) -> None:
        self.stacks.pop(id, None)
