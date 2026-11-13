# Copyright (c) 2025-2026 Brett T. Warden

"""Tests for the AREDN Node API client."""

from __future__ import annotations

from custom_components.aredn_node.api import _parse_hostish


def test_parse_hostish_plain_host():
    host, ssl, port = _parse_hostish("node.local.mesh")
    assert host == "node.local.mesh"
    assert ssl is False
    assert port is None


def test_parse_hostish_host_port():
    host, ssl, port = _parse_hostish("10.0.0.1:8443")
    assert host == "10.0.0.1"
    assert ssl is False
    assert port == 8443


def test_parse_hostish_https_url():
    host, ssl, port = _parse_hostish("https://node.example.com:8443")
    assert host == "node.example.com"
    assert ssl is True
    assert port == 8443