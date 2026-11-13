# Copyright (c) 2025-2026 Brett T. Warden
#
# SPDX-License-Identifier: MIT

"""Constants for the AREDN Node integration."""

from logging import Logger, getLogger

from homeassistant.const import Platform

LOGGER: Logger = getLogger(__package__)

DOMAIN = "aredn_node"
MANUFACTURER = "Amateur Radio Emergency Data Network"
AREDN_FIRMWARE_CONFIG_URL = "http://downloads.arednmesh.org/afs/www/config.js"

# How often the published firmware version is re-fetched, in seconds.
AREDN_FIRMWARE_CONFIG_REFRESH_INTERVAL = 6 * 60 * 60

CONF_FIRMWARE_CONFIG_URL = "firmware_config_url"
PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.DEVICE_TRACKER,
    Platform.UPDATE,
]
