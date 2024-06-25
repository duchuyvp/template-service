import pathlib
from typing import Any, Generator

import pytest
import utils
from fastapi import testclient

from user_service.entrypoints.rest.app import app


@pytest.fixture(scope="session")
def project_path() -> Generator[pathlib.Path, Any, None]:
    yield pathlib.Path(__file__).parents[1]


@pytest.fixture(scope="session")
def config_path(project_path: pathlib.Path) -> str:
    return str(project_path / ".configs")


@pytest.fixture
def config(config_path: str) -> Generator[dict[str, Any], Any, None]:
    yield utils.load_config(config_path)


@pytest.fixture
def rest_client() -> Generator[testclient.TestClient, Any, None]:
    yield testclient.TestClient(app)
