#!/usr/bin/env python3
"""
Tileset Image and JSON File Generation Script

This tool concatenates images in the `tileset/src` directory to create a tileset image `mods/fungal_reality_shift/tileset/32x32.png`,
and simultaneously generates a tileset definition file `mods/fungal_reality_shift/tileset/32x32.json`.

## Usage

```bash
python tools/create_tileset.py
```

## Requirements

- Python 3.x
- Pillow library

## Installation

```bash
pip install Pillow
```

## Directory Structure

- `tileset/src/32x32/`: Directory to store source image files
- `mods/fungal_reality_shift/tileset/`: Directory to store generated tileset images and JSON files

## Notes

- All source images must be the same size.
- Images are concatenated to the tileset in alphabetical order by filename.
"""

import os
import json
from PIL import Image


def get_image_files(src_dir):
    """
    Get image files from the source directory
    """
    image_files = []
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                # Exclude files (background image)
                if file != "terrain_background.png":
                    image_files.append(os.path.join(root, file))
    return image_files


def create_tileset_image(image_files, output_path):
    """
    Concatenate image files to create a tileset image
    """
    # Load images
    images = [Image.open(file) for file in image_files]
    
    # Check image size (assuming all images are the same size)
    if not images:
        print("No images found.")
        return
    
    tile_width, tile_height = images[0].size
    
    # Concatenate images (side by side)
    total_width = tile_width * len(images)
    max_height = max(image.height for image in images)
    
    # Create a new image
    combined_image = Image.new('RGBA', (total_width, max_height))
    
    # Paste images
    for i, image in enumerate(images):
        combined_image.paste(image, (i * tile_width, 0))
    
    # Save the image
    combined_image.save(output_path)
    print(f"Tileset image saved: {output_path}")


def create_tileset_json(image_files, output_path, tileset_image_path, background_image_path=None):
    """
    Create a tileset JSON file corresponding to the image files
    """
    # Load existing JSON file (if any)
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = [
            {
                "type": "mod_tileset",
                "compatibility": [
                    "MshockXottoplus", "UNDEAD_PEOPLE_BASE", "MSX++DEAD_PEOPLE",
                    "MSX++DEAD_PEOPLE+", "UNDEAD_PEOPLE", "MSX++ZaragaTiles",
                    "UltimateCataclysm", "Chibi_Ultica"
                ],
                "tiles-new": [
                    {
                        "file": tileset_image_path,
                        "sprite_height": 32,
                        "sprite_width": 32,
                        "tiles": []
                    }
                ]
            }
        ]
    
    # Update tile information
    tiles = data[0]["tiles-new"][0]["tiles"]
    tiles.clear()  # Clear existing tile information
    
    for i, file in enumerate(image_files):
        # Generate ID from filename
        id_name = os.path.splitext(os.path.basename(file))[0]
        
        # For terrain files, add a "bg" field
        # The index for "fg" needs to account for the background image being the first tile (index 0)
        fg_index = i + 1 if (background_image_path and os.path.exists(background_image_path)) else i
        if "terrain" in file and "terrain_background" not in file:
            tiles.append({"id": id_name, "fg": fg_index, "bg": 0})
        else:
            tiles.append({"id": id_name, "fg": fg_index})
    
    # Save JSON file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Tileset JSON file saved: {output_path}")


def main():
    """
    Main function
    """
    src_dir = "tileset/src/32x32"
    output_image_path = "mods/fungal_reality_shift/tileset/32x32.png"
    output_json_path = "mods/fungal_reality_shift/tileset/32x32.json"
    tileset_image_path = "./tileset/32x32.png"
    background_image_path = os.path.join(src_dir, "terrain_background.png")
    
    # Check if source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory not found: {src_dir}")
        return
    
    # Create output directory
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    
    # Get image files (excluding background image)
    image_files = get_image_files(src_dir)
    if not image_files:
        print("No image files found.")
        return
    
    # Create tileset image
    # For image creation, we need to include the background image in the list
    all_image_files = [background_image_path] + image_files if (background_image_path and os.path.exists(background_image_path)) else image_files
    create_tileset_image(all_image_files, output_image_path)
    
    # Create tileset JSON file
    create_tileset_json(image_files, output_json_path, tileset_image_path, background_image_path)


if __name__ == "__main__":
    main()