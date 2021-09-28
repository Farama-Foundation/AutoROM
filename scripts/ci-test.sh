#!/usr/bin/env bash
set -e

test_init() {
  set -e
  python -m venv env
  source env/bin/activate

  pip install -U pip setuptools
  pip install multi-agent-ale-py ale-py
}

test_cleanup() {
  set -e
  deactivate
  rm -r env
}

# Test procedure
test_autorom() {
  set -e
  # Get install flag
  local install_to_pkgs=false
  while getopts 'i' opt; do
    case $opt in
        i) install_to_pkgs=true ;;
    esac
  done

  # Work in roms directory
  mkdir -p roms && pushd roms

  # Install locally
  AutoROM --accept-license --install-dir . && ls -l

  # Conditionally install to packages
  if [ "$install_to_pkgs" = true ]; then
    AutoROM --accept-license
  fi

  # Print ROMs the ALE can find
  python -c "import ale_py.roms as roms; print(roms.__all__)"

  # Cleanup
  popd && rm -r roms
}

./scripts/build-dist.sh

# Test local pip insall with installing to packages
echo "::group::Test AutoROM CLI install"
test_init

pip install --find-links dist/ --no-cache-dir AutoROM

test_autorom -i
test_cleanup
echo "::endgroup::"

# Test installing the source dist
echo "::group::Test AutoROM no install"
test_init
pip install --find-links dist/ --no-cache-dir AutoROM

test_autorom
test_cleanup
echo "::endgroup::"

# Test installing the source dist when accepting the license
echo "::group::Test AutoROM[accept-rom-license]"
test_init
pip install --find-links dist/ --no-cache-dir AutoROM[accept-rom-license]

test_autorom
test_cleanup
echo "::endgroup::"
