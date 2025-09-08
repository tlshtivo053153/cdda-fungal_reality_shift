#!/usr/bin/env bash

# Script to update PO files for the Fungal Reality Shift MOD
# Usage: ./update_po.sh [-h] [-l language] [-o output_dir]
#   -h: Show this help message
#   -l: Language code (default: ja)
#   -o: Output directory (default: lang/po)

# Default values
LANGUAGE="ja"
OUTPUT_DIR="lang/po"
INPUT_DIR="mods/fungal_reality_shift"
MOD_NAME="Fungal Reality Shift"

# Parse command line options
while getopts "hl:o:" opt; do
  case $opt in
    h)
      echo "Usage: $0 [-h] [-l language] [-o output_dir]"
      echo "  -h: Show this help message"
      echo "  -l: Language code (default: $LANGUAGE)"
      echo "  -o: Output directory (default: $OUTPUT_DIR)"
      exit 0
      ;;
    l)
      LANGUAGE="$OPTARG"
      ;;
    o)
      OUTPUT_DIR="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Check if required files/directories exist
if [ ! -d "$INPUT_DIR" ]; then
  echo "Error: Input directory '$INPUT_DIR' does not exist." >&2
  exit 1
fi

if [ ! -d "$OUTPUT_DIR" ]; then
  echo "Error: Output directory '$OUTPUT_DIR' does not exist." >&2
  exit 1
fi

# Define file paths
POT_FILE="$OUTPUT_DIR/translation.pot"
PO_FILE="$OUTPUT_DIR/${LANGUAGE}.po"

# Extract strings from JSON
echo "Extracting strings from JSON..."
if ! python external/cdda/lang/extract_json_strings.py -i "$INPUT_DIR" -r "$POT_FILE" -n "$MOD_NAME"; then
  echo "Error: Failed to extract strings from JSON." >&2
  exit 1
fi

# Initialize PO file
echo "Initializing PO file..."
if ! msginit -i "$POT_FILE" -o "$PO_FILE" -l "$LANGUAGE" --no-translator; then
  echo "Error: Failed to initialize PO file." >&2
  exit 1
fi

echo "PO file updated successfully."