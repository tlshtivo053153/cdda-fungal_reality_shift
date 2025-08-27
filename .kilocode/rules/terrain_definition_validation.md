# Terrain Definition Validation Guidelines

## Overview

This document provides guidelines for validating terrain definitions in MOD development.

## Terrain Definition Validation

### Liquid Source Validation

- When adding a new terrain definition with `liquid_source`, ensure that the specified item ID actually exists in the game data.
- Use search tools to verify the existence of the item ID before adding the terrain definition.
- If the item ID does not exist, either find an appropriate existing item ID or consider adding the item definition to the MOD.

### Naming Convention Validation

- When adding a new terrain definition, check for existing similar terrain IDs to ensure consistency in naming conventions.
- Be aware of potential typos or inconsistencies in naming (e.g., `t_lave` vs `t_lava`).

### Dependency Check

- Ensure that all referenced items and groups in terrain definitions exist.
- Use a reference checker to validate references.
- Handle missing references gracefully.

## Automated Dependency Check

- Implement automated dependency checks for terrain definitions.
- Use continuous integration to run dependency checks.
- Include dependency checks in the pre-commit hook.

## Review and Approval

- Terrain definitions should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful dependency check and review.