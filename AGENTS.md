# AREDN Node Home Assistant integration

## Commit style

- Use kernel-style commits: imperative mood subject line, optional subsystem
  prefix, and a verbose body explaining *why* the change is made.
- One functional change per commit; do not mix unrelated fixes.
- Describe the change and its rationale in detail in the commit message.
- Include relevant error messages and tracebacks verbatim when the change
  fixes a specific failure, so the fix is discoverable by searching logs.

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