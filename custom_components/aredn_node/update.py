# Copyright (c) 2025-2026 Brett T. Warden
#
# SPDX-License-Identifier: MIT

"""Update platform for AREDN Node integration."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.update import (
    UpdateDeviceClass,
    UpdateEntity,
)
from homeassistant.helpers.entity import EntityCategory

from .entity import ArednNodeEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import ArednNodeDataUpdateCoordinator
    from .data import ArednNodeConfigEntry


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001
    entry: ArednNodeConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the update platform."""
    async_add_entities(
        [ArednNodeFirmwareUpdate(coordinator=entry.runtime_data.coordinator)]
    )


class ArednNodeFirmwareUpdate(ArednNodeEntity, UpdateEntity):
    """AREDN Node firmware update entity."""

    _attr_device_class = UpdateDeviceClass.FIRMWARE
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_name = "Firmware Update"

    def __init__(self, coordinator: ArednNodeDataUpdateCoordinator) -> None:
        """Initialize the update entity."""
        super().__init__(coordinator)
        node_name = coordinator.data.get("node")
        self._attr_name = f"{node_name} Firmware Update"
        self._attr_unique_id = f"{coordinator.config_entry.entry_id}-firmware_update"
        self._attr_title = "AREDN Firmware"

    @property
    def installed_version(self) -> str | None:
        """Return the currently installed firmware version."""
        return self.coordinator.data.get("node_details", {}).get("firmware_version")

    @property
    def latest_version(self) -> str | None:
        """Return the latest available firmware version."""
        return self.coordinator.data.get("latest_firmware_version")

    @property
    def has_update(self) -> bool:
        """Return True if an update is available."""
        installed = self.installed_version
        latest = self.latest_version
        return bool(installed and latest and installed != latest)
