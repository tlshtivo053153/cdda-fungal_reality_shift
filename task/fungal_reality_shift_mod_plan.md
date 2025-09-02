# Fungal Reality Shift MOD Plan

## Overview
- **Name**: Fungal Reality Shift
- **Concept**: A MOD where eating a specific item causes random terrain changes around the player, inspired by Noita.
- **Action Entity**: Player character only
- **Effect Range**: 20 tiles around the player
- **Effect Duration**: 24 hours (terrain changes every minute)
- **Terrain Changes**: Walls and liquids randomly transform into other terrains (e.g., concrete → wood, water → lava)
- **Item**: Modify existing items or obtain by disassembling fungal creatures

## Development Steps

### 1. Create MOD Basic Structure (modinfo.json)
- MOD ID: fungal_reality_shift
- Name: Fungal Reality Shift
- Author: KiloCode
- Description: A MOD where eating a specific item causes random terrain changes around the player
- Category: magical
- Dependencies: dda
- Version: v1.0.0

### 2. Create JSON File to Modify Existing Items
- Determine which existing items to modify
- Define item effects (trigger for terrain changes)
- Item name: fungal_spore
- Effect: When eaten, starts terrain transformation effect for 24 hours

### 3. Set Up to Obtain Items by Disassembling Fungal Creatures
- Determine which fungal creatures to target
- Define disassembly recipes and acquisition methods
- Target creatures: fungal zombie, fungal boomer, etc.
- Recipe: Disassemble 1 fungal creature to obtain 1-3 fungal_spore

### 4. Implement Terrain Change Logic (Using EOC)
- Use EOC (Effects On Condition) to implement terrain change triggers
- Implement processing every minute
- Logic for determining effect range (20 tiles around player)
- EOC ID: fungal_reality_shift_effect
- Trigger condition: Player has eaten fungal_spore within last 24 hours
- Effect: Randomly transform terrains in effect range

### 5. Define Terrain Change Rules
- Wall terrain transformations:
  - Concrete → Wood
  - Wood → Log
  - Log → Fungal matter
  - Metal → Fungal matter
  - Brick → Fungal matter
  - Other wall types → Fungal matter
- Liquid terrain transformations:
 - Water → Lava
  - Water → Liquid fuel
  - Water → Whiskey
  - Other liquids → Random liquid from pool

### 6. Implement Effect Duration Management
- Implement 24-hour countdown
- Processing for effect end (effect cancellation, maintaining transformed terrain)
- Timer: 24 hours (1440 minutes)
- Status effect: fungal_reality_shift_status
- When timer expires, remove status effect but keep terrain changes

### 7. Testing and Adjustment
- In-game testing
- Balance adjustments as needed
- Test scenarios:
  - Eating item and observing terrain changes
  - Checking effect range and duration
  - Verifying terrain transformation rules
  - Testing disassembly recipes

## Implementation Details

### Item: fungal_spore
- Type: COMESTIBLE
- Category: food
- Symbol: *
- Color: light_gray
- Description: A strange spore that seems to pulse with otherworldly energy. Eating it might have unexpected effects.
- Use function: Trigger fungal_reality_shift_effect EOC
- Price: 500 USD
- Material: fungal_matter
- Volume: 1ml
- Weight: 1g

### EOC: fungal_reality_shift_effect
- Type: EFFECT_ON_CONDITION
- Condition: Player has fungal_reality_shift_status
- Effect:
  - Every minute, transform random terrains in 20-tile radius
  - Roll for terrain transformation (20% chance per tile)
  - Apply terrain changes
  - Check if 24 hours have passed, if so remove status

### Terrain Transformation Rules
- Wall terrains (t_wall, t_concrete_wall, t_wood_wall, etc.):
  - 30% chance: t_wood_wall
  - 20% chance: t_log_wall
  - 20% chance: t_fungal_wall
  - 15% chance: t_metal_wall
  - 10% chance: t_brick_wall
  - 5% chance: t_paper_wall
- Liquid terrains (t_water_sh, t_water_dp, etc.):
  - 40% chance: t_lava
  - 20% chance: t_liquid_fuel
  - 20% chance: t_whiskey
  - 10% chance: t_milk
  - 5% chance: t_honey
  - 5% chance: t_sap

## File Structure
```
external/cdda/data/mods/fungal_reality_shift/
├── modinfo.json
├── items/
│   └── fungal_spore.json
├── effects_on_condition/
│   └── terrain_transformation.json
├── itemgroups/
│   └── fungal_loot.json
└── README.md
```

## Testing Plan
1. Create a new character and start a game
2. Find or spawn fungal_spore item
3. Eat the item and observe status effects
4. Move around and check for terrain changes every minute
5. Verify effect lasts for 24 hours
6. Disassemble fungal creatures to obtain items
7. Check that terrain changes persist after effect ends
8. Balance adjustments based on playtesting