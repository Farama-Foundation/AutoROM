#!/usr/bin/env bash
set -e

# Get installation directory so we can remove ROMs between runs
# They're located in ${INSTALL_DIR}/roms/*.bin
INSTALL_DIR="$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/AutoROM"

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


test_cleanup() {
  pip uninstall -y AutoROM > /dev/null 2>&1
  pip uninstall -y AutoROM.accept-rom-license > /dev/null 2>&1
  rm ${INSTALL_DIR}/roms/*.bin 2>/dev/null || true
}


# Install deps
pip install multi-agent-ale-py ale-py
pip install click requests tqdm

./scripts/build-sdist.sh

# Test local pip insall with installing to packages
echo "::group::Test AutoROM CLI install"
pip install --find-links dist/ --no-index --no-cache-dir AutoROM

test_autorom -i
test_cleanup
echo "::endgroup::"

# Test installing the source dist
echo "::group::Test AutoROM no install"
pip install --find-links dist/ --no-index --no-cache-dir AutoROM

test_autorom
test_cleanup
echo "::endgroup::"

# Test installing the source dist when accepting the license
echo "::group::Test AutoROM[accept-rom-license]"
pip install --find-links dist/ --no-index --no-cache-dir AutoROM[accept-rom-license]

test_autorom
test_cleanup
echo "::endgroup::"
