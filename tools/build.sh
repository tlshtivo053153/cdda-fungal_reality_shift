#!/usr/bin/env bash

# Script to build the Fungal Reality Shift MOD
# Usage: ./build.sh [-h]
#   -h: Show this help message

# Default values
LANGUAGE="ja"
PO_FILE="lang/po/${LANGUAGE}.po"
MO_DIR="mods/fungal_reality_shift/lang/mo/${LANGUAGE}/LC_MESSAGES"
MO_FILE="${MO_DIR}/${LANGUAGE}.mo"
ZIP_FILE="fungal_reality_shift.zip"
MOD_DIR="mods"

# Parse command line options
while getopts "h" opt; do
  case $opt in
    h)
      echo "Usage: $0 [-h]"
      echo "  -h: Show this help message"
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Function to check command result
check_command() {
  if [ $? -ne 0 ]; then
    echo "Error: $1 failed." >&2
    exit 1
  fi
}

# Create directory for MO file
echo "Creating directory for MO file..."
mkdir -p "$MO_DIR"
check_command "mkdir -p $MO_DIR"

# Compile PO file to MO file
echo "Compiling PO file to MO file..."
msgfmt "$PO_FILE" -o "$MO_FILE"
check_command "msgfmt $PO_FILE -o $MO_FILE"

# Create ZIP file
echo "Creating ZIP file..."
zip -r "$ZIP_FILE" "$MOD_DIR"
check_command "zip -r $ZIP_FILE $MOD_DIR"

echo "Build completed successfully."