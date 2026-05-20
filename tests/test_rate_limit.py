from fastapi import HTTPException
from unittest.mock import AsyncMock

import pytest

from auth.rate_limit import rate_limit


class FakeRequest:
    class Client:
        host = "127.0.0.1"

    client = Client()


@pytest.mark.asyncio
async def test_anonymous_not_limited(monkeypatch):

    from auth import rate_limit as rl

    rl.r = AsyncMock()

    rl.r.zcard.return_value = 1

    request = FakeRequest()

    await rate_limit(request)


@pytest.mark.asyncio
async def test_anonymous_limited(monkeypatch):

    from auth import rate_limit as rl

    rl.r = AsyncMock()

    rl.r.zcard.return_value = 2

    request = FakeRequest()

    with pytest.raises(HTTPException) as exc:
        await rate_limit(request)

    assert exc.value.status_code == 429


@pytest.mark.asyncio
async def test_authenticated_not_limited(monkeypatch):

    from auth import rate_limit as rl

    rl.r = AsyncMock()

    rl.r.zcard.return_value = 5

    request = FakeRequest()

    await rate_limit(request, "admin")


@pytest.mark.asyncio
async def test_authenticated_limited(monkeypatch):

    from auth import rate_limit as rl

    rl.r = AsyncMock()

    rl.r.zcard.return_value = 10

    request = FakeRequest()

    with pytest.raises(HTTPException) as exc:
        await rate_limit(request, "admin")

    assert exc.value.status_code == 429