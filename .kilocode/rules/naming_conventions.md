# MOD Naming Conventions

## MOD Name
- Use snake case for MOD names.
  - Example: `my_new_mod`, `another_mod_example`

## Version Number
- Use the `v1.0.0` format for version numbers.
  - Example: `v1.0`, `v2.1.3`

## ID Naming Convention
- The MOD's id is prefixed by taking the first letter of each word in the MOD name.
  - Example: If the MOD name is `big_apple_monster`, the id starts with `bam_`.
  - Example: `bam_apple_zombie`, `bam_apple_meat`, etc.

## File Name
- Use snake case for file names.
  - Example: `item_groups.json`, `monster_factions.json`
- For MOD-specific files, prefix the file name with the MOD's ID.
  - Example: `bam_items.json`, `bam_monsters.json`

## JSON Key Name
- Use snake case for JSON key names.
  - Example: `item_name`, `spawn_rate`

## Variable and Function Names
- Use snake case for variable and function names.
  - Example: `spawn_rate`, `calculate_damage()`