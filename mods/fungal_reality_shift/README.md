# Fungal Reality Shift

A MOD where eating a specific item causes random terrain changes around the player, inspired by Noita.

## Features
- Eating a "fungal spore" item starts a 24-hour effect that randomly transforms terrain around the player every minute.
- Terrain transformations include walls (concrete, wood, etc.) and liquids (water, lava, etc.).
- Obtain fungal spores by disassembling fungal creatures.

## Installation
1. Place the "fungal_reality_shift" folder in your CDDA mods directory.
2. Enable the mod in the game's mod selection menu.

## Usage
1. Find or craft a "fungal spore" item.
2. Eat the item to activate the terrain transformation effect.
3. Observe as the world around you shifts and changes over the next 24 hours.

## File Structure
```
external/cdda/data/mods/fungal_reality_shift/
├── modinfo.json
├── items/
│   ├── fungal_spore.json
│   └── fungal_dissection_recipe.json
├── effects_on_condition/
│   └── terrain_transformation.json
├── itemgroups/
│   └── fungal_loot.json
├── monsters/
│   └── fungal_dissection.json
└── README.md
```

## Testing
1. Create a new character and start a game
2. Find or spawn fungal_spore item
3. Eat the item and observe status effects
4. Move around and check for terrain changes every minute
5. Verify effect lasts for 24 hours
6. Disassemble fungal creatures to obtain items
7. Check that terrain changes persist after effect ends
8. Balance adjustments based on playtesting

## Known Issues
- None at this time.

## Changelog
- v1.0.0: Initial release