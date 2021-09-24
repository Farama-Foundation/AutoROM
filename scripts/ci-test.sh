#!/usr/bin/env bash
set -e

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

# Get installation directory so we can remove ROMs between runs
# They're located in ${INSTALL_DIR}/roms/*.bin
INSTALL_DIR="$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/AutoROM"

# Install deps
pip install multi-agent-ale-py ale-py

# Test local pip insall with installing to packages
echo "::group::Test pip install"

pip install . --verbose
test_autorom -i
pip uninstall -y AutoROM > /dev/null 2>&1
rm ${INSTALL_DIR}/roms/*.bin 2>/dev/null || true
echo "::endgroup::"

# Test installing the source dist
echo "::group::Test sdist install"

./scripts/build-sdist.sh
pushd dist
pwd
find * -type f -name "*.tar.gz" -exec sh -c \
  'pip install $0 --verbose' {} +
pwd
popd
test_autorom
pip uninstall -y AutoROM > /dev/null 2>&1
rm ${INSTALL_DIR}/roms/*.bin 2>/dev/null || true
echo "::endgroup::"

# Test installing the source dist when accepting the license
echo "::group::Test sdist install [accept-rom-license]"

./scripts/build-sdist.sh
pushd dist
find * -type f -name "*.tar.gz" -exec sh -c \
  'pip install $0[accept-rom-license] --verbose' {} +
popd
test_autorom
pip uninstall -y AutoROM AutoROM-licensed-roms > /dev/null 2>&1
rm ${INSTALL_DIR}/roms/*.bin 2>/dev/null || true
echo "::endgroup::"
