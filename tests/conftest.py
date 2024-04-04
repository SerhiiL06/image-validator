import pytest
from httpx import ASGITransport, AsyncClient

from main import app


@pytest.fixture(scope="session")
async def aclient():
    async with ASGITransport(app=app) as t:
        aclient = AsyncClient(
            transport=t,
            base_url="http://test",
        )
        yield aclient
