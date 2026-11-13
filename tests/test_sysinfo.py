# Copyright (c) 2025-2026 Brett T. Warden

"""Tests using a redacted real-node sysinfo sample."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock

from custom_components.aredn_node.update import ArednNodeFirmwareUpdate


def _load_sysinfo() -> dict:
    path = Path(__file__).parent / "fixtures" / "sysinfo.json"
    return json.loads(path.read_text())


def test_sysinfo_firmware_version():
    data = _load_sysinfo()
    assert data["node_details"]["firmware_version"] == "4.26.7.0"


def test_sysinfo_node_count():
    data = _load_sysinfo()
    assert len(data["nodes"]) == 1


def test_update_entity_has_update():
    coordinator = MagicMock()
    coordinator.data = _load_sysinfo()
    coordinator.data["latest_firmware_version"] = "4.26.10.0"
    coordinator.config_entry.entry_id = "test-entry"

    entity = ArednNodeFirmwareUpdate.__new__(ArednNodeFirmwareUpdate)
    entity.coordinator = coordinator
    assert entity.has_update is True
    assert entity.installed_version == "4.26.7.0"
    assert entity.latest_version == "4.26.10.0"
