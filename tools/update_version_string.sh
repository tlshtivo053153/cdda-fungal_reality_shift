#!/usr/bin/env bash

# Get version from the first argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <new_version>"
  echo "Example: $0 1.2.1"
  exit 1
fi

VERSION="$1"
TARGET_FILE="mods/fungal_reality_shift/modinfo.json"

# Check if the target file exists
if [ ! -f "$TARGET_FILE" ]; then
  echo "Error: Target file '$TARGET_FILE' does not exist."
  exit 1
fi

# Update the version field value with sed
# The regular expression matches the "vX.Y.Z" format string after "version":
if sed -i -E "s/(\"version\":\s*\")v[0-9]+\.[0-9]+\.[0-9]+(\".*)/\1v$VERSION\2/" "$TARGET_FILE"; then
  echo "Successfully updated version to v$VERSION in $TARGET_FILE"
else
  echo "Error: Failed to update version in $TARGET_FILE"
  exit 1
fi