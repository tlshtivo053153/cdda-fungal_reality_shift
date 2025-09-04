# JSON Validation Guidelines for Comestible Items

## Overview

This document provides guidelines for validating JSON files related to comestible items in MOD development, specifically regarding the use of effect definitions.

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

## Validation Procedure

1. When validating JSON files, check if items with `comestible_type` have `use_action` with `"type": "effect_on_conditions"`.
2. If such usage is found, flag it as an error and recommend using `consumption_effect_on_conditions` instead.
3. Ensure that `consumption_effect_on_conditions` references valid effect definitions.

## Review and Approval

- JSON files should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful validation and review.