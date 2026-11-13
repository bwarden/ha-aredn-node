"""Constants for the AREDN Node integration."""

from logging import Logger, getLogger

from homeassistant.const import Platform

LOGGER: Logger = getLogger(__package__)

DOMAIN = "aredn_node"
MANUFACTURER = "Amateur Radio Emergency Data Network"
AREDN_FIRMWARE_CONFIG_URL = "http://downloads.arednmesh.org/afs/www/config.js"
PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.DEVICE_TRACKER,
    Platform.UPDATE,
]
