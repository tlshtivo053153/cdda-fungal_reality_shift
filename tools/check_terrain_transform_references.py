#!/usr/bin/env python3
#
# Terrain Transformation Reference Check Script
#
# This script checks if the IDs in the terrain transformation files under
# `mods/fungal_reality_shift/ter_furn_transform/wall` follow the naming convention
# `terrain_transform_frs_A_to_B` and if the references are consistent.
#
# Usage:
#   python3 check_terrain_transform_references.py
#
# The script will:
# 1. List all JSON files in the `mods/fungal_reality_shift/ter_furn_transform/wall` directory.
# 2. Read each JSON file and parse the `ter_furn_transform` definitions.
# 3. Check if the ID follows the naming convention `terrain_transform_frs_A_to_B`.
# 4. Store the transformation definitions in a dictionary.
# 5. Check for consistency in references (i.e., if `A` to `B` exists, `B` to `A` should also exist).
# 6. Output the results.

import os
import json
import re

# Define the directory path
directory_path = 'mods/fungal_reality_shift/ter_furn_transform/wall'

# Get a list of all JSON files in the directory
json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]

# Dictionary to store transformation definitions
transformations = {}

# Regular expression to match the naming convention
naming_convention = re.compile(r'^terrain_transform_frs_(.+)_to_(.+)$')

# Parse each JSON file
for file_name in json_files:
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            if item.get('type') == 'ter_furn_transform':
                transform_id = item.get('id')
                match = naming_convention.match(transform_id)
                if match:
                    source = match.group(1)
                    target = match.group(2)
                    if source not in transformations:
                        transformations[source] = {}
                    if target not in transformations[source]:
                        transformations[source][target] = []
                    transformations[source][target].append(file_name)
                else:
                    print(f"ID '{transform_id}' in file '{file_name}' does not follow the naming convention.")

# Check for consistency in references
print("Checking for consistent references...")
for source, targets in transformations.items():
    for target in targets:
        if target in transformations and source in transformations[target]:
            print(f"Consistent reference: {source} <-> {target}")
        else:
            print(f"Inconsistent reference: {source} -> {target} (missing reverse: {target} -> {source})")

# Summary
print("\nSummary:")
print(f"Total transformations: {sum(len(targets) for targets in transformations.values())}")
print(f"Unique sources: {len(transformations)}")
print(f"Unique targets: {len(set(target for targets in transformations.values() for target in targets))}")