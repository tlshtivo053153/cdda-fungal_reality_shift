# Effect on Condition ID Naming and Dependency Management Guidelines

## Overview

This document provides guidelines for naming `effect_on_condition` (EOC) IDs and managing dependencies to prevent conflicts and ensure consistency across the MOD.

## EOC ID Naming Convention

To prevent ID conflicts and improve readability, EOC IDs MUST follow a specific naming convention.

### Format

`EOC_<MOD_PREFIX>_TRANSFORM_<SOURCE_TYPE>_TO_<TARGET_TYPE>_FROM_<SOURCE_MATERIAL>`

- `<MOD_PREFIX>`: The unique prefix for the MOD (e.g., `FRS` for Fungal Reality Shift).
- `<SOURCE_TYPE>`: The type of source being transformed (e.g., `TERRAIN`, `FURNITURE`).
- `<TARGET_TYPE>`: The type of target the source is being transformed into.
- `<SOURCE_MATERIAL>`: The specific material type of the source (e.g., `CONCRETE`, `WOOD`). This part is crucial for uniqueness.

### Examples

- `EOC_FRS_TRANSFORM_TERRAIN_TO_WALL_FROM_CONCRETE`
- `EOC_FRS_TRANSFORM_TERRAIN_TO_BRICK_FROM_WOOD`
- `EOC_FRS_TRANSFORM_FURNITURE_TO_DOOR_FROM_STEEL`

### Rationale

- Including the source material in the ID ensures uniqueness, especially when multiple materials can be transformed into the same target.
- A consistent format improves readability and makes it easier to understand the purpose of an EOC at a glance.

## Dependency Management

When modifying or creating EOCs, it's essential to manage dependencies correctly to avoid broken references and ensure the game functions as expected.

### Checking References

- Before renaming or removing an EOC ID, ALWAYS check for references to that ID in other files.
- Use project-wide search tools (e.g., `grep`, VSCode's search) to find all usages.
- Pay special attention to `weighted_list_eocs` and `queue_eocs` that might reference the EOC.

### Updating References

- When an EOC ID is changed, ALL references to the old ID MUST be updated to the new ID.
- This includes direct references within `effect_on_condition` definitions and indirect references in lists or queues.

### Post-Modification Verification

- After making changes, perform a project-wide search for the old ID to ensure it's no longer used anywhere.
- Test the modified functionality in-game to verify that all transformations and effects work as expected.

## Best Practices

- **Consistency is Key**: Always adhere to the naming convention. Inconsistencies can lead to confusion and errors.
- **Document Complex Logic**: If an EOC implements complex transformation logic, add comments to explain the process.
- **Regular Audits**: Periodically review EOC IDs and their references to ensure continued consistency and correctness, especially after large refactors.
- **Error Handling**: When an error related to an invalid EOC ID occurs, the first step should be to trace the origin of that ID reference, not just fix the symptom. Use the error message to guide your investigation.