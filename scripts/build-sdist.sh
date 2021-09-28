#!/usr/bin/env bash
set -e

# Build source-dist
pip install -U build

# Make sure dist exists
mkdir -p dist

# Build AutoROM
pushd packages/AutoROM
python -m build --sdist
popd

mv packages/AutoROM/dist/* dist/
rm -r packages/AutoROM/dist
rm -r packages/AutoROM/*.egg-info

# Build AutoROM.accept-rom-license
pushd packages/AutoROM.accept-rom-license
python -m build --sdist
popd

mv packages/AutoROM.accept-rom-license/dist/* dist/
rm -r packages/AutoROM.accept-rom-license/dist
rm -r packages/AutoROM.accept-rom-license/*.egg-info
