from typing import Any, Dict, Optional, Tuple

import flask
from flask import Flask, abort

from rpn.repository import NoSuchStack, Repository
from rpn.stack import Operand, Stack

JsonResponse = Tuple[Dict[str, Any], int]


def get_stack_or_404(repository: Repository, stack_id: str) -> Stack:
    try:
        stack = repository.get_stack(stack_id)
    except NoSuchStack as e:
        abort(404, str(e))
    return stack


def create_app(test_repository: Optional[Repository] = None) -> Flask:
    app = Flask(__name__)
    repository = test_repository or Repository()

    @app.route("/rpn/op", methods=["GET"])
    def get_operands() -> JsonResponse:
        return {"operands": [o.value for o in Operand]}, 200

    @app.route("/rpn/stack", methods=["POST"])
    def create_stack() -> JsonResponse:
        stack_id = repository.create_stack()

        return {"id": stack_id}, 201

    @app.route("/rpn/stack", methods=["GET"])
    def list_stacks() -> JsonResponse:
        return {"stacks": [{"id": id} for id in repository.get_stack_ids()]}, 200

    @app.route("/rpn/stack/<stack_id>", methods=["GET"])
    def get_stack(stack_id: str) -> JsonResponse:
        stack = get_stack_or_404(repository, stack_id)
        return stack.to_json(), 200

    @app.route("/rpn/stack/<stack_id>", methods=["POST"])
    def push_value(stack_id: str) -> JsonResponse:
        json_request = flask.request.json
        if not json_request:
            abort(400)
        value = json_request["value"]

        stack = get_stack_or_404(repository, stack_id)

        stack.push(value)

        return stack.to_json(), 200

    @app.route("/rpn/op/<op>/stack/<stack_id>", methods=["POST"])
    def apply_operand(op: str, stack_id: str) -> JsonResponse:
        try:
            operand = Operand(op)
        except ValueError as e:
            abort(400, str(e))

        stack = get_stack_or_404(repository, stack_id)
        stack.apply_operand(operand)

        return stack.to_json(), 200

    return app
