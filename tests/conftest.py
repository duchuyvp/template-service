import pathlib
from typing import Any, Generator

import pytest
import utils
from fastapi import testclient

from core.adapters import create_component_factory
from template_service.adapters.orm import registry, component_factory
from core.adapters import sqlalchemy_adapter
from template_service.entrypoints.rest.app import app
from template_service.adapters import orm


@pytest.fixture(scope="session")
def project_path() -> Generator[pathlib.Path, Any, None]:
    yield pathlib.Path(__file__).parents[1]


@pytest.fixture(scope="session")
def config_path(project_path: pathlib.Path) -> str:
    return str(project_path / ".configs")


@pytest.fixture(scope="session")
def config(config_path: str) -> Generator[dict[str, Any], Any, None]:
    yield utils.load_config(config_path)


@pytest.fixture(scope="session")
def rest_client(config: dict[str, Any]) -> Generator[testclient.TestClient, Any, None]:
    yield testclient.TestClient(app)

    # Clean up
    component_factory = create_component_factory(config)
    assert isinstance(component_factory, sqlalchemy_adapter.ComponentFactory)
    registry.metadata.drop_all(bind=component_factory.engine)
