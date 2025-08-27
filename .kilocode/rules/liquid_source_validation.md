# Liquid Source Validation Guidelines

## Overview

This document provides guidelines for validating liquid source definitions in MOD development.

## Liquid Source Validation

### Item ID Validation

- When adding a new terrain definition with `liquid_source`, ensure that the specified item ID actually exists in the game data.
- Use search tools to verify the existence of the item ID before adding the terrain definition.
- If the item ID does not exist, either find an appropriate existing item ID or consider adding the item definition to the MOD.

### Appropriate Item Selection

- When selecting an item ID for `liquid_source`, choose an item that is logically appropriate for the liquid being represented.
- For example, for a honey liquid, `honey_bottled` is more appropriate than `molasses`.

## Automated Validation

- Implement automated validation checks for liquid source definitions.
- Use continuous integration to run validation checks.
- Include validation checks in the pre-commit hook.

## Review and Approval

- Liquid source definitions should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful validation and review.