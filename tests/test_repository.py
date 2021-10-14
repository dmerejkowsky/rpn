import pytest

from rpn.repository import NoSuchStack, Repository


def test_create_stack() -> None:
    repository = Repository()
    stack_id = repository.create_stack()
    assert stack_id


def test_retrieve_stack() -> None:
    repository = Repository()
    stack_id = repository.create_stack()

    stack = repository.get_stack(stack_id)
    assert stack.values == []


def test_no_such_task_id() -> None:
    repository = Repository()
    with pytest.raises(NoSuchStack) as e:
        repository.get_stack("no-such-id")
    assert e.value.id == "no-such-id"


def test_delete_stack() -> None:
    repository = Repository()
    stack_id = repository.create_stack()

    repository.delete_stack(stack_id)
    with pytest.raises(NoSuchStack):
        repository.get_stack(stack_id)
