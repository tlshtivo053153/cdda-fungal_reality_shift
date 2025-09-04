# JSON Validation Guidelines

## Overview

This document provides guidelines for validating JSON files in MOD development.

## JSON Syntax Validation

- All JSON files must be syntactically correct.
- Use a JSON validator to check the syntax of JSON files.
- Ensure that all fields are properly closed with commas and braces.

## Field Name Validation

- Verify that all field names are correct and match the expected schema.
- Use the game's JSON documentation to confirm field names.
- Pay special attention to fields that are case-sensitive.

## Dependency Validation

- Check for circular dependencies in recipes and item groups.
- Ensure that all referenced items and groups exist.
- Use tools to visualize and validate dependency graphs.

## Prohibition of `use_action` with `effect_on_conditions` for Comestible Items

- Comestible items (items with `comestible_type`) must not use `use_action` with `"type": "effect_on_conditions"`.
- Instead, use the `consumption_effect_on_conditions` parameter to define effects that occur when the item is consumed.

## Recommended Structure for Comestible Items with Effects

```jsonc
[
  {
    "type": "ITEM",
    "subtypes": [ "COMESTIBLE" ],
    "id": "example_item",
    "comestible_type": "FOOD",
    // ... other fields ...
    "consumption_effect_on_conditions": [ "example_effect" ]
  }
]
```

## Validation Procedure for Comestible Items

1. When validating JSON files, check if items with `comestible_type` have `use_action` with `"type": "effect_on_conditions"`.
2. If such usage is found, flag it as an error and recommend using `consumption_effect_on_conditions` instead.
3. Ensure that `consumption_effect_on_conditions` references valid effect definitions.

## Automated Testing

- Implement automated tests to validate JSON files.
- Use continuous integration to run JSON validation tests.
- Include JSON validation in the pre-commit hook.

## Review and Approval

- JSON files should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful validation and review.