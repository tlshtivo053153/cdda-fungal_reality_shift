# ter_furn_transform Variable Call

## Overview

When specifying an id for `ter_furn_transform`, it should be called via a variable set by `set_string_var`.

## Rule

- The id specified for `ter_furn_transform` should be called via a variable set by `set_string_var`.
- Calling via a variable instead of directly specifying the id improves flexibility and readability.

## Example

```json
{
  "set_string_var": "terrain_transform_frs_<context_val:source_material>_to_<context_val:target_material>",
  "target_var": { "context_val": "transform_id" },
  "parse_tags": true
},
{
  "u_transform_radius": 20,
  "ter_furn_transform": { "context_val": "transform_id" },
  "target_var": { "u_val": "transform_center" }
}
```

## Related Task

- [Conduct a detailed review of the task implementation process and results, perform an objective and honest self-evaluation, and based on that evaluation, propose new rules to be added to .kilocode/rules or improvements to existing rules with concrete examples. The proposed rule ideas should contribute to quality improvement, efficiency, and risk avoidance in future similar tasks.](#)