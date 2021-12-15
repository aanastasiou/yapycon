#!/bin/bash

# Builds the release archive
# Athanasios Anastasiou, Dec 2021

# If the release folder exists, erase and rebuild it.
if [ -f "yapycon.zip" ]; then
  rm yapycon.zip
fi

if [ -d "yapycon_release/" ]; then
  rm -rf yapycon_release/
fi

mkdir -p yapycon_release/doc
mkdir -p yapycon_release/yapycon

# Rebuild the documentation
pushd ./ && cd doc && make clean && make html && popd

# Copy required files (only).
# Docs
cp -r doc/build/html/* yapycon_release/doc
# Plugin
cp yapycon/yapycon.py yapycon_release/yapycon
cp yapycon/yasara_kernel.py yapycon_release/yapycon
cp requirements.txt yapycon_release/
# Installers
cp install_plugin.* yapycon_release/
cp uninstall_plugin.* yapycon_release/

zip -r yapycon.zip yapycon_release/*



