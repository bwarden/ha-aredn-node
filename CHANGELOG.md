# Changelog

## v1.5.0

- Fix options flow crash when opening integration options (property
  `config_entry` has no setter on Home Assistant 2026).
- Keep entities available with their last known values during transient
  network outages instead of marking them unavailable.
- Refactor reconfigure and options flows; apply ruff formatting across
  the integration.
- Add a local test suite and CI (pytest, ruff) plus a packaging script
  that ships the integration as a zip.
- Move the firmware refresh interval to a constant (6 hours).
- Replace `async_timeout` with `asyncio.timeout`.
- Dependabot dependency and GitHub Actions updates.

## v1.4.1

- Fix options flow crash when opening integration options.

## v1.4.0

- Fix deprecated `TrackerEntity` import for current Home Assistant.
- Add a per-node firmware update entity comparing the installed firmware
  version with the latest published AREDN version.
- Move the firmware download URL into constants and expose it as a
  configuration option (defaults to the AREDN downloads site).
- Replace HACS references with the Home Assistant Marketplace and rename the
  repository to `ha-aredn-node`.
- Bump the minimum Home Assistant version to 2026.10.0 and Python to 3.14.
- Add SPDX copyright/license headers to Python files.