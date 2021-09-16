#!/usr/bin/env bash
set -e

# Build source-dist
pip install -U build
python -m build --sdist

# Work in dist
pushd dist

# Extract and delete old archive
tar -xzvf *.tar.gz
find * -type f -maxdepth 0 -name "*.tar.gz" -delete

# Find the requires.txt file and replace our absolute directory
# with a relative directory.
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  find * -type f -path "*.egg-info/requires.txt" -exec sed -i "s/file:\/\/localhost\/.*\/AutoROM/.\/AutoROM/g" {} +
elif [[ "$OSTYPE" == "darwin"* ]]; then
  find * -type f -path "*.egg-info/requires.txt" -exec sed -i "" "s/file:\/\/localhost\/.*\/AutoROM/.\/AutoROM/g" {} +
fi

# Create our new archive with the folders name
find * -type d -maxdepth 0 -exec sh -c \
  'tar -zcvf "$0.tar.gz" $0' {} \;
# Delete the old folder
find * -type d -maxdepth 0 -exec rm -r {} +

popd
