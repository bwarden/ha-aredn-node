# AREDN Node Home Assistant integration

Custom integration (`custom_components/aredn_node`) for managing AREDN nodes.

## Dependency notes

- `requirements.txt` pins `homeassistant`. Home Assistant releases may raise
  their `requires-python` floor (e.g. 2026.10.0 needs Python >=3.14.2). When
  bumping the `homeassistant` dependency, check its `requires-python` and update
  `.github/workflows/lint.yml`, `.ruff.toml` (`target-version`), and
  `.devcontainer.json` to a compatible Python version at the same time.
- `hacs.json` carries the Marketplace-facing minimum Home Assistant version
  (`homeassistant` key) and may differ from the PyPI version in
  `requirements.txt`.