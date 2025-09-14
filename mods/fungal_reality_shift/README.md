# Fungal Reality Shift

A MOD where eating a specific item causes random terrain changes around the player, inspired by Noita.

## Features
- Eating a "fungal spore" item starts a 24-hour effect that randomly transforms terrain around the player every minute.
- Terrain transformations include walls (concrete, wood, etc.) and liquids (water, lava, etc.).
- Obtain fungal spores by disassembling fungal creatures.
- Includes chocolate-themed items that can be used for various purposes.

## Installation
1. Place the "fungal_reality_shift" folder in your CDDA mods directory.
2. Enable the mod in the game's mod selection menu.

## Usage
1. Find or craft a "fungal spore" item.
2. Eat the item to activate the terrain transformation effect.
3. Observe as the world around you shifts and changes over the next 24 hours.

## File Structure
```
mods/fungal_reality_shift/
├── modinfo.json
├── README.md
├── CHANGELOG.md
├── effects/
│   └── fungal_reality_shift_active.json
├── effects_on_condition/
│   ├── portal_monster_spawn.json
│   ├── portal_wall_check.json
│   └── terrain_transformation/
│       ├── terrain_transformation.json
│       ├── liquid/
│       │   ├── dynamic_eoc.json
│       │   ├── terrain_transformation_acid.json
│       │   ├── terrain_transformation_honey.json
│       │   ├── terrain_transformation_lava.json
│       │   ├── terrain_transformation_liquid_fuel.json
│       │   ├── terrain_transformation_milk.json
│       │   ├── terrain_transformation_sap.json
│       │   ├── terrain_transformation_sewage.json
│       │   ├── terrain_transformation_slime.json
│       │   ├── terrain_transformation_water_dp.json
│       │   ├── terrain_transformation_water_sh.json
│       │   └── terrain_transformation_whiskey.json
│       └── wall/
│           ├── dynamic_eoc.json
│           ├── terrain_transformation_brick_wall.json
│           ├── terrain_transformation_chocolate_wall.json
│           ├── terrain_transformation_concrete_wall.json
│           ├── terrain_transformation_fungus_wall.json
│           ├── terrain_transformation_gold_wall.json
│           ├── terrain_transformation_paper.json
│           ├── terrain_transformation_sconc_wall.json
│           ├── terrain_transformation_strconc_wall.json
│           ├── terrain_transformation_wall_log.json
│           ├── terrain_transformation_wall_metal.json
│           ├── terrain_transformation_wall_portal.json
│           ├── terrain_transformation_wall_resin.json
│           ├── terrain_transformation_wall_wood.json
│           └── terrain_transformation_wall.json
├── items/
│   ├── fungal_spore.json
│   ├── items_chocolate_chunk.json
│   ├── json_flag_flammable.json
│   └── liquid_fuel.json
├── lang/
│   └── mo/
│       └── ja/
│           └── LC_MESSAGES/
├── recipes/
│   ├── .gitkeep
│   ├── fungal_spore_creation.json
│   └── recipe_liquid_fuel.json
├── ter_furn_transform/
│   ├── liquid/
│   │   ├── terrain_transformation_acid.json
│   │   ├── terrain_transformation_honey.json
│   │   ├── terrain_transformation_lava.json
│   │   ├── terrain_transformation_liquid_fuel.json
│   │   ├── terrain_transformation_milk.json
│   │   ├── terrain_transformation_sap.json
│   │   ├── terrain_transformation_sewage.json
│   │   ├── terrain_transformation_slime.json
│   │   ├── terrain_transformation_water_dp.json
│   │   ├── terrain_transformation_water_sh.json
│   │   └── terrain_transformation_whiskey.json
│   └── wall/
│       ├── terrain_transformation_brick_wall.json
│       ├── terrain_transformation_chocolate_wall.json
│       ├── terrain_transformation_concrete_wall.json
│       ├── terrain_transformation_fungus_wall.json
│       ├── terrain_transformation_gold_wall.json
│       ├── terrain_transformation_paper.json
│       ├── terrain_transformation_sconc_wall.json
│       ├── terrain_transformation_strconc_wall.json
│       ├── terrain_transformation_wall_log.json
│       ├── terrain_transformation_wall_metal.json
│       ├── terrain_transformation_wall_portal.json
│       ├── terrain_transformation_wall_resin.json
│       ├── terrain_transformation_wall_wood.json
│       └── terrain_transformation_wall.json
└── terrain/
    ├── liquids.json
    └── walls.json
├── tileset/
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