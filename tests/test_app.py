from typing import List

from flask.testing import FlaskClient

from rpn.repository import Repository


def test_create_stack(client: FlaskClient, repository: Repository) -> None:
    response = client.post("/rpn/stack")
    assert response.status_code == 201
    assert response.json
    stack_id = response.json["id"]
    assert stack_id

    assert repository.get_stack(stack_id)


def test_list_stacks(client: FlaskClient, repository: Repository) -> None:
    id_one = repository.create_stack()
    id_two = repository.create_stack()

    response = client.get("/rpn/stack")
    assert response.json
    assert response.status_code == 200

    actual = response.json["stacks"]
    assert actual == [{"id": id_one}, {"id": id_two}]


def test_list_operands(client: FlaskClient) -> None:
    response = client.get("/rpn/op")

    assert response.status_code == 200
    assert response.json
    actual = response.json["operands"]
    assert actual == ["+", "-", "*", "/"]


def test_push_to_stack(client: FlaskClient, repository: Repository) -> None:
    stack_id = repository.create_stack()

    response = client.post(f"/rpn/stack/{stack_id}", json={"value": 42})
    assert response.status_code == 200

    actual = repository.get_stack(stack_id)
    assert actual.values == [42]


def make_stack(repository: Repository, values: List[int]) -> str:
    stack_id = repository.create_stack()
    stack = repository.get_stack(stack_id)
    for value in values:
        stack.push(value)
    return stack_id


def test_get_stack(client: FlaskClient, repository: Repository) -> None:
    stack_id = make_stack(repository, [1, 2])

    response = client.get(f"/rpn/stack/{stack_id}")

    assert response.status_code == 200
    assert response.json

    actual = response.json["values"]
    assert actual == [1, 2]


def test_apply_operand(client: FlaskClient, repository: Repository) -> None:
    stack_id = make_stack(repository, [4, 1])

    response = client.post(f"/rpn/op/+/stack/{stack_id}")
    assert response.status_code == 200

    actual = repository.get_stack(stack_id)
    assert actual.values == [5]
