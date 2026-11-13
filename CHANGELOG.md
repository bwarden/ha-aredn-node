# Changelog

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