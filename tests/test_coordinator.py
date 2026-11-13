# Copyright (c) 2025-2026 Brett T. Warden
"""Tests for the AREDN Node coordinator."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from custom_components.aredn_node.coordinator import (
    _LATEST_FIRMWARE_CACHE,
    ArednNodeDataUpdateCoordinator,
)


@pytest.fixture(autouse=True)
def clear_cache():
    """Clear the shared firmware version cache between tests."""
    _LATEST_FIRMWARE_CACHE.clear()
    yield
    _LATEST_FIRMWARE_CACHE.clear()


@pytest.mark.asyncio
async def test_fetch_latest_firmware_version_parses_default_version():
    """The published default_version is extracted from config.js."""
    hass = MagicMock()
    entry = MagicMock()
    entry.data = {}
    entry.options = {}
    coordinator = ArednNodeDataUpdateCoordinator(
        hass=hass,
        logger=__import__("logging").getLogger("test"),
        name="test",
        update_interval=__import__("datetime").timedelta(seconds=60),
        config_entry=entry,
    )

    response = AsyncMock()
    response.raise_for_status = MagicMock()
    response.text = AsyncMock(return_value='default_version: "4.26.10.0",')
    response.__aenter__ = AsyncMock(return_value=response)
    response.__aexit__ = AsyncMock(return_value=None)

    session = MagicMock()
    session.get = MagicMock(return_value=response)

    with patch(
        "custom_components.aredn_node.coordinator.async_get_clientsession",
        return_value=session,
    ):
        version = await coordinator._async_fetch_latest_firmware_version()

    assert version == "4.26.10.0"


@pytest.mark.asyncio
async def test_fetch_latest_firmware_version_uses_cache():
    """Repeated calls within the TTL do not re-fetch."""
    hass = MagicMock()
    entry = MagicMock()
    entry.data = {}
    entry.options = {}
    coordinator = ArednNodeDataUpdateCoordinator(
        hass=hass,
        logger=__import__("logging").getLogger("test"),
        name="test",
        update_interval=__import__("datetime").timedelta(seconds=60),
        config_entry=entry,
    )

    response = AsyncMock()
    response.raise_for_status = MagicMock()
    response.text = AsyncMock(return_value='default_version: "4.26.10.0"')
    response.__aenter__ = AsyncMock(return_value=response)
    response.__aexit__ = AsyncMock(return_value=None)

    session = MagicMock()
    session.get = MagicMock(return_value=response)

    with patch(
        "custom_components.aredn_node.coordinator.async_get_clientsession",
        return_value=session,
    ):
        await coordinator._async_fetch_latest_firmware_version()
        await coordinator._async_fetch_latest_firmware_version()

    assert session.get.call_count == 1
