import pytest
from flask import Flask

from rpn.app import create_app
from rpn.repository import Repository


@pytest.fixture
def repository() -> Repository:
    return Repository()


@pytest.fixture
def app(repository: Repository) -> Flask:
    app = create_app(test_repository=repository)
    return app
